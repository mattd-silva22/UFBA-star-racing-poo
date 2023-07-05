# #####################################
#             Bibliotecas             #
# #####################################  

from typing import Optional
from tupy import *
import random

# #####################################
#          Variáveis Globais          #
# #####################################  


# #####################################
#           Classe 'Meteor'           #
# #####################################  

class Meteor(Image):
    def __init__(self) -> None:
        self.file = f'Meteors/meteoro{random.randint(1,6)}.png'
        self.x = random.randint(40, 890)
        self._hide()

    def move(self) -> None:
        '''
        Método de movimentação dos objetos da classe 'Meteor'.
        Este método retorna None.
        '''
        self.y = (self.y + 15) % 540
        if self.y < 10:
            self.x = random.randint(40, 890)
            image = random.randint(1, 6)
            self.file = f'Meteors/meteoro{image}.png'