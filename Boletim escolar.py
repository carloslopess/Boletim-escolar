
alunos = list()

while True:
    #? aqui recebemos o nome do aluno e fica salvo na variavel
    aluno = str(input('Digite o nome do aluno ("sair" para encerrar.): '))
    if aluno.lower() == 'sair':
        break
    #? agora sera armazenada as notas do aluno
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))

    alunos.append([aluno, nota1, nota2])

print('-='*10, 'Boletim', '=-'*10)
#? nestas linhas e mostrado as medias de cada aluno
for aluno in alunos:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    media = (nota1 + nota2) / 2
    print(f'\nNome: {nome}\nMedia: {media}\n')

while True:
    #? neste loop vamos verificar de o usuario deseja continuar e verificar as notas separadamente de cada aluno
    found=False
    individuo = str(input('Digite o nome do aluno para ver suas notas ("sair" para encerrar): '))
    if individuo.lower() == 'sair':
        break

    for aluno in alunos: #? aqui verificamos se o aluno digitado esta presente na lista
        if aluno[0] == individuo:
            found=True
            nome = aluno[0]
            nota1 = aluno[1]
            nota2 = aluno[2]
            #? mostra as notas separadamente do aluno
            print(f'Nome: {nome}\nNotas: [{nota1}][{nota2}]')
    if not found:
        print('Aluno nao encontrado...')

print('Encerrando...')