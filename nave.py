from tupy import *


class Nave(Image):
    def __init__(self):
        # super().__init__('nave.png', 450, 450)
        self.file = 'nave.png'
        self.x = 450
        self.y = 450
        self._hide()
        
    def update(self):

        if keyboard.is_key_down('Right'): #move a nave para a direita

            if self.x < 850: #impede que a nave saia da tela indo demais para a direita
                self.x += 20

        elif keyboard.is_key_down('Left'): #move a nave para a esquerda

            if self.x > 60: #impede que a nave saia da tela indo demais para a esquerda
                self.x -= 20
       
       


