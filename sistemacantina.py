

# Define as opções usando dicionários
OPCOES = {
    'categorias': {1: 'Aluno', 2: 'Servidor', 3: 'Professor'},
    'cursos': {1: 'IA', 2: 'ESG'}
}

# Implementa a proteção da senha e dados (Encapsulamento)
class Sistema:
    def __init__(self):
        self.__senhacorreta = 'atletica26' # Senha privada

    def validar_senha(self, digitada):
        return digitada == self.__senhacorreta

class Usuario:
    def __init__(self, nome, cat_id):
        self.nome = nome.upper()
        # Busca a categoria direto no dicionário
        self.categoria = OPCOES['categorias'].get(cat_id, 'Opção Inválida')
        self.curso = 'N/A'

# Implementa o painel administrativo/compras
def rodar_programa():
    sys = Sistema()

    while True:
        try: # garante que o usuario digite apenas 1 ou 2 e não quebre o codigo caso digite uma string
            usuario = int(input('Digite 1 para Admin ou 2 para Comprador: '))
        except ValueError:
            print('Digite apenas 1 para Admin ou 2 para Comprador')
            continue # pula o codigo abaixo e volta ao while

        if usuario == 1:
            print('Painel administrativo. Faça sua autenticação')
            while True:
                senha = input('Digite sua senha: ')
                if sys.validar_senha(senha): # Usa o método da classe para validar
                    print('Autenticação bem sucedida!')
                    break
                else:
                    print('Senha incorreta. Tente novamente')

        elif usuario == 2:
            print('Painel de compras')
            nome = input('Digite seu nome: ').upper()
            try:
                cat_id = int(input('Digite sua categoria: 1 para Aluno, 2 para Servidor ou 3 para Professor: '))
                comprador = Usuario(nome, cat_id) # Cria o objeto comprador
            except ValueError:
                print('Digite apenas 1 para Aluno, 2 para Servidor ou 3 para Professor')
                continue

            if comprador.categoria == 'Aluno':
                try:
                    curso_id = int(input('Qual seu curso? Digite 1 para IA ou 2 para ESG?: '))
                    # Define o curso usando o dicionário
                    comprador.curso = OPCOES['cursos'].get(curso_id, 'Curso não existente')
                except ValueError:
                    print('Digite apenas 1 para IA ou 2 para ESG')
                    continue
            
            # Mostra o resultado final do cadastro
            print(f'\nBem-vindo, {comprador.nome}!')
            print(f'Categoria: {comprador.categoria} | Curso: {comprador.curso}')

        else:
            print('Opção indisponível! Digite 1 para Admin ou 2 para Comprador')
            continue # pula o codigo abaixo e volta ao while

# Inicia o programa
rodar_programa()