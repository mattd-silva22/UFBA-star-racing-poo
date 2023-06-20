from background import *
from nave import *
from meteoro import *

background = Background()
nave = Nave()
meteoro = Meteoro()
   
class StartGame(BaseTupyObject):
    def __init__(self):
       self.contador = 0

    def update(self):
        self.contador += 1
        if background._file == 'Backgrounds/background.png':
            nave._show() 
            meteoro._show()
            if self.contador > 90:
                background.move()
                meteoro.move()
                   

start = StartGame()

run(globals())