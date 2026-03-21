
senhacorreta = 'atletica26'

#Implementa o painel administrativo/compras
while True:
    usuario = int(input('Digite 1 para Admin ou 2 para Comprador?: '))
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
        categoria = input('Digite sua categoria (Aluno, Servidor ou Professor) ').upper()
        if categoria == 'ALUNO':
            curso = int(input('Qual seu curso? Digite 1 para IA ou 2 para ESG?: '))
            if curso == 1:
                curso = 'IA'
            elif curso == 2:
                curso = 'ESG'
            else:
                print('Curso não existente digite 1 para IA ou 2 para ESG')
        else:
            curso = 'N/A'
    else:
        print('Opção indisponível! Digite 1 para Admin ou 2 para Comprador')