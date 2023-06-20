from tupy import *

class Background(BaseImage):
    def __init__(self):
        super().__init__('Backgrounds/start.png', 450, 250)
      
    def update(self): 
        if ( 320 <  mouse.x < 580) and (250 > mouse.y > 200): #botão Start Game
            if mouse.is_button_down():
                self._file = 'Backgrounds/background.png'

    def move(self):
        self._y = (self._y + 10) % 540 #movimenta o background após o start game

            



    
        
                

