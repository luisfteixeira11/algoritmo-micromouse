import API
import numpy



def atualizar_paredes(matriz, y, x, orientacao):
    cima = 8
    baixo = 4
    esquerda = 2
    direita = 1

    dir = 1
    bx = 2
    esq = 3

    if orientacao == dir: ##parte do código que adapta a alteração do código
        cima, direita, baixo, esquerda = direita, baixo, esquerda, cima
    elif orientacao == bx:
        cima, direita, baixo, esquerda = baixo, esquerda, cima, direita
    elif orientacao == esq:
        cima, direita, baixo, esquerda = esquerda, cima, direita, baixo


    parede = 0

    
    if API.wallFront():
        parede+=cima
    if API.wallBack():
        parede+=baixo
    if API.wallLeft():
        parede+=esquerda
    if API.wallRight():
        parede+=direita
        
    matriz[y][x] = parede

    return matriz