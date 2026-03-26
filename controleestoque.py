from estruturasdados import FilaEstoque
import pickle
from faker import Faker

class Produto: # classe para gerenciar produtos
    def __init__(self, nome, preco_compra, quantidade, data_compra, data_vencimento):
        self.__nome = nome.capitalize()
        self.__preco_compra = float(preco_compra.replace(',', '.')) # replace aceita , para substituir por .
        self.__preco_venda = round(self.__preco_compra * 1.40, 2) # margem de lucro de 40%, round arredonda para duas classes decimais
        self.__quantidade = int(quantidade)
        self.__data_compra = data_compra
        self.__data_vencimento = data_vencimento

    def get_nome(self):     # métodos para acessar e alterar os dados
        return self.__nome
    
    def get_preco_compra(self):
        return self.__preco_compra

    def get_preco_venda(self):
        return self.__preco_venda

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, nova_qtd): #atualiza o estoque após venda
        if nova_qtd >= 0:
            self.__quantidade = nova_qtd

    def get_data_compra(self):
        return self.__data_compra

    def get_data_vencimento(self):
        return self.__data_vencimento

class GerenciarEstoque: # gerenciar estoque total
    def __init__(self): # o primeiro da lista (índice 0) será sempre o mais velho
        self.lista_produtos = FilaEstoque()

    def adicionar_produto(self, produto):
        self.lista_produtos.entrar(produto)
        print(f'Produto {produto.get_nome()} adicionado com sucesso!')

    def mostrar_estoque(self):
        produtos = self.lista_produtos.get_todos()
        if not produtos:
            print('Sem produtos em estoque!')
            return

        print('Estoque de produtos')
        for p in produtos:
            print(f'Produto: {p.get_nome()}, \nQtd: {p.get_quantidade()}, \nPreço: R$ {p.get_preco_venda():.2f}')

    def editar_quantidade(self, nome_busca, nova_qtd): # permite editar a quantidade
        encontrado = False # variável de controle para verificar se o produto existe
        for p in self.lista_produtos.get_todos():
            if p.get_nome() == nome_busca.capitalize():
                p.set_quantidade(int(nova_qtd))
                encontrado = True # se achar
                print(f'Quantidade de {p.get_nome()} atualizada para {nova_qtd}.')
                break
        if not encontrado: # se não achar
            print('Produto não encontrado para edição.')

    def salvar_dados(self): # salvamento de dados (pickle)
        with open('estoque.dat', 'wb') as f:
            pickle.dump(self.lista_produtos, f)

    def carregar_dados(self): # carrega os dados (pickle)
        try:
            with open('estoque.dat', 'rb') as f:
                self.lista_produtos = pickle.load(f)
        except (FileNotFoundError, EOFError):
            pass # se não existir o arquivo, ignora

    def popular_estoque_faker(self):
        fake = Faker('pt_BR')
        produtos_disponiveis = [
            'Coxinha de Frango', 'Kibe com Requeijão', 'Pão de Queijo', 
            'Enroladinho', 'Pastel de Carne', 'Sanduíche Natural',
            'Coca-Cola Lata', 'Suco de Laranja', 'Água Mineral',
            'Barra de Chocolate', 'Trident Hortelã'
        ]
        
        for _ in range(5):
            nome = fake.random_element(elements=produtos_disponiveis) # pega 5 produtos de forma random da lista
            preco_c = round(fake.pyfloat(left_digits=2, right_digits=2, min_value=2.0, max_value=8.0), 2) # define o preço ter 2 digitos antes e depois, no min 2 reais e max 8
            qtd = fake.random_int(min=5, max=20) # quantidade de 5 a 8
            data_c = "25/03/2026"
            data_v = "20/12/2026"

            novo_p = Produto(nome, str(preco_c), qtd, data_c, data_v)
            self.adicionar_produto(novo_p)
            
        self.salvar_dados()
        print('Estoque inicial gerado com sucesso!')