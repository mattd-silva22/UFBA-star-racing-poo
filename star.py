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

class Star(BaseImage):
    def __init__(self, star:int ) -> None:
        super().__init__("Stars/star.png", (star + 1) * 40, 450)
