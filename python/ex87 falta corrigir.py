
'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint

jogos = [[], [], [], [], [], []] #! lista com os jogos

for i in range(len(jogos)):
    #? pergunta de quantos jogos serao feitos
    ask = int(input('Quantos jogos voce quer gerar?\n: '))
    for c in range(ask):
        #? jogos que estao sendo gerados
        numeros = randint(1, 60)
        jogos[i].append(numeros)
    print(jogos)
    
