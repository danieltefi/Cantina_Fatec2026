from controleestoque import Produto, GerenciarEstoque
from controlepagamento import GerenciarPagamentos
from carrinho import Carrinho
from usuarios import Sistema, Usuario
from faker import Faker

def rodar_programa(): # implementa o painel administrativo/compras
    sys = Sistema()
    estoque = GerenciarEstoque() # acesso à prateleira de produtos
    estoque.carregar_dados() # tenta carregar dados salvos anteriormente
    if not estoque.lista_produtos.get_todos(): # se estiver vazio
        print('Estoque vazio. Gerando dados iniciais automaticamente...')
        popular_estoque_faker(estoque) # gera os dados automaticamente
    financeiro = GerenciarPagamentos()
    financeiro.carregar_dados() # carrega as vendas do arquivo 'vendas.dat'

    while True:
        try: # garante que o usuario digite apenas 1 ou 2 e não quebre o codigo caso digite uma string
            print('Cantina Atlética FATEC 2026, \n1 - Administrador, \n2 - Comprador')
            usuario = int(input('Digite o número da sua opção: '))
        except ValueError:
            print('Opção inválida! Digite apenas 1 para Admin ou 2 para Comprador')
            continue # pula o codigo abaixo e volta ao while

        if usuario == 1:
            print('PAINEL ADMINISTRATIVO. \nFaça sua autenticação')
            senha = input('Digite sua senha: ')

            if sys.validar_senha(senha): # usa o método da classe para validar
                print('Autenticação bem sucedida!')

                while True: #permite cadastrar vários produtos seguidos, sem precisar precisar digitar a senha novamente
                    print('MENU ADMINISTRADOR \n1 - Cadastrar produto, \n2 - Ver estoque, \n3 - Editar quantidade, \n4 - Relatório de Vendas, \n0 - Sair do painel Admin')
                    
                    try:
                        op_admin = int(input('Escolha uma opção: '))
                    except ValueError:
                        print('Inválido! Digite apenas os números.')
                        continue

                    if op_admin == 1:
                        nome = input('Nome do produto: ')
                        preco_compra = input('Preço de compra: ')
                        quantidade = input('Quantidade: ')
                        data_compra = input('Data de compra: ')
                        data_vencimento = input('Data de vencimento: ')

                        novo_p = Produto(nome, preco_compra, quantidade, data_compra, data_vencimento) # cria o objeto produto e adiciona ao estoque
                        estoque.adicionar_produto(novo_p)
                        estoque.salvar_dados() # salva os dados no arquivo

                    elif op_admin == 2:
                        estoque.mostrar_estoque()

                    elif op_admin == 3:
                        nome_busca = input('Nome do produto a ser editado: ')
                        nova_qtd = input('Nova quantidade: ')
                        estoque.editar_quantidade(nome_busca, nova_qtd)
                        estoque.salvar_dados() # salva os dados no arquivo

                    elif op_admin == 4:
                        financeiro.exibir_relatorio()

                    elif op_admin == 0:
                        break # Sai do menu admin e volta ao menu principal
                    else:
                        print('Opção inválida! Digite 0, 1, 2 ou 3')
            else:
                print('Senha incorreta!')

        elif usuario == 2:
            print('PAINEL DE COMPRAS')
            nome = input('Digite seu nome: ')
            
            try:
                print('1 - Aluno, 2 - Servidor, 3 - Professor')
                op_cat = int(input('Digite o número da sua categoria: '))
                
                if op_cat == 1:
                    categoria = 'Aluno'
                elif op_cat == 2:
                    categoria = 'Servidor'
                elif op_cat == 3:
                    categoria = 'Professor'
                else:
                    print('Opção inválida! Digite apenas 1 para Aluno, 2 para Servidor ou 3 para Professor')
                    continue

                curso = 'N/A'
                if categoria == 'Aluno':
                    print('1 - IA, 2 - ESG')
                    op_curso = int(input('Digite o número do seu curso: '))
                    if op_curso == 1:
                        curso = 'IA'
                    elif op_curso == 2:
                        curso = 'ESG'
                    else:
                        print('Opção inválida! Digite apenas 1 para IA ou 2 para ESG')
                        continue
            
                comprador = Usuario(nome, categoria, curso) # cria o objeto usuário
                meu_carrinho = Carrinho() # cria um carrinho para o usuário
            
                print(f'Bem-vindo, {comprador.get_nome()}!, \nCategoria: {comprador.get_categoria()}, \nCurso: {comprador.get_curso()}') # mostra o resultado final

                while True:
                    print('PRODUTOS DISPONÍVEIS')
                    estoque.mostrar_estoque() 

                    escolha = input('Digite o nome do produto, "Fim" para pagar ou "Sair" para cancelar: ').capitalize()

                    if escolha == 'Sair':
                        meu_carrinho.limpar()
                        break

                    if escolha == 'Fim':
                        if meu_carrinho.get_total() > 0:
                            financeiro.processar_venda_carrinho(comprador, meu_carrinho) # chama o metodo (mostra total, registra e baixa estoque)
                            
                            print('Compra finalizada com sucesso!')
                            break
                        else:
                            print('Carrinho vazio!')
                            continue

                    achou = False 
                    for p in estoque.lista_produtos.get_todos():
                        if p.get_nome() == escolha:
                            achou = True 
                            if p.get_quantidade() > 0:
                                try:
                                    qtd_desejada = int(input(f'Quantidade de {p.get_nome()} em número: '))
                                    if 0 < qtd_desejada <= p.get_quantidade(): # se a quantidade requerida é maior que zero e menor do que a quantidade em estoque
                                        meu_carrinho.adicionar(p, qtd_desejada) # adiciona ao carrinho
                                        print(f'{qtd_desejada}x {p.get_nome()} adicionado ao carrinho.')
                                    else:
                                        print('Quantidade indisponível.')
                                except ValueError:
                                    print('Digite um número inteiro para a quantidade.')
                            else:
                                print(f'Desculpe, o produto {p.get_nome()} está esgotado.')
                            break
                    
                    if not achou:
                        print('Produto não encontrado.')

            except ValueError:
                print('Erro: Digite apenas os números das opções!')
                continue

        else:
            print('Opção indisponível! Digite 1 para Admin ou 2 para Comprador')

rodar_programa() # inicia o programa

def popular_estoque_faker(gerente_estoque): # geração de dados aleatórios 
    fake = Faker('pt_BR')
    for _ in range(5): # gera 5 produtos de exemplo
        nome = fake.word().capitalize()
        preco_c = round(fake.pyfloat(left_digits=2, right_digits=2, min_value=1.0, max_value=10.0), 2)
        qtd = fake.random_int(min=5, max=20)
        data_c = "25/03/2026"
        data_v = "01/12/2026"
        
        novo_p = Produto(nome, str(preco_c), qtd, data_c, data_v)
        gerente_estoque.adicionar_produto(novo_p)
    gerente_estoque.salvar_dados() # salva os dados gerados 
    print('Estoque gerado com sucesso via Faker!')