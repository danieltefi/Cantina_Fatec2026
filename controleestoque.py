class Produto: # classe para gerenciar produtos
    def __init__(self, nome, preco_compra, quantidade, data_compra, data_vencimento):
        self.__nome = nome.capitalize()
        self.__preco_compra = float(preco_compra)
        self.__preco_venda = round(self.preco__compra * 1.40, 2) # margem de lucro de 40%, round arredonda para duas classes decimais
        self.__quantidade = int(quantidade)
        self.__data_compra = data_compra
        self.__data_vencimento = data_vencimento

    def get_nome(self):     # métodos para acessar e alterar os dados
        return self.__nome

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, nova_qtd):
        if nova_qtd >= 0:
            self.__quantidade = nova_qtd

    def get_data_compra(self):
        return self.__data_compra

    def get_data_vencimento(self):
        return self.__data_vencimento

class GerenciarEstoque: # gerenciar estoque total
    def __init__(self): # o primeiro da lista (índice 0) será sempre o mais velho
        self.lista_produtos = []

    def adicionar_produto(self, produto):
        self.lista_produtos.append(produto)
        print(f'Produto {produto.get_nome()} adicionado com sucesso!')

    def mostrar_estoque(self):
        if not self.lista_produtos:
            print('Sem produtos em estoque!')
            return

        print('Estoque de produtos')
        for p in self.lista_produtos:
            print(f'Produto: {p.get_nome()}, \nQtd: {p.get_quantidade()}, \nCompra: {p.get_data_compra()}, \nVencimento: {p.get_data_vencimento()}')

    def editar_quantidade(self, nome_busca, nova_qtd): # permite editar a quantidade
        encontrado = False # variável de controle para verificar se o produto existe
        for p in self.lista_produtos:
            if p.get_nome() == nome_busca.capitalize():
                p.set_quantidade(int(nova_qtd))
                encontrado = True # se achar
                print(f'Quantidade de {p.get_nome()} atualizada para {nova_qtd}.')
                break
        if not encontrado: # se não achar
            print('Produto não encontrado para edição.')