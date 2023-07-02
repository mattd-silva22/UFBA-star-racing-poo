from background import *
from ship import *
from meteor import Meteor
from button import Button
from star import Star
from tupy import *

background = Background()
qtd_lifes = 3
ship = Ship()
pause_button = Button(780, 50, "Buttons/pause.png")
restart_button = Button(870, 50, "Buttons/return.png")
meteors = [Meteor() for meteor in range(10)]
stars = [Star(star) for star in range(qtd_lifes)]
level_limits = [10, 30]

class StartGame(BaseTupyObject):
    
    def __init__(self):
        self.distance = 0
        self.temporizer = 0
        self.game_over = False
        self.pause = False
        self.time_limit_in_seconds = 1
        self.pause_state = False


    def update(self):
        if background._file == 'Backgrounds/background.png':
            self.show_ship_and_buttons()
            self.show_meteors()
            self.show(f"pontos: {int(self.distance)}")

            self.temporizer += 1
            ship.is_paused = pause_button.is_clicked

            if pause_button.is_clicked:
                pause_button.file = "Buttons/forward.png"
                toast("Jogo Pausado")
            
            elif self.pause_state != pause_button.is_clicked:
                pause_button.file = "Buttons/pause.png"

            self.pause_state = pause_button.is_clicked

            if restart_button.is_clicked:
                self.restart_game()
                restart_button.is_clicked = not restart_button.is_clicked
            
            if len(stars) == ship.get_lifes() + 1:
                self.remove_star(ship.get_lifes())
            
            if self.can_begin() and not pause_button.is_clicked:
                self.distance += 0.1
                self.check_ship_level()
                self.pause = False
                for meteor in meteors:
                    if ship._collides_with(meteor) and ship._is_colliding == False:
                        self.pause = True
                        self.temporizer = 0

                        if not ship._is_colliding:
                            ship.collision()

                            if ship.has_lifes():
                                toast("Tente Novamente...")

                            elif len(stars) != 0:
                                self.remove_star(0)
                                toast("Fim de Jogo!")
                                ship._hide()
                                self.game_over = True

                    elif not ship._collides_with(meteor):
                        ship._is_colliding = False

                    else:
                        pass

                if not self.pause:
                    background.move()
                    for i in range(len(meteors)-1):
                        meteors[i].move()

    def show_ship_and_buttons(self):
        global ship, pause_button, restart_button
        ship._show()
        pause_button._show()
        restart_button._show()

    def show_meteors(self):
        global meteors
        for i in range(len(meteors)-1):
            meteors[i]._show()

    def upgrade_ship(self):
        ship.level += 1
        ship.file = f"Naves/nave{ship.level}.png"
        self.show(message="Você subiu de nível!", duration=1000, x=10, y=150)

    def remove_star(self, index):
        global stars
        stars[index]._hide()
        stars.pop()
    
    def check_ship_level(self):
        for level, value in enumerate(level_limits):
            if self.distance > value and ship.level == level + 1:
                self.upgrade_ship()
                break

    def show(self, message: str, duration: int | Literal['idle'] = 2000, x=300, y=100) -> None:
        import tkinter as tk
        label = tk.Label(window.root, text=message, bg="#f0f0f0", font=("Arial", 20))
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
        pause_button = Button(780, 50, "Buttons/pause.png")
        restart_button = Button(870, 50, "Buttons/return.png")
        meteors = [Meteor() for meteor in range(10)]
        stars = [Star(star) for star in range(qtd_lifes)]

    def can_begin(self):
        return self.temporizer/30 > self.time_limit_in_seconds and not self.game_over

start = StartGame()
run(globals())