from collections import deque

"""
O adicionar_inundação é uma função que, considerando a matriz de paredes já concluída, retorna uma matriz de inundação (Floodfill)
que á como a inundação de um rio partindo dos pontos iniciais, até o ponto mais distante, adicionando a distância de cada célula até o inicio
ele auxilia na busca pelo melhor caminho possível tanto para a volta ao início, quanto para a ida ao centro.
"""

def posicao_acessivel(x1, y1):
    if x1>15 or y1>15 or y1<0 or x1<0:
        return False
    return True

def flood_volta(matriz, paredes):
    ## zeros na matriz, ou seja, a chegada
    inicio1 = (15,0)

    # fila que vai conter as duplas de indices de cada elemento da matriz
    movimentos = deque() 

    #adição dos quatro valores setados como zero (os valores finais)
    movimentos.append(inicio1)

    #numero do inicio da matriz
    distancia = 0

     
    while movimentos:
        ##enquanto y fila tiver elementos dentro dela, vai continuar o loop
        tamanho_movimentos = len(movimentos)
        ##pra cada elemento da fila ela irá entrar no laço for para interagir com a posição atual
        for i in range(tamanho_movimentos): 
            
            ##pega as coordenadas da matriz
            y, x = movimentos.popleft()
            
            ##verifica se é o melhor caminho possível, se não for ele repete o laço sem executar o resto
            if matriz[y,x]<=distancia and matriz[y,x] != -1:
                continue

            
            ## se for melhor subscreve e adiciona as coordenadas adjascentes
            matriz[y,x] = distancia

            #se a posição for acessível ele pode entrar
            if posicao_acessivel(x+1, y):
            # se no primeiro bit 2⁰==1 (indice 0 do binário ex.0010(que é esse ultimo zero)) não tiver parede na direita pode adicionar o adjascente
                if ((paredes[y,x]&1)==0 or paredes[y,x]==-1) and ((paredes[y,x+1]&2)==0 or paredes[y,x+1]==-1):
                    movimentos.append((y,x+1))

            # se o segundo bit 2¹==2 (indice 1 do binário) não tiver parede na esquerda pode adicionar o adjascente
            if posicao_acessivel(x-1,y):
                if ((paredes[y,x]&2)==0 or paredes[y,x]==-1) and ((paredes[y,x-1]&1)==0 or paredes[y,x-1]==-1):
                    movimentos.append((y,x-1))

            # se o terceiro bit 2²==4 (indice 2 do binário) não tiver parede embaixo pode adicionar o adjascente
            if posicao_acessivel(x,y-1):
                if ((paredes[y,x]&8)==0 or paredes[y,x]==-1) and ((paredes[y-1,x]&4)==0 or paredes[y-1,x]==-1):
                    movimentos.append((y-1,x))

            # se o quarto bit 2³==8 (indice 3 do binário) não tiver parede encima pode adicionar o adjascente
            if posicao_acessivel(x,y+1):
                if ((paredes[y,x]&4)==0 or paredes[y,x]==-1) and ((paredes[y+1,x]&8)==0 or paredes[y+1,x]==-1):
                    movimentos.append((y+1,x))
        
        distancia+=1
        
    return matriz