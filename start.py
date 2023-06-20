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
       self.contador = 0
       self.vidas = 3

    def update(self):
        self.contador += 1

        if background._file == 'Backgrounds/background.png':

            nave._show() 

            for i in range(len(lista_meteoros)-1):
                lista_meteoros[i]._show()

            if self.contador > 90:

                if self.perde_vida() == True:

                    self.vidas -=1

                else:

                    background.move()

                    for i in range(len(lista_meteoros)-1):
                        lista_meteoros[i].move()
                   
    def perde_vida(self):
        i=0
        for i in range(len(lista_meteoros)-1):
            if nave._collides_with(lista_meteoros[i]):
                return True
            return False

start = StartGame()

run(globals())

