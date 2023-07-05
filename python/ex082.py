
#*: Crie um programa que vai ler vários números e colocar em uma lista. 
'''
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
conteúdo das três listas geradas.
'''
#* mostrar apenas valores impares
#* mostrar apenas valores pares

lista = list()
imp = list()
par = list()

while True:
    lista.append(int(input('Digite um numero: ')))
    ask = str(input('Deseja continuar? [S]|[N]: ')).upper().strip()
    if ask in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)

print(f'A lista completa e {lista}.')
print(f'Os numeros pares sao {par}.')
print(f'Os numeros impares sao {imp}.')
