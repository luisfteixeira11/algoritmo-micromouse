import numpy
from collections import deque

def atualizar_inundacao(matriz):
    inicio1 = (8,8)
    inicio2 = (8,7) ## zeros na matriz
    inicio3 = (7,8)
    inicio4 = (7,7)

    movimentos = deque() # fila que vai conter as duplas de indices de cada elemento da matriz
    movimentos.append(inicio1)
    movimentos.append(inicio2)
    movimentos.append(inicio3)
    movimentos.append(inicio4)

    distancia = 0  #numero do inicio da matriz

     
    while movimentos: 
        ##enquanto a fila tiver elementos dentro dela, vai continuar o loop
        tamanho_movimentos = len(movimentos)
        for i in range(tamanho_movimentos): ##pra cada elemento da fila
            x = movimentos[0][0]
            y = movimentos[0][1] ##pega as coordenadas da matriz
            if (x>=16 or y>=16 or x<0 or y<0): ##verifica se essa coordenada tá saindo da matriz
                movimentos.popleft()
                continue
            if matriz[x,y]<=distancia and matriz[x,y] != -1: ##verifica se é o melhor caminho possível
                movimentos.popleft() ##se não for apaga
                continue
            matriz[x,y] = distancia
            movimentos.append((x+1,y))
            movimentos.append((x,y+1)) ## se for subscreve e adiciona as coordenadas adjascentes
            movimentos.append((x-1,y))
            movimentos.append((x,y-1))
            movimentos.popleft()
        distancia+=1
    return matriz