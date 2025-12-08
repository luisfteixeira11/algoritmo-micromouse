import API

# Matriz de paredes foi finalizada

def atualizar_paredes(matriz, x, y, orientacao):
    cima = 8
    baixo = 4
    esquerda = 2
    direita = 1

    dir = 1
    bx = 2
    esq = 3
    
    # Altera a orientação do robô para ele considerar sempre a parte visual do labirinto
    if orientacao == dir:
        cima, direita, baixo, esquerda = direita, baixo, esquerda, cima
    elif orientacao == bx:
        cima, direita, baixo, esquerda = baixo, esquerda, cima, direita
    elif orientacao == esq:
        cima, direita, baixo, esquerda = esquerda, cima, direita, baixo

    parede = 0

    # Faz a soma dos valores da parede
    if API.wallFront():
        parede+=cima
    if API.wallBack():
        parede+=baixo
    if API.wallLeft():
        parede+=esquerda
    if API.wallRight():
        parede+=direita

    #se não tiver parede
    
    
    matriz[y, x] = parede

    return matriz