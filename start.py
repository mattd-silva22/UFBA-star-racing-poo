from background import *
from ship import *
from meteor import Meteor
from button import Button
from star import Star
from tupy import *

background = Background()
qtd_lifes: int = 3
ship = Ship()
pause_button = Button(780, 50, "Buttons/pause.png")
restart_button = Button(870, 50, "Buttons/return.png")
meteors: list = [Meteor() for meteor in range(10)]
stars: list = [Star(star) for star in range(qtd_lifes)]
level_limits: list = [10, 30]

class StartGame(BaseTupyObject):
    
    def __init__(self) -> None:
        self.distance = 0
        self.temporizer = 0
        self.game_over = False
        self.pause = False
        self.time_limit_in_seconds = 1
        self.pause_state = False
        self.started = False

    def update(self) -> None:
        if self.clicked_in_start():
            self.temporizer += 1
            self.show_ship_and_buttons()
            self.show_meteors()
            self.show(f"pontos: {int(self.distance)}")

            if not self.started and not self.finish_count(5):
                return

            self.started = True
            self.check_buttons()

            if not self.pause:
                self.move_elements()

            if not pause_button.is_clicked and self.can_begin():
                self.distance += 0.1
                self.check_ship_level()
                self.pause = False

                for meteor in meteors:
                    if ship._collides_with(meteor): 
                        self.register_collision()
                        
                        if ship.has_lifes():
                            self.remove_star(ship.get_lifes())
                            toast("Tente Novamente...")

                        else:
                            self.end_game()

                        break

                else:
                    ship.set_collision(False)


    def show_ship_and_buttons(self) -> None:
        global ship, pause_button, restart_button
        ship._show()
        pause_button._show()
        restart_button._show()

    def finish_count(self, time_limit_in_seconds: float = 3) -> bool:
        count = time_limit_in_seconds - int(self.temporizer/30)

        if count:
            self.show(message=f"{count}", duration=200, x=400, y=300)

        return count == 0
    
    def register_collision(self) -> None:
        self.pause = True
        self.temporizer = 0
        ship.collision()

    def show_meteors(self) -> None:
        global meteors
        for i in range(len(meteors)-1):
            meteors[i]._show()

    @staticmethod
    def clicked_in_start() -> None:
        return background._file == 'Backgrounds/background.png'
    
    @staticmethod
    def move_elements() -> None:
        background.move()
        for i in range(len(meteors)-1):
            meteors[i].move()

    def upgrade_ship(self) -> None:
        ship.level += 1
        ship.file = f"Naves/nave{ship.level}.png"
        self.show(message="Voce subiu de nivel!", duration=1000, x=10, y=150)

    def remove_star(self, index) -> None:
        global stars
        stars[index]._hide()
        stars.pop()
    
    def check_ship_level(self) -> None:
        for level, value in enumerate(level_limits):
            if self.distance > value and ship.level == level + 1:
                self.upgrade_ship()
                break

    def check_buttons(self) -> None:
        if pause_button.is_clicked:
            pause_button.file = "Buttons/forward.png"
            toast("Jogo Pausado")
        
        elif self.pause_state != pause_button.is_clicked:
            pause_button.file = "Buttons/pause.png"

        if restart_button.get_state():
            self.restart_game()
            restart_button.reset_state()

        self.pause_state = ship.is_paused = pause_button.is_clicked

    def end_game(self):
        self.remove_star(0)
        toast("Fim de Jogo!")
        ship._hide()
        self.game_over = True

    def show(self, message: str, duration: int or Literal['idle'] = 2000, x=300, y=100) -> None:
        """
        Funcao replica o comportamento da funcao 'toast', mas torna alguns parametros
        mais flexiveis.
        """
        import tkinter as tk
        label = tk.Label(window.root, text=message, bg="#000000", fg="#ffffff", font=("Arial", 20))
        label.place(x=x, y=y)
        label.after(duration, label.destroy)

    def restart_game(self):
        global background, qtd_lifes, ship, pause_button, restart_button, meteors, stars
        
        self.distance = 0
        self.temporizer = 0
        self.game_over = False
        background = Background()
        qtd_lifes = 3
        ship = Ship()
        ship.update()
        pause_button = Button(780, 50, "Buttons/pause.png")
        restart_button = Button(870, 50, "Buttons/return.png")
        meteors = [Meteor() for meteor in range(10)]
        stars = [Star(star) for star in range(qtd_lifes)]

    def can_begin(self):
        return self.temporizer/30 > self.time_limit_in_seconds and not self.game_over

start = StartGame()
run(globals())