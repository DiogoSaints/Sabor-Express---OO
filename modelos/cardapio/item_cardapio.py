from abc import ABC, abstractcmethod

class ItemCardapio(ABC):
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco
    
    @abstractcmethod
    def aplicar_desconto(self):
        pass