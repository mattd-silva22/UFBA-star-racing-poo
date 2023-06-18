from background import *
from nave import *

background = Background()
nave = Nave()

class StartGame(BaseTupyObject):
    def update(self):
        if background.file == 'background.png':
            nave._show() #mostra a nave após o botão start game
            background.y = (background.y + 10) % 540 #movimenta o background após o start game

start = StartGame()
run(globals())