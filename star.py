# #####################################
#             Bibliotecas             #
# #####################################  

from tupy import *
from time import sleep

# #####################################
#          Variáveis Globais          #
# #####################################  


# #####################################
#            Classe 'Star'            #
# #####################################  

class Star(Image):
    def __init__(self, star) -> None:
        self.file = "Stars/star.png"
        self.x = (star + 1) * 40
        self.y = 450
