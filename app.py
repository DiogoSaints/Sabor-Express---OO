from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_sushi = Restaurante('sushi','japonesa')
restaurante_praca = Restaurante('Praca','Gourmet')
resttaurante_piza = Restaurante('Pizza','Italiana')
bebida_suco = Bebida('Refrigerante',5.00,'2L')
Prato_pizza = Prato('Pizza',25.00,'Pizza maravilhosa')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(Prato_pizza)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()