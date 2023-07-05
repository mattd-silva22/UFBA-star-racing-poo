# #####################################
#             Bibliotecas             #
# #####################################  

from background import *
from ship import *
from meteor import Meteor
from button import Button
from star import Star
from typing import Union

# #####################################
#          Variáveis Globais          #
# #####################################  

# #####################################
#          Variáveis Globais          #
# #####################################  

background = Background()
qtd_lifes: int = 3
ship = Ship()
pause_button = Button(780, 50, "Buttons/pause.png")
restart_button = Button(870, 50, "Buttons/return.png")
meteors: list[Meteor] = [Meteor() for meteor in range(10)]
stars: list[Star] = [Star(star) for star in range(qtd_lifes)]
level_limits: list[int] = [10, 30]

# #####################################
#          Classe 'StartGame'         #
# #####################################  

class StartGame(BaseTupyObject):
    
    def __init__(self) -> None:
        self._distance: int = 0
        self._temporizer = 0
        self._game_over = False
        self._pause = False
        self._time_limit_in_seconds = 1
        self._pause_state = False
        self._started = False
        self._x: int
        self._y: int
        self._tkid: int

    def update(self) -> None:
        '''
        Método de Atualização de Tela (30 FPS) dos objetos das classes 'Background' (Plano 
        de Fundo), 'Button' (Botão), 'Meteor' (Meteoro), 'Ship' (Nave) e 'Star' (Estrela) para
        realização das animações e controles do jogo.
        Este método retorna None.
        '''
        if self.clicked_in_start():
            self._temporizer += 1
            self.show_ship_and_buttons()
            self.show_meteors()
            self.show(f"pontos: {int(self._distance/10)}")

            if not self._started and not self.finish_count(5):
                return

            self._started = True
            self.check_buttons()

            if not self._pause:
                self.move_elements()

            if not pause_button._is_clicked and self.can_begin():
                self._distance += 1
                self.check_ship_level()
                self._pause = False

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
        '''
        Método para exibição na tela dos botões de início, reinício e pausa do jogo; e, também
        da nave espacial a ser controlada pelo jogador.
        Este método retorna None.
        '''
        global ship, pause_button, restart_button
        ship._show()
        pause_button._show()
        restart_button._show()

    def finish_count(self, time_limit_in_seconds: float = 3) -> bool:
        '''
        Método contador para exibir na tela uma contagem regressiva 
        com objetivo de alertar ao jogador sobre o início do jogo.
        Este método retorna um Booleano: True, caso o contador chegue
        a 0; ou False, caso o contador seja diferente de 0.
        '''
        count = time_limit_in_seconds - int(self._temporizer/30)

        if count:
            self.show(message=f"{count}", duration=200, x=400, y=300)

        return count == 0
    
    def register_collision(self) -> None:
        '''
        Método de chamada para o Método da classe 'Ship' a fim de registrar colisões.
        Este método retorna None.
        '''
        self._pause = True
        self._temporizer = 0
        ship.collision()

    def show_meteors(self) -> None:
        '''
        Método para exibição dos objetos da Classe 'Meteor' na tela.
        Este método retorna None.
        '''
        global meteors
        for i in range(len(meteors)-1):
            meteors[i]._show()

    @staticmethod
    def clicked_in_start() -> bool:
        '''
        Método Estático para verificação de clique no botão iniciar.
        Este método retorna um Booleano: True, se o botão foi pressionado (imagem de fundo
        inicial foi trocada); ou False, se o botão não foi pressionado (imagem de fundo 
        inicial não foi modificada).
        '''
        return background._file == 'Backgrounds/background.png'
    
    @staticmethod
    def move_elements() -> None:
        '''
        Método Estático para movimentar os objetos das classes 'Meteor' e 'Background'.
        Este método retorna None.
        '''
        background.move()
        for i in range(len(meteors)-1):
            meteors[i].move()

    def upgrade_ship(self) -> None:
        '''       
        Método que modifica dois atributos do objeto da classe 'Ship' após atingir
        uma determinada pontuação: Nível e Arquivo de Imagem.
        Este método retorna None.
        '''
        ship._level += 1
        ship._file = f"Naves/nave{ship._level}.png"
        self.show(message="Voce subiu de nivel!", duration=1000, x=10, y=150)

    def remove_star(self, index: int) -> None:
        '''
        Método que esconde e remove um objeto da classe 'Star' em caso de perda de vidas.
        Este método retorna None.
        '''
        global stars
        stars[index]._hide()
        stars.pop()
    
    def check_ship_level(self) -> None:
        '''
        Método de verificação da distância percorrida (pontuação) pelo jogador para permitir
        a melhoria de nível do objeto da classe 'Ship'.
        Este método retorna None.
        '''
        for level, value in enumerate(level_limits):
            if (self._distance / 10) > value and ship._level == level + 1:
                self.upgrade_ship()
                break

    def check_buttons(self) -> None:
        '''
        Método de verificação se algum objeto da classe 'Button' (botões de pausa e reinício)
        está pressionado para executar suas respectivas funções.
        Este método retorna None.
        '''
        if pause_button._is_clicked:
            pause_button._file = "Buttons/forward.png"
            toast("Jogo Pausado")
        
        elif self._pause_state != pause_button._is_clicked:
            pause_button._file = "Buttons/pause.png"

        if restart_button.get_state():
            self.restart_game()
            restart_button.reset_state()

        self._pause_state = ship._is_paused = pause_button._is_clicked

    def end_game(self) -> None:
        '''
        Método que determina o estado de "fim de jogo" do aplicativo.
        '''
        self.remove_star(0)
        toast("Fim de Jogo!")
        ship._hide()
        self._game_over = True

    def show(self, message: str, duration: int = 2000, x: int =300, y: int =100) -> None:
        '''
        Funçao replica o comportamento da funçao 'toast', mas torna alguns parametros
        mais flexiveis.
        Este método retorna None.
        '''
        import tkinter as tk
        label = tk.Label(window.root, text=message, bg="#000000", fg="#ffffff", font=("Arial", 20))
        label.place(x=x, y=y)
        label.after(duration, label.destroy)

    def restart_game(self) -> None:
        '''
        Método que redefine todos os parâmetros e atributos para seu estado original (início
        do jogo).
        Este método retorna None.
        '''
        global background, qtd_lifes, ship, pause_button, restart_button, meteors, stars
        
        self._distance = 0
        self._temporizer = 0
        self._game_over = False
        background = Background()
        qtd_lifes = 3
        ship = Ship()
        ship.update()
        pause_button = Button(780, 50, "Buttons/pause.png")
        restart_button = Button(870, 50, "Buttons/return.png")
        meteors = [Meteor() for meteor in range(10)]
        stars = [Star(star) for star in range(qtd_lifes)]

    def can_begin(self) -> Union[float, bool]:
        '''
        Método de verificação para novo reinício de jogo.
        Este método retorna um Float, o temporizador; e um Booleano: True, se o atributo 
        game_over for Verdadeiro; ou False, caso contrário.
        '''
        return self._temporizer/30 > self._time_limit_in_seconds and not self._game_over

start = StartGame()
run(globals())