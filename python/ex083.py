
#todo: Crie um programa que verifique se uma expressão é valida.

expr = str(input('Digite uma expressao: '))
pilha = list()

for simbolo in expr:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta correta')
else:
    print('Sua expressao esta errada.')
