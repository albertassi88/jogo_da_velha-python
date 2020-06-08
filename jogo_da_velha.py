import numpy as np
from jogoDaVelha import tratamento_erro

tabuleiro = [[' 1 ', ' 2 ', ' 3 '], [' 4 ', ' 5 ', ' 6 '], [' 7 ', ' 8 ', ' 9 ']]
print(np.matrix(tabuleiro))

op_j2 = ""
op_nova = ""

op_j1 = str(input('Jogador 1 você escolhe a letra "x" ou "o"?'))
while (op_j1 != 'x') & (op_j1 != 'o'):
    op_j1 = str(input('Opção inválida! Jogador 1 digite a letra "x" ou "o".'))

if op_j1 == 'x':
    op_j2 = 'o'
elif op_j1 == 'o':
    op_j2 = 'x'

print(f'Jogador 2 você vai jogar com a letra: {op_j2}')
resultado = 0
while resultado != 1:

    for n in range(1, 3):
        print("")
        print(f'Jogador {n} agora é a sua vez!')
        numero = tratamento_erro.erro()

        if n != 1:
            op_nova = op_j2
        elif n != 2:
            op_nova = op_j1

        def jogo(numero, op_nova):
            while (numero < 1) | (numero > 9):
                print('Opção Inválida!')
                numero = tratamento_erro.erro()
            if (numero == 1) & (tabuleiro[0][0] == ' 1 '):
                tabuleiro[0][0] = " " + op_nova.upper() + " "
            elif (numero == 2) & (tabuleiro[0][1] == ' 2 '):
                tabuleiro[0][1] = " " + op_nova.upper() + " "
            elif (numero == 3) & (tabuleiro[0][2] == ' 3 '):
                tabuleiro[0][2] = " " + op_nova.upper() + " "
            elif (numero == 4) & (tabuleiro[1][0] == ' 4 '):
                tabuleiro[1][0] = " " + op_nova.upper() + " "
            elif (numero == 5) & (tabuleiro[1][1] == ' 5 '):
                tabuleiro[1][1] = " " + op_nova.upper() + " "
            elif (numero == 6) & (tabuleiro[1][2] == ' 6 '):
                tabuleiro[1][2] = " " + op_nova.upper() + " "
            elif (numero == 7) & (tabuleiro[2][0] == ' 7 '):
                tabuleiro[2][0] = " " + op_nova.upper() + " "
            elif (numero == 8) & (tabuleiro[2][1] == ' 8 '):
                tabuleiro[2][1] = " " + op_nova.upper() + " "
            elif (numero == 9) & (tabuleiro[2][2] == ' 9 '):
                tabuleiro[2][2] = " " + op_nova.upper() + " "

        jogo(numero, op_nova)
        print(np.matrix(tabuleiro))

        if (tabuleiro[0][0] == ' X ') & (tabuleiro[1][1] == ' X ') & (tabuleiro[2][2] == ' X ') | (tabuleiro[0][0] == ' O ') & (tabuleiro[1][1] == ' O ') & (tabuleiro[2][2] == ' O '):
            print(f'Jogador {n} você ganhou!')
            resultado = resultado + 1
        elif (tabuleiro[0][0] == ' X ') & (tabuleiro[1][0] == ' X ') & (tabuleiro[2][0] == ' X ') | (tabuleiro[0][0] == ' O ') & (tabuleiro[1][0] == ' O ') & (tabuleiro[2][0] == ' O '):
            print(f'Jogador {n} você ganhou!')
            resultado = resultado + 1
        elif (tabuleiro[0][1] == ' X ') & (tabuleiro[1][1] == ' X ') & (tabuleiro[2][1] == ' X ') | (tabuleiro[0][1] == ' O ') & (tabuleiro[1][1] == ' O ') & (tabuleiro[2][1] == ' O '):
            print(f'Jogador {n} você ganhou!')
            resultado = resultado + 1
        elif (tabuleiro[0][2] == ' X ') & (tabuleiro[1][2] == ' X ') & (tabuleiro[2][2] == ' X ') | (tabuleiro[0][2] == ' O ') & (tabuleiro[1][2] == ' O ') & (tabuleiro[2][2] == ' O ') :
            print(f'Jogador {n} você ganhou!')
            resultado = resultado + 1
        elif (tabuleiro[0][0] == ' X ') & (tabuleiro[0][1] == ' X ') & (tabuleiro[0][2] == ' X ') | (tabuleiro[0][0] == ' O ') & (tabuleiro[0][1] == ' O ') & (tabuleiro[0][2] == ' O '):
            print(f'Jogador {n} você ganhou!')
            resultado = resultado + 1
        elif (tabuleiro[1][0] == ' X ') & (tabuleiro[1][1] == ' X ') & (tabuleiro[1][2] == ' X ') | (tabuleiro[1][0] == ' O ') & (tabuleiro[1][1] == ' O ') & (tabuleiro[1][2] == ' O '):
            print(f'Jogador {n} você ganhou!')
            resultado = resultado + 1
        elif (tabuleiro[2][0] == ' X ') & (tabuleiro[2][1] == ' X ') & (tabuleiro[2][2] == ' X ') | (tabuleiro[2][0] == ' O ') & (tabuleiro[2][1] == ' O ') & (tabuleiro[2][2] == ' O '):
            print(f'Jogador {n} você ganhou!')
            resultado = resultado + 1
        elif (tabuleiro[2][0] == ' X ') & (tabuleiro[1][1] == ' X ') & (tabuleiro[0][2] == ' X ') | (tabuleiro[2][0] == ' O ') & (tabuleiro[1][1] == ' O ') & (tabuleiro[0][2] == ' O '):
            print(f'Jogador {n} você ganhou!')
            resultado = resultado + 1
        elif ((tabuleiro[0][0] == ' X ') | (tabuleiro[0][0] == ' O ')) & ((tabuleiro[0][1] == ' X ') | (tabuleiro[0][1] == ' O ')) & ((tabuleiro[0][2] == ' X ') | (tabuleiro[0][2] == ' O ')) & ((tabuleiro[1][0] == ' X ') | (tabuleiro[1][0] == ' O ')) & ((tabuleiro[1][1] == ' X ') | (tabuleiro[1][1] == ' O ')) & ((tabuleiro[1][2] == ' X ') | (tabuleiro[1][2] == ' O ')) & ((tabuleiro[2][0] == ' X ') | (tabuleiro[2][0] == ' O ')) & ((tabuleiro[2][1] == ' X ') | (tabuleiro[2][1] == ' O ')) & ((tabuleiro[2][2] == ' X ') | (tabuleiro[2][2] == ' O ')):
            print('Empatou!')
            resultado = resultado + 1

        if not resultado != 1:
            break









