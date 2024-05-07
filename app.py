from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesas import Sobremesa
from modelos.cardapio.bebida import Bebida
restaurante_praca = Restaurante('praça','Geral')
sobremesa_1 = Sobremesa('Sorvete',20,'Grande')
sobremesa_1.aplicar_desconto()
prato_1 = Prato('Bife acebolado', 18.99,'Bife acebolado com fritas')
prato_1.aplicar_desconto()
bebida_1 = Bebida('Coca',3.95,'Media')
bebida_1.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(prato_1)
restaurante_praca.adicionar_no_cardapio(sobremesa_1)
restaurante_praca.adicionar_no_cardapio(bebida_1)


def main():
  restaurante_praca.exibir_cardapio
if __name__ =='__main__':
    main()