
#Fazer jogo da velha em Python

import os
import sys

tabuleiro = [[1,2,3],[4,5,6],[7,8,9]]
valor_auxiliar = 0

def limpar_tela():
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system('clear')
    elif sys.platform == "win32":
        os.system('cls')

def vez():
    if valor_auxiliar % 2 == 0:
        return 'O'
    else:
        return 'X'

def desenhar():
    '''
    Desenha o tabuleiro
    :return:
    '''
    for elem in tabuleiro:
        print(str(elem[0])+ ' ' + str(elem[1]) + ' ' + str(elem[2]))

def linha_vencedorBool(lista):
    '''
    Verifica se há um vencedor numa linha.
    :param lista:
    :return:
    '''
    if len(list(set(lista))) == 1 and type(lista[0]) == str:
        return True
    else:
        return False

def coluna_vencedorBool():
    '''
    Verifica se há um vencedor numa coluna
    :return:
    '''
    if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:
        return True
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:
        return True
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:
        return True
    else:
        return False

def diagonal_vencedorBool():
    '''
    Verifica se há um vencedor na diagonal.
    :return:
    '''
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return True
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return True
    else:
        return False

def linha_vencedor(lista):
    '''
    Retorna o vencedor numa linha
    :param lista:
    :return:
    '''
    return lista[0]

def coluna_vencedor():
    '''
    Retorna o vencedor numa coluna
    :return:
    '''
    if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:
        return tabuleiro[0][0]
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:
        return tabuleiro[0][1]
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:
        return tabuleiro[0][2]

def diagonal_vencedor():
    '''
    Retorna o vencedor na diagonal.
    :return:
    '''
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return tabuleiro[0][0]
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return tabuleiro[0][2]

def verificar():
    '''
    Verifica se há um vencedor.
    :return:
    '''
    if (linha_vencedorBool(tabuleiro[0])) or linha_vencedorBool(tabuleiro[1]) or linha_vencedorBool(tabuleiro[2]):
        return True
    elif diagonal_vencedorBool():
        return True
    elif coluna_vencedorBool():
        return True
    else:
        pass

def vencedor():
    if diagonal_vencedorBool():
        print("O vencedor é o jogador", diagonal_vencedor())
    elif coluna_vencedorBool():
        print("O vencedor é o jogador", coluna_vencedor())
    elif linha_vencedorBool(tabuleiro[0]):
        print("O vencedor é o jogador", linha_vencedor(tabuleiro[0]))
    elif linha_vencedorBool(tabuleiro[1]):
        print("O vencedor é o jogador", linha_vencedor(tabuleiro[1]))
    elif linha_vencedorBool(tabuleiro[2]):
        print("O vencedor é o jogador", linha_vencedor(tabuleiro[2]))

def menu():
    print("\tCOMO JOGAR\nO jogador da vez deve dizer onde quer jogar.\nExemplo: Se quiser jogar no número 5, digite 5.\n")
    global valor_auxiliar
    while True:
        desenhar()
        if verificar():
            vencedor()
            return
        elif velha():
            print("\nDeu velha!")
            return
        valor_auxiliar += 1
        print("\nO jogador " + vez()+ " pode fazer a sua jogada.")
        jogada = int(input())
        for num in range(0,3):
            i = 0
            for elem in tabuleiro[num]:
                if elem == jogada:
                    tabuleiro[num][i] = vez()
                else:
                    i+=1
        limpar_tela()

def tabuleiro_preenchido():
    for l in tabuleiro:
        for num in l:
            if type(num) != str:
                return False
    return True

def velha():
    if tabuleiro_preenchido() and not verificar():
        return True
    else:
        return False

menu()