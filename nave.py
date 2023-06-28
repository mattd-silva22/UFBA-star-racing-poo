from tupy import *


class Nave(Image):
    def __init__(self):
        super().__init__('Naves/nave.png', 450, 450)
        self._hide()
        self.vidas = 3
        self._estaBatendo = False

    def getVidas(self):
        return self.vidas
    
    def colisao(self):
        self.vidas -= 1
        
    def update(self):

        if keyboard.is_key_down('Right'): #move a nave para a direita

            if self.x < 850: #impede que a nave saia da tela indo demais para a direita
                self.x += 15

        elif keyboard.is_key_down('Left'): #move a nave para a esquerda

            if self.x > 60: #impede que a nave saia da tela indo demais para a esquerda
                self.x -= 15
    
    
       


