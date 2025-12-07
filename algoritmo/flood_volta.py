<<<<<<< HEAD
#implementar corinthians porra

x = 1
=======
from collections import deque
import API

# Ainda não finalizado, importante aprimorar a verificação dos bits

def posicao_acessivel(x1, y1):
    if x1>15 or y1>15 or y1<0 or x1<0:
        return False
    return True

def flood_volta(matriz, paredes):
    inicio1 = (15,0)

    movimentos = deque() # fila que vai conter as duplas de indices de cada elemento da matriz
    movimentos.append(inicio1)

    #numero do inicio da matriz
    distancia = 0

     
    while movimentos: 
        ##enquanto y fila tiver elementos dentro dela, vai continuar o loop
        ##pra cada elemento da fila
        tamanho_movimentos = len(movimentos)
        for i in range(tamanho_movimentos): 
            

            ##pega as coordenadas da matriz
            y, x = movimentos.popleft()
            

            ##verifica se é o melhor caminho possível
            if matriz[y,x]<=distancia and matriz[y,x] != -1:
                continue

            
            ## se for subscreve e adiciona as coordenadas adjascentes
            matriz[y,x] = distancia

            # se no primeiro bit 2⁰==1 (indice 0 do binário ex.0010(que é esse ultimo zero)) não tiver parede na direita
            #a coordenada sucessora pode entrar na fila
            if ((paredes[y,x]&(1<<0))==0 or paredes[y,x]==-1) and posicao_acessivel(x+1,y):
                if (paredes[y,x+1]&(1<<1))==0 or paredes[y,x+1]==-1:
                    movimentos.append((y,x+1))

            # se o segundo bit 2¹==2 (indice 1 do binário) não tiver parede na esquerda pode entrar na fila
            if ((paredes[y,x]&(1<<1))==0 or paredes[y,x]==-1) and posicao_acessivel(x-1,y):
                if (paredes[y,x-1]&(1<<0))==0 or paredes[y,x-1]==-1:
                    movimentos.append((y,x-1))

            # se o terceiro bit 2²==4 (indice 2 do binário) não tiver parede embaixo pode entrar na fila
            if ((paredes[y,x]&(1<<2))==0 or paredes[y,x]==-1) and posicao_acessivel(x,y-1):
                if (paredes[y-1,x]&(1<<3))==0 or paredes[y-1,x]==-1:
                    API.log(paredes[y-1,x]&(1<<3)==0)
                    movimentos.append((y-1,x))

            # se o quarto bit 2³==8 (indice 3 do binário) não tiver parede encima pode entrar na fila
            if ((paredes[y,x]&(1<<3))==0 or paredes[y,x]==-1) and posicao_acessivel(x,y+1):
                if (paredes[y+1,x]&(1<<2))==0 or paredes[y+1,x]==-1:
                    movimentos.append((y+1,x))
        
        distancia+=1

    return matriz
>>>>>>> b70a93ff57ed6778ebcb2724d05cf008deb6ac9f
