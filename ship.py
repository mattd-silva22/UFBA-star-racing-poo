from tupy import *

class Ship(BaseImage):
    def __init__(self) -> None:
        super().__init__('Naves/nave1.png', 450, 450)
        self._is_paused = False
        self._hide()
        self._lifes = 3
        self._is_colliding = False
        self._level = 1

    def has_lifes(self) -> bool:
        return self._lifes > 0

    def get_lifes(self) -> int:
        return self._lifes
        
    def collision(self) -> None:
        self._lifes -= 1
        self._is_colliding = True
    
    def is_colliding(self) -> bool:
        return self._is_colliding
    
    def set_collision(self, value: bool = False) -> None:
        self._is_colliding = value
        
    def update(self) -> None:
        
        if not self._is_paused:
            if keyboard.is_key_down('Right'): #move a nave para a direita

                if self._x < 850: #impede que a nave saia da tela indo demais para a direita
                    self._x += 15

            elif keyboard.is_key_down('Left'): #move a nave para a esquerda

                if self._x > 60: #impede que a nave saia da tela indo demais para a esquerda
                    self._x -= 15
        
        
        


