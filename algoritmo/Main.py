import API 
import sys
from matriz_inundacao import atualizar_inundacao
from matriz_paredes import atualizar_paredes
import numpy as np
from rota_mapeamento import rota_mapeamento


def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

N = 0
L = 1
S = 2
O = 3

def atualizar_coordenada_orientacao(x, y, movimento, orientacao):
    if movimento == "F":
        if orientacao == N:
            y -= 1
        elif orientacao == S:
            y += 1
        elif orientacao == L:
            x += 1
        elif orientacao == O:
            x -= 1
    if movimento == "D":
        orientacao = (orientacao + 1) % 4
    if movimento == "E":
        orientacao = (orientacao -1) % 4

    return x, y, orientacao     



## A fazer: ajuste da posição inicial da matriz

def main():
    x = 0
    y = 15
    orientacao = 0 
    log("Running...")
    # Criação da matriz de paredes com todos os elementos -1
    matriz_parede = np.zeros((16, 16), dtype=int)-1
    # Criação da matriz de inundaçao com todos elementos em -1
    matriz_inundacao = np.zeros((16, 16), dtype=int)-1
    API.setColor(0, 0, "G")
    API.setText(0, 0, "START")
    while True:
        # Atualização da matriz de inundação no contexto atual da célula
        matriz_inundacao = atualizar_inundacao(matriz_inundacao)
        # Atualização da matriz
        log("Running...")
        # Criação da matrz de inundação no contexto atual da célula
        matriz_parede = atualizar_paredes(matriz_parede, x, y, orientacao)
        # Lógica de virar a matriz. 
        if not API.wallLeft():
            API.turnLeft()
            x, y, orientacao = atualizar_coordenada_orientacao(x, y, "E", orientacao)
        while API.wallFront():
            API.turnRight()
            x, y, orientacao = atualizar_coordenada_orientacao(x, y, "D", orientacao)
        log(matriz_parede)
        log(matriz_inundacao)
        API.moveForward()
        x, y, orientacao = atualizar_coordenada_orientacao(x, y, "F", orientacao)
        log(x)
        log(y)

        

if __name__ == "__main__":
    main()