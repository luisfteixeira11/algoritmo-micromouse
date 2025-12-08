import sys
sys.path.insert(0, '/home/luis/Documentos/algoritmo-micromouse/algoritmo')

import numpy as np
from collections import deque

# Copiar função de teste sem dependência de API
def posicao_acessivel(x1, y1):
    if x1>15 or y1>15 or y1<0 or x1<0:
        return False
    return True

def atualizar_inundacao(matriz, paredes):
    inicio1 = (8,8)
    inicio2 = (8,7)
    inicio3 = (7,8)
    inicio4 = (7,7)

    movimentos = deque()
    movimentos.append(inicio1)
    movimentos.append(inicio2)
    movimentos.append(inicio3)
    movimentos.append(inicio4)

    distancia = 0

    while movimentos:
        tamanho_movimentos = len(movimentos)
        for i in range(tamanho_movimentos): 
            y, x = movimentos.popleft()

            if matriz[y,x]<=distancia and matriz[y,x] != -1:
                continue

            matriz[y,x] = distancia

            # direita (bit 0 == 1)
            nx, ny = x + 1, y
            if posicao_acessivel(nx, ny):
                if ((paredes[y,x] & 1) == 0 or paredes[y,x] == -1) and ((paredes[ny, nx] & 2) == 0 or paredes[ny, nx] == -1):
                    movimentos.append((ny, nx))

            # esquerda (bit 1 == 2)
            nx, ny = x - 1, y
            if posicao_acessivel(nx, ny):
                if ((paredes[y,x] & 2) == 0 or paredes[y,x] == -1) and ((paredes[ny, nx] & 1) == 0 or paredes[ny, nx] == -1):
                    movimentos.append((ny, nx))

            # cima (bit 3 == 8)
            nx, ny = x, y - 1
            if posicao_acessivel(nx, ny):
                if ((paredes[y,x] & 8) == 0 or paredes[y,x] == -1) and ((paredes[ny, nx] & 4) == 0 or paredes[ny, nx] == -1):
                    movimentos.append((ny, nx))

            # baixo (bit 2 == 4)
            nx, ny = x, y + 1
            if posicao_acessivel(nx, ny):
                if ((paredes[y,x] & 4) == 0 or paredes[y,x] == -1) and ((paredes[ny, nx] & 8) == 0 or paredes[ny, nx] == -1):
                    movimentos.append((ny, nx))
        
        distancia+=1
        
    return matriz

# Teste: matriz de paredes vazia (sem paredes = -1)
paredes = np.zeros((16, 16), dtype=int) - 1
matriz = np.zeros((16, 16), dtype=int) - 1

print("Antes do floodfill:")
print(f"Centro (8,8): {matriz[8,8]}")
print(f"Centro (7,7): {matriz[7,7]}")

matriz = atualizar_inundacao(matriz, paredes)

print("\nDepois do floodfill (sem paredes):")
print(f"Centro (8,8): {matriz[8,8]}")
print(f"Centro (7,7): {matriz[7,7]}")
print(f"Ponto (0,0): {matriz[0,0]}")
print(f"Ponto (15,15): {matriz[15,15]}")
print(f"Ponto (15,0): {matriz[15,0]}")
print(f"Ponto (0,15): {matriz[0,15]}")

# Visualizar matriz (primeiras 10x10)
print("\nMatriz de distâncias (10x10 do canto superior):")
print(matriz[0:10, 0:10])
