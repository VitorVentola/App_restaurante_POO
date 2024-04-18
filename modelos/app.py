from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_macarrao = Prato('Macarrao Carbonara', 34.0, 'Carbonara ao molho de cogumelos')
prato_macarrao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_macarrao)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
