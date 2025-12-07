import API 
from matriz_inundacao import atualizar_inundacao
from matriz_paredes import atualizar_paredes
import numpy as np
from rota_mapeamento import rota_mapeamento
from flood_volta import flood_volta


## A fazer: ajuste da posição inicial da matriz

def main():
    x = 0
    y = 15
    orientacao = 0 
    API.log("Running...")
    # Criação da matriz de paredes com todos os elementos -1
    matriz_parede = np.zeros((16, 16), dtype=int)-1
    # Criação da matriz de inundaçao com todos elementos em -1
    API.setColor(0, 0, "G")
    API.setText(0, 0, "START")
    # Atualização da matriz
    while True:
        matriz_inundacao = np.zeros((16, 16), dtype=int)-1
        # Lógica de virar a matriz. 
        if not API.wallLeft():
            API.turnLeft()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
        while API.wallFront():
            API.turnRight()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
        # Criação da matriz de paredes no contexto atual da célula
        matriz_parede = atualizar_paredes(matriz_parede, x, y, orientacao)
        API.log(matriz_parede)
        # Atualização da matriz de inundação no contexto atual da célula
        matriz_inundacao = flood_volta(matriz_inundacao, matriz_parede)
        API.log(matriz_inundacao)
        matriz_inundacao = atualizar_inundacao(matriz_inundacao, matriz_parede)
        API.log(matriz_inundacao)
        API.moveForward()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
        

        

if __name__ == "__main__":
    main()