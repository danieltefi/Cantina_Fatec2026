from datetime import datetime

class Pagamento:
    def __init__(self, comprador, produto):
        self.cliente = comprador.nome
        self.categoria = comprador.categoria
        self.curso = comprador.curso
        self.item = produto.nome
        self.valor = produto.preco_venda
        self.data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # captura data e hora do sistema no momento da criação do objeto

class GerenciarPagamentos:
    def __init__(self):
        self.historico_vendas = []

    def processar_pix(self, pagamento):
        print(f'PAGAMENTO PIX \nValor: R$ {pagamento.valor}')
        confirmar = input("PIX foi enviado? (S/N): ").upper()
        
        if confirmar == 'S':
            self.historico_vendas.append(pagamento)
            print(f'Venda registrada com sucesso em: {pagamento.data_hora}')
            return True
        else:
            print('Pagamento não realizado.')
            return False