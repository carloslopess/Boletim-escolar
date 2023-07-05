nums = []

for contagem in range(0,5):
    n = int(input('Digite um numero: ')) #numeros que sao adicionados
    if contagem == 0 or n > nums[-1]:# checando se o numero e o maior da lista (add ele no final sempre)
        nums.append(n) # comando para adicionar no final (append)
        print('Numero adicionado no final da lista.')
    else:
        ini = 0 #essa aq indica o inicio da lista, ja que a outra esta adicionando no final da lista.
        while ini < len(nums):#? LEN e usado para checar todos os numeros da lista
            if n <= nums[ini]:
                nums.insert(ini, n)
                print(f'Numero adicionado na posicao {ini} da lista.')
                break
            ini += 1
print('+-'*30)
print(f'Os numeros digitados em ordem sao {nums}')
