
#todo: faça um programa que leia o nome e peso de varias pessoas, guardando tudo em uma lista. E no final, mostre:
#* Quantas pessoas foram cadastradas
#* Uma listagem com as pessoas mais pesadas
#* Uma listagem com as pessoas mais leves

pessoas = list()
nome = list()
peso = list()
pesop = pesoL = cont = 0
temp = list()

while True:
    temp.append((str(input('Nome: '))))
    temp.append((int(input('Peso: '))))
    if len(pessoas) == 0:
        pesop = pesoL = temp[1]
    else:
        if temp[1] > pesop:
            pesop = temp[1]
        if temp[1] < pesoL:
            pesoL = temp[1]
    pessoas.append(temp[:])
    temp.clear()

    cont += 1
    ask = str(input('Deseja continuar?\n[S]/[N]: ')).strip()[0]
    if ask in 'Nn':
        break
print('-='*30)
print(f'Os dados completos sao {pessoas}')
print(f'O total de pessoas cadastradas foram {cont}')
print(f'O maior peso registrado foi de {pesop}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesop:
        print(f'{p[0]}')
print(f'O menor peso registrado foi de {pesoL}kg. Peso de ')
for p in pessoas:
    if p[1] == pesoL:
        print(f'{p[0]}')
