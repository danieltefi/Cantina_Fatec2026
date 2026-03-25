class ItemCarrinho:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__subtotal = produto.get_preco_venda() * quantidade

    def get_produto(self): # getters para permitir a leitura
        return self.__produto
    def get_quantidade(self): 
        return self.__quantidade
    def get_subtotal(self): 
        return self.__subtotal

class Carrinho:
    def __init__(self):
        self.__itens = [] # lista encapsulada

    def adicionar(self, produto, quantidade):
        novo_item = ItemCarrinho(produto, quantidade)
        self.__itens.append(novo_item)

    def get_total(self): # soma os subtotais de cada item
        return sum(item.get_subtotal() for item in self.__itens)

    def get_itens(self): # mostra os itens do carrinho
        return self.__itens

    def limpar(self): # limpa o carrinho
        self.__itens = []