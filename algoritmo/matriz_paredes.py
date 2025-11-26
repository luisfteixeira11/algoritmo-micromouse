import API
import numpy

def atualizar_paredes(matriz, x, y):
    cima = 8
    baixo = 4
    esquerda = 2
    direita = 1
    parede = 0
    if API.wallFront():
        parede+=cima
    if API.wallBack():
        parede+=baixo
    if API.wallLeft():
        parede+=esquerda
    if API.wallRight():
        parede+=direita
    matriz[x][y] = parede
    return matriz