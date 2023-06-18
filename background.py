from tupy import *

class Background(Image):
    def __init__(self):
        # super().__init__('start.png', 450, 250)
        self.file = 'start.png'
        self.x = 450
        self.y = 250

    def update(self): 
        if ( 320 <  mouse.x < 580) and (250 > mouse.y > 200): #botão Start Game
            if mouse.is_button_down():
                self.file = 'background.png'
        elif self.file == 'background.png':
            self.y = (self.y + 10) % 540



    
        
                

