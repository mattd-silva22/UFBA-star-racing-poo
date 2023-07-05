# #####################################
#             Bibliotecas             #
# #####################################  

from tupy import *

# #####################################
#          Variáveis Globais          #
# #####################################  


# #####################################
#            Classe 'Ship'            #
# #####################################  

class Ship(BaseImage):
    def __init__(self) -> None:
        super().__init__('Naves/nave1.png', 450, 450)
        self._is_paused = False
        self._hide()
        self._lifes = 3
        self._is_colliding = False
        self._level = 1

    def has_lifes(self) -> bool:
        '''
        Método de verificação de quantidade do atributo "lifes".
        Este método retorna um Booleano: True, caso o valor do atributo seja
        maior que 0; False, caso o valor do atributo seja menor ou igual a 0.
        '''
        return self._lifes > 0

    def get_lifes(self) -> int:
        '''
        Método "Getter" do valor do atributo "lifes".
        Este método retorna um Inteiro, seu valor é o valor presente no atri-
        buto "lifes".
        '''
        return self._lifes
        
    def collision(self) -> None:
        '''
        Método modificador de atributos, "lifes" e "_is_colliding" caso seja 
        detectado uma colisão na classe 'StartGame'.
        Este método retorna None.
        '''
        self._lifes -= 1
        self._is_colliding = True
    
    def is_colliding(self) -> bool:
        '''
        Método "Getter" do valor do atributo "_is_colliding".
        Este método retorna um Booleano: True, caso o atributo possua valor
        Verdadeiro; ou False, caso o atributo possua valor Falso.
        '''
        return self._is_colliding
    
    def set_collision(self, value: bool = False) -> None:
        '''
        Método "Setter" do valor do atributo "_is_colliding" para um valor
        Booleano.
        Este método retorna None.
        '''
        self._is_colliding = value
        
    def update(self) -> None:
        
        if not self._is_paused:
            if keyboard.is_key_down('Right'): #move a nave para a direita

                if self._x < 850: #impede que a nave saia da tela indo demais para a direita
                    self._x += 15

            elif keyboard.is_key_down('Left'): #move a nave para a esquerda

                if self._x > 60: #impede que a nave saia da tela indo demais para a esquerda
                    self._x -= 15
        
        
        


