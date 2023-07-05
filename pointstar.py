# #####################################
#             Bibliotecas             #
# #####################################

from meteor import *
import random

# #####################################
#          Variáveis Globais          #
# #####################################  


# #####################################
#          Classe 'PointStar'         #
# #####################################  

class PointStar(Meteor):
    def __init__(self) -> None:
        self.file = 'Stars/pointstar.png'
        self._hide()

    def move(self) -> None:
        '''
        Método de movimentação dos objetos da classe 'PointStar'.
        Este método retorna None.
        '''
        self.y = (self.y + 15) % 540
        if self.y < 10:
            self.x = random.randint(40, 890)