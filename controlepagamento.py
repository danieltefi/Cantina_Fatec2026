from datetime import datetime
from estruturasdados import ListaVendas

class Pagamento:
    def __init__(self, comprador, produto):
        self.__cliente = comprador.get_nome()
        self.__categoria = comprador.get_categoria()
        self.__curso = comprador.get_curso()
        self.__item = produto.get_nome()
        self.__valor = produto.get_preco_venda()
        self.__data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # captura data e hora do sistema no momento da criação do objeto

    def get_cliente(self): return self.__cliente # permitir a leitura dos dados pelo relatório
    def get_categoria(self): return self.__categoria
    def get_curso(self): return self.__curso
    def get_item(self): return self.__item
    def get_valor(self): return self.__valor
    def get_data_hora(self): return self.__data_hora

class GerenciarPagamentos:
    def __init__(self):
        self.historico_vendas = ListaVendas()

    def processar_pix(self, pagamento):
        print(f'PAGAMENTO PIX \nValor: R$ {pagamento.get_valor()}')
        confirmar = input("PIX foi enviado? (S/N): ").upper()
        
        if confirmar == 'S':
            self.historico_vendas.registrar(pagamento)
            print(f'Venda registrada com sucesso em: {pagamento.get_data_hora()}')
            return True
        else:
            print('Pagamento não realizado.')
            return False
        
    def exibir_relatorio(self): # exibe o relatório de vendas
        print('RELATÓRIO DE VENDAS (PIX)')
        vendas = self.historico_vendas.get_todas()
        if not self.historico_vendas.vazia(): 
            for v in vendas:
                print(f'Data: {v.get_data_hora()}, \nCliente: {v.get_cliente()}, {v.get_categoria()}, {v.get_curso()}, \nItem: {v.get_item()}, \nValor: R$ {v.get_valor()}')
        else:
            print('Nenhuma venda realizada até o momento.')