'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo 
a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

#* ler o nome de varios alunos;
#* ler duas notas de varios alunos;
#* guardar tudo em uma lista composta;
#* mostrar um boletim com a media de cada aluno individualmente.
#* crie um loop para mostrar novamente alunos existentes ou um novo adicionado

alunos = []

while True:
    aluno = str(input('Digite o nome do aluno (ou digite "sair" para finalizar).\n: '))
    if aluno.lower() == 'sair':
        break

    nota1 = float(input('Digite a primeira nota do aluno\n: '))
    nota2 = float(input('Digite a segunda nota do aluno\n: '))

    alunos.append([aluno, nota1, nota2])

print('\nBoletim dos alunos')

for aluno in alunos:
    nome = aluno[0]
    media = (aluno[1] + aluno[2]) / 2
    print(f'O aluno {nome} teve a media de {media}.')

while True:
    escolha = str(input('Digite o nome do aluno (ou digite "sair" para finalizar).\n:  '))
    if escolha.lower() == 'sair':
        break

    encontrado = False
    for aluno in alunos:
        if aluno[0] == escolha:
            print(f'O aluno {aluno[0]} teve a nota de \n{nota1}\n{nota2}')
            encontrado = True
            break
    if not encontrado:
        break
