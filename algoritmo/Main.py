import API as API
import sys
from matriz_inundacao import atualizar_inundacao
from matriz_paredes import atualizar_paredes
import numpy as np


def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()


## A fazer: ajuste da posição inicial da matriz

def main():
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
        # Atualização da matri
        log("Running...")
        # Criação da matrz de inundação no contexto atual da célula
        matriz_parede = atualizar_paredes(matriz_parede, x, y, orientacao)
        # Lógica de virar a matriz
        if not API.wallLeft():
            API.turnLeft()
        while API.wallFront():
            API.turnRight()
        log(matriz_parede)
        log(matriz_inundacao)
        API.moveForward()
        

if __name__ == "__main__":
    main()