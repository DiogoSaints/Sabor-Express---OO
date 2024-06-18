from modelos.restaurante import Restaurante

restaurante_sushi = Restaurante('sushi','japonesa')
restaurante_praca = Restaurante('Praca','Gourmet')
resttaurante_piza = Restaurante('Pizza','Italiana')

restaurante_praca.receber_avaliacao('Gui',10)
restaurante_praca.receber_avaliacao('Gu',5)















def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()