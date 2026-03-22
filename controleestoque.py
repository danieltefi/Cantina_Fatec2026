class Produto: # classe para gerenciar produtos
    def __init__(self, nome, preco_compra, preco_venda, quantidade, data_compra, data_vencimento):
        self.nome = nome.capitalize()
        self.preco_compra = float(preco_compra)
        self.preco_venda = float(preco_venda)
        self.quantidade = int(quantidade)
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento

class GerenciarEstoque: # gerenciar estoque total
    def __init__(self): # o primeiro da lista (índice 0) será sempre o mais velho
        self.lista_produtos = []

    def adicionar_produto(self, produto):
        self.lista_produtos.append(produto)
        print(f'Produto {produto.nome} adicionado com sucesso!')

    def mostrar_estoque(self):
        if not self.lista_produtos:
            print('Sem produtos em estoque!')
            return

        print('Estoque de produtos')
        for p in self.lista_produtos:
            print(f'Produto: {p.nome}, \nQtd: {p.quantidade}, \nCompra: {p.data_compra}, \nVencimento: {p.data_vencimento}')

    def editar_quantidade(self, nome_busca, nova_qtd): # permite editar a quantidade
        encontrado = False # variável de controle para verificar se o produto existe
        for p in self.lista_produtos:
            if p.nome == nome_busca.capitalize():
                p.quantidade = int(nova_qtd)
                encontrado = True # se achar
                print(f'Quantidade de {p.nome} atualizada para {nova_qtd}.')
                break
        if not encontrado: # se não achar
            print('Produto não encontrado para edição.')