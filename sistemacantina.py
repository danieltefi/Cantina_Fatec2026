
senhacorreta = 'atletica26'

#Implementa o painel administrativo/compras
while True:
    try: #garante que o usuario digite apenas 1 ou 2 e não quebre o codigo caso digite uma string
        usuario = int(input('Digite 1 para Admin ou 2 para Comprador: '))
    except ValueError:
        print('Digite apenas 1 para Admin ou 2 para Comprador')
        continue #pula o codigo abaixo e volta ao while

    if usuario == 1:
        print('Painel administrativo. Faça sua autenticação')
        while True:
            senha = input('Digite sua senha: ')
            if senha == senhacorreta:
                print('Autenticação bem sucedida!')
                break
            else:
                print('Senha incorreta. Tente novamente')

    elif usuario == 2:
        print('Painel de compras')
        nome = input('Digite seu nome: ').upper()
        try:
            categoria = int(input('Digite sua categoria 1 para Aluno, 2 para Servidor ou 3 para Professor) '))
        except ValueError:
            print('Digite apenas 1 para Aluno, 2 para Servidor ou 3 para Professor')
            continue

        if categoria == 1:
            categoria = 'Aluno'
            try:
                curso = int(input('Qual seu curso? Digite 1 para IA ou 2 para ESG?: '))
            except ValueError:
                print('Digite apenas 1 para IA ou 2 para ESG')
                continue
            
            if curso == 1:
                curso = 'IA'
            elif curso == 2:
                curso = 'ESG'
            else:
                print('Curso não existente digite 1 para IA ou 2 para ESG')
        elif categoria == 2:
            categoria = 'Servidor'
            curso = 'N/A'
        elif categoria == 3:
            categoria = 'Professor'
            curso = 'N/A'
        else:
            print('Opção Inválida! Digite 1 para Aluno, 2 para Servidor ou 3 para Professor')

    else:
        print('Opção indisponível! Digite 1 para Admin ou 2 para Comprador')
        continue #pula o codigo abaixo e volta ao while