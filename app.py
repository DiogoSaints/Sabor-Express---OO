from modelos.restaurante import Restaurante

restaurante_sushi = Restaurante('sushi','japonesa')
restaurante_praca = Restaurante('Praca','Gourmet')
resttaurante_piza = Restaurante('Pizza','Italiana')
















def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()