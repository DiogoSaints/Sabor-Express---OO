class Restaurante:
    
    restaurantes = []

    def __init__(self,nome,categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} - {self.categoria} - {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante('Praca','Gourmet')
restaurante_praca.alternar_estado()
resttaurante_piza = Restaurante('Pizza','Italiana')
resttaurante_piza.alternar_estado()


Restaurante.listar_restaurantes()