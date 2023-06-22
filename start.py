from background import *
from nave import *
from meteoro import *

background = Background()
nave = Nave()
meteoro = Meteoro()
meteoro1 = Meteoro()
meteoro2 = Meteoro()
meteoro3 = Meteoro()
meteoro4 = Meteoro()
meteoro5 = Meteoro()
meteoro6 = Meteoro()
meteoro7 = Meteoro()
meteoro8 = Meteoro()
meteoro9 = Meteoro()
lista_meteoros = [meteoro, meteoro1, meteoro2, meteoro3, meteoro4, meteoro5, meteoro6, meteoro7, meteoro8, meteoro9]


class StartGame(BaseTupyObject):
    def __init__(self):
       self.temporizador = 0
       self.pause = 0

    def update(self):
        
        if background._file == 'Backgrounds/background.png':
            self.temporizador += 1
            nave._show() 

            for i in range(len(lista_meteoros)-1):
                lista_meteoros[i]._show()

            if self.temporizador > 90: #o método update atualiza 30 vezes por segundo, então o jogo começa após 3 segundos
                self.pause = 0
                for i in range(len(lista_meteoros)-1):
                    if nave._collides_with(lista_meteoros[i]):
                        self.pause = 1
                        self.temporizador = 0
                        break

                if self.pause == 0:
                    background.move()
                    for i in range(len(lista_meteoros)-1):
                        lista_meteoros[i].move()
                   

start = StartGame()

run(globals())

