class FilaEstoque:
    def __init__(self):
        self.__produtos = [] # lista encapsulada

    def entrar(self, item):
        self.__produtos.append(item) # adiciona ao final da fila

    def sair(self):
        if not self.vazia():
            return self.__produtos.pop(0) # remove o primeiro (mais velho - FIFO)

    def vazia(self):
        return len(self.__produtos) == 0 # se esta sem produtos
    
    def get_todos(self): # retorna relatórios e visualização
        return self.__produtos

class ListaVendas:
    def __init__(self):
        self.__vendas = [] # lista encapsulada

    def registrar(self, venda): # adiciona um novo registro de pagamento
        self.__vendas.append(venda)

    def vazia(self):
        return len(self.__vendas) == 0
    
    def get_todas(self): # retorna as vendas para relatório
        return self.__vendas