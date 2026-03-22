# implementa a proteção da senha (Encapsulamento)
class Sistema:
    def __init__(self):
        self.__senhacorreta = 'atletica26' # senha privada para segurança

    def validar_senha(self, digitada):
        return digitada == self.__senhacorreta

# classe para guardar os dados de quem compra
class Usuario:
    def __init__(self, nome, categoria, curso='N/A'):
        self.nome = nome.upper()
        self.categoria = categoria
        self.curso = curso

# implementa o painel administrativo/compras
def rodar_programa():
    sys = Sistema()

    while True:
        try: # garante que o usuario digite apenas 1 ou 2 e não quebre o codigo caso digite uma string
            print('Cantina Atlética Fatec 2026')
            print('1 - Administrador, 2 - Comprador')
            usuario = int(input('Digite o número da sua opção: '))
        except ValueError:
            print('Opção inválida! Digite apenas 1 para Admin ou 2 para Comprador')
            continue # pula o codigo abaixo e volta ao while

        if usuario == 1:
            print('Painel administrativo. Faça sua autenticação')
            senha = input('Digite sua senha: ')
            if sys.validar_senha(senha): # usa o método da classe para validar
                print('Autenticação bem sucedida!')
            else:
                print('Senha incorreta!')

        elif usuario == 2:
            print('Painel de compras')
            nome = input('Digite seu nome: ').capitalize()
            
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
            
                comprador = Usuario(nome, categoria, curso) # cria o objeto direto com os textos digitados
            
                # mostra o resultado final
                print(f'\nBem-vindo, {comprador.nome}!')
                print(f'Categoria: {comprador.categoria} | Curso: {comprador.curso}')

            except ValueError:
                print('Erro: Digite apenas os números das opções!')
                continue

        else:
            print('Opção indisponível! Digite 1 para Admin ou 2 para Comprador')

# inicia o programa
rodar_programa()