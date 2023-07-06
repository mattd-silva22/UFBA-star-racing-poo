# #####################################
#             Bibliotecas             #
# #####################################  

from tupy import *
from time import sleep

# #####################################
#          Variáveis Globais          #
# ##################################### 


# #####################################
#           Classe 'Button'           #
# #####################################  

class Button(BaseImage):
    def __init__(self, x: int, y: int, file: str) -> None:
        self._file = file
        self._x = x
        self._y = y
        self._is_clicked = False

    def update(self) -> None:
        '''
        Método de Verificação do posicionamento do Mouse para pressionamento
        dos objetos da classe 'Button'.
        Este método retorna None.
        '''
        if (self._x <  mouse.x < self._x + 80) and (self._y - 20 < mouse.y < self._y + 80):
            if mouse.is_button_down():
                self._click()
                sleep(0.5)

    def _click(self) -> None:
        '''
        Método para funcionalidade de clique no objeto da classe 'Button'.
        Este método retorna None.   
        '''
        self._is_clicked = not self._is_clicked
    
    def _get_state(self) -> bool:
        '''
        Método "Getter" para o valor do atributo "is_clicked".
        Este método retorna um Booleano: True, se o atributo "is_clicked"
        for Verdadeiro; ou False, se o atributo "is_clicked"for Falso.
        '''
        return self._is_clicked
    
    def _reset_state(self) -> None:
        '''
        Método de redefinição do atributo "is_clicked" para seu valor original.
        Este método retorna None.
        '''
        self._is_clicked = False
        
if __name__ == '__main__':
    pause_button = Button(10, 10, "pausa.png")
    restart_button = Button(10, 10, "return.png")

    print(dir(pause_button))
    pause_button._click()
