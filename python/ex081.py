
#* | Crie um programa que vai ler vários números e colocar em uma lista.
#* | Depois disso, mostre:
#* | A) Quantos números foram digitados.
#* |   B) A lista de valores, ordenada de forma decrescente.
#* |     C) Se o valor 5 foi digitado e está ou não na lista.

nums = []
while True:
    nums.append(int(input(' Digite um numero: ')))
    ask = str(input('Quer continuar? [S]|[N]: ')).strip().upper()
    if ask == 'N':
        break

print(f'Foram digitados {len(nums)} numeros.')
nums.sort(reverse=True) #? Com isso deixamos a lista em ordem decrescente, utilizando sort( com protocolo reverse=True)
print(f'De forma decrescente a lista fica assim:\n{nums}')
if 5 in nums:
    print('O numero 5 esta presente na lista.')
else:
    print('O numero 5 nao esta presente na lista.')
