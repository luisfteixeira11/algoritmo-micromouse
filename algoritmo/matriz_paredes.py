import API

"""
A matriz de paredes utiliza uma lógica baseada em bits binários para definir as paredes naquela célula,
Cima Baixo Esquerda Direita
 1     0      1        0
ou seja, se o bit designado a cima for 1, tem parede acima, facilitando na parte da adição à uma variável,
pois pode apenas somar 8+2 que vai resultar em 1 0 1 0, que é o mesmo que 12 em binário.
Isso otimiza em relação à necessidade de fazer uma matriz 32x32, pois torna-se um gasto desnecesário de memória.
"""

def atualizar_paredes(matriz, x, y, orientacao):
    # Cima == 1 0 0 0
    cima = 8
    
    # Baixo == 0 1 0 0
    baixo = 4
    
    # Esquerda == 0 0 1 0
    esquerda = 2

    # Direita == 0 0 0 1
    direita = 1

    # Variáveis relacionadas à orientação, pois as paredes são atualizadas de acordo com a visão humana, e não a do rato.
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

    # Parede inicial vazia: 0 0 0 0 == 0
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
    
    
    matriz[y, x] = parede

    return matriz