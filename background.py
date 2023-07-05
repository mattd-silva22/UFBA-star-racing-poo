# #####################################
#             Bibliotecas             #
# #####################################  

from tupy import *

# #####################################
#          Variáveis Globais          #
# ##################################### 


# #####################################
#          Classe 'Background'        #
# #####################################  

class Background(BaseImage):
    def __init__(self) -> None:
        super().__init__('Backgrounds/start.png', 450, 250)
      
    def update(self) -> None:
        '''
        Método de atualização de arquivo do objeto da classe 'Background' caso o botão 
        de inicio seja pressionado.
        Este método retorna None.
        ''' 
        if (320 <  mouse.x < 580) and (250 > mouse.y > 200): #botão Start Game
            if mouse.is_button_down():
                self._file = 'Backgrounds/background.png'

    def _move(self) -> None:
        '''
        Método de movimentação do objeto da classe 'Background' (responsavel pela sensa-
        ção de movimento).
        Este método retorna None.
        '''
        self._y = (self._y + 10) % 540 #movimenta o background após o start game

   