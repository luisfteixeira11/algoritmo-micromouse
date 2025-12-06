from collections import deque

# Ainda não finalizado, importante aprimorar a verificação dos bits

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
        ##enquanto y fila tiver elementos dentro dela, vai continuar o loop
        ##pra cada elemento da fila
        tamanho_movimentos = len(movimentos)
        for i in range(tamanho_movimentos): 
            

            ##pega as coordenadas da matriz
            y = movimentos[0][0]
            x = movimentos[0][1] 
            
            ##verifica se essa coordenada tá saindo da matriz
            if y>=16 or x>=16 or y<0 or x<0:
                x, y = movimentos.popleft()
                continue

            ##verifica se é o melhor caminho possível
            if matriz[y,x]<=distancia and matriz[y,x] != -1:
                ##se não for apaga
                x, y = movimentos.popleft() 
                continue

            
            ## se for subscreve e adiciona as coordenadas adjascentes
            matriz[y,x] = distancia

            # se no primeiro bit 2⁰==1 (indice 0 do binário ex.0010(que é esse ultimo zero)) não tiver parede na direita
            #a coordenada sucessora pode entrar na fila
            if (paredes[y,x]&(1<<0))==0 or paredes[y,x]==-1:
                movimentos.append((y,x+1))

            # se o segundo bit 2¹==2 (indice 1 do binário) não tiver parede na esquerda pode entrar na fila
            if (paredes[y,x]&(1<<1))==0 or paredes[y,x]==-1:
                movimentos.append((y,x-1))

            # se o terceiro bit 2²==4 (indice 2 do binário) não tiver parede embaixo pode entrar na fila
            if (paredes[y,x]&(1<<2))==0 or paredes[y,x]==-1:
                movimentos.append((y-1,x))

            # se o quarto bit 2³==8 (indice 3 do binário) não tiver parede encima pode entrar na fila
            if (paredes[y,x]&(1<<3))==0 or paredes[y,x]==-1:
                movimentos.append((y+1,x))
            movimentos.popleft()
        distancia+=1
    return matriz