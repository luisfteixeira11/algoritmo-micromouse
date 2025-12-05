from collections import deque

def atualizar_inundacao(matriz, paredes):
    inicio1 = (8,8)
    inicio2 = (8,7) ## zeros na matriz
    inicio3 = (7,8)
    inicio4 = (7,7)

    movimentos = deque() # fila que vai conter as duplas de indices de cada elemento da matriz
    movimentos.append(inicio1)
    movimentos.append(inicio2)
    movimentos.append(inicio3)
    movimentos.append(inicio4)

    #numero do inicio da matriz
    distancia = 0

     
    while movimentos: 
        ##enquanto a fila tiver elementos dentro dela, vai continuar o loop
        ##pra cada elemento da fila
        tamanho_movimentos = len(movimentos)
        for i in range(tamanho_movimentos): 
            

            ##pega as coordenadas da matriz
            x = movimentos[0][0]
            y = movimentos[0][1] 
            
            ##verifica se essa coordenada tá saindo da matriz
            if x>=16 or y>=16 or x<0 or y<0:
                movimentos.popleft()
                continue

            ##verifica se é o melhor caminho possível
            if matriz[x,y]<=distancia and matriz[x,y] != -1: 
                ##se não for apaga
                movimentos.popleft() 
                continue

            
            ## se for subscreve e adiciona as coordenadas adjascentes
            matriz[x,y] = distancia
            if paredes[x,y]&(1<<0)==0 or paredes[x,y]==-1:
                movimentos.append((x-1,y))
            if paredes[x,y]&(1<<1)==0 or paredes[x,y]==-1:
                movimentos.append((x+1,y))
            if paredes[x,y]&(1<<2)==0 or paredes[x,y]==-1:
                movimentos.append((x,y-1))
            if paredes[x,y]&(1<<3)==0 or paredes[x,y]==-1:
                movimentos.append((x,y+1))
            movimentos.popleft()
        distancia+=1
    return matriz