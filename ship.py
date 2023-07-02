from tupy import *

class Ship(Image):
    def __init__(self):
        super().__init__('Naves/nave1.png', 450, 450)
        self.is_paused = False
        self._hide()
        self.lifes = 3
        self._is_colliding = False
        self.level = 1

    def has_lifes(self) -> bool:
        return self.lifes > 0

    def get_lifes(self):
        return self.lifes
        
    def collision(self):
        self.lifes -= 1
        self._is_colliding = True
        
    def update(self):
        
        if not self.is_paused:
            if keyboard.is_key_down('Right'): #move a nave para a direita

                if self.x < 850: #impede que a nave saia da tela indo demais para a direita
                    self.x += 15

            elif keyboard.is_key_down('Left'): #move a nave para a esquerda

                if self.x > 60: #impede que a nave saia da tela indo demais para a esquerda
                    self.x -= 15
        
        
        


