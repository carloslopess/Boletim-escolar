
#todo: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
#todo: que mantenha separados os valores pares e ímpares. No final, mostre:
#* valores pares e ímpares em ordem crescente.

nums = [[], []] #? pode fazer isso, criar uma lista com outras listas dentro, isso na variavel aq logo.
ask = 0

for c in range(1, 8):
    ask = int(input(f'Digite o {c}o valor: '))
    if ask % 2 == 0:
        nums[0].append(ask)
    else:
        nums[1].append(ask)

print('-='*30)
nums[0].sort()
nums[1].sort()
print()
print(f'Os numeros pares digitados sao {nums[0]}')
print(f'Os numeros impares digitados sao {nums[1]}')
print()
print('-='*30)
