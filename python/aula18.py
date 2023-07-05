'''teste = list()
teste.append('Carlos')
teste.append('18')
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = '19'
galera.append(teste[:])
print(galera)'''

'''galera = [['Carlos', 18], ['Maria', 19], ['Juca', 20]]
for p in galera:
    print(p)'''

'''galera = list()
dado = list()
totmaior = totmenor = 0'''

'''for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()'''

'''
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} e maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} e menor de idade')
        totmenor += 1

print(f'Temos no total {totmaior} maiores de idade e {totmenor} menores de idade.')'''
