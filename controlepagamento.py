from datetime import datetime
from estruturasdados import ListaVendas
from carrinho import Carrinho

class Pagamento:
    def __init__(self, comprador, produto):
        self.__cliente = comprador.get_nome()
        self.__categoria = comprador.get_categoria()
        self.__curso = comprador.get_curso()
        self.__item = produto.get_nome()
        self.__valor = produto.get_preco_venda()
        self.__data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # captura data e hora do sistema no momento da criação do objeto

    def get_cliente(self): # permitir a leitura dos dados pelo relatório
        return self.__cliente
    def get_categoria(self): 
        return self.__categoria
    def get_curso(self): 
        return self.__curso
    def get_item(self): 
        return self.__item
    def get_valor(self): 
        return self.__valor
    def get_data_hora(self): 
        return self.__data_hora

class GerenciarPagamentos:
    def __init__(self):
        self.historico_vendas = ListaVendas()
        
    def exibir_relatorio(self): # exibe o relatório de vendas
        print('RELATÓRIO DE VENDAS (PIX)')
        vendas = self.historico_vendas.get_todas()
        if not self.historico_vendas.vazia(): 
            for v in vendas:
                print(f'Data: {v.get_data_hora()}, \nCliente: {v.get_cliente()}, {v.get_categoria()}, {v.get_curso()}, \nItem: {v.get_item()}, \nValor: R$ {v.get_valor()}')
        else:
            print('Nenhuma venda realizada até o momento.')

    def processar_venda_carrinho(self, comprador, carrinho):
        total = carrinho.get_total()
        
        print(f"Processando PIX no valor de: R$ {total:.2f}")
        
        for item in carrinho.get_itens():
            produto = item.get_produto() # qual o produto
            quantidade = item.get_quantidade() # qual a quantidade

            for i in range(quantidade): # roda o loop (quantidade)x
                nova_venda = Pagamento(comprador, produto) # cria um novo pagamento para cada unidade
                self.historico_vendas.registrar(nova_venda) # registra na lista de vendas

            nova_qtd = int(produto.get_quantidade()) - quantidade # o que tem no estoque - o que esta levando e atualiza no estoque
            produto.set_quantidade(nova_qtd)