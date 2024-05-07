from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = [] # Restaurantes é igual a uma lista vazia

    def __init__(self,nome,categoria):
        self._nome = nome.title() # Title deixa a primeira letra maiúscula
        self._categoria = categoria
        self._ativo = False # esse _ significa que o atributo n pode ser mexido
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) # todo o Restaurante que for criado vai ser colocado na lista

    def __str__(self):  # Método que transforma em string
        return f'{self._nome} | {self._categoria}'  # O que queremos exibir da class Restaurante o nome e categoria
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(24)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}')
    @property
    def ativo(self):
        return 'Ⓥ' if self._ativo else 'Ⓕ'

    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self,cliente,nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Restaurante sem avaliações'
        soma_das_notas = (sum(avaliacao._nota for avaliacao in self._avaliacao ))
        quantidade_de_notas = len(self._avaliacao)
        if any(avaliacao._nota > 5 for avaliacao in self._avaliacao):
            return 'Avaliação inválida - nota maior que 5'
        media = round(soma_das_notas / quantidade_de_notas,1)
        return media
            
    '''def adicionar_prato_no_cardapio(self,prato):
        self._cardapio.append(prato)  # criei uma lista para colocar o prato no cardapio
        is
    def adicionar_sobremesa_no_cardapio(self,sobremesa):
        self._cardapio.append(sobremesa) # criei uma lista para colocara sobremesa no cardapio'''
    # Como prato e sobremesa tem parametros iguais, não faz sentido ter 2 métodos, vamos criar um só
    def adicionar_no_cardapio(self,item):
        if isinstance (item,ItemCardapio):
            self._cardapio.append(item)
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_sobremesa = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_sobremesa)