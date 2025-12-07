import API 
import sys
from matriz_inundacao import atualizar_inundacao
from matriz_paredes import atualizar_paredes
import numpy as np
from rota_mapeamento import rota_mapeamento
from fastrun import melhor_caminho_para_centro



def main():
    x = 0
    y = 15
    orientacao = 0 
    # Criação da matriz de paredes com todos os elementos -1
    matriz_parede = np.zeros((16, 16), dtype=int)-1
    # Criação da matriz de inundaçao com todos elementos em -1
    matriz_inundacao = np.zeros((16, 16), dtype=int)-1
    API.setColor(0, 0, "R")
    API.setText(0, 0, "START")
    API.setColor(7, 7, "G")
    API.setText(7, 7, "END")
    API.setColor(8, 7, "G")
    API.setText(8, 7, "END")
    API.setColor(7, 8, "G")
    API.setText(7, 8, "END")
    API.setColor(8, 8, "G")
    API.setText(8, 8, "END")
    # Atualização da matriz
    while True:
        # Criação da matriz de paredes no contexto atual da célula
        # Atualização da matriz de inundação no contexto atual da célula
        matriz_concluida = False
        matriz_inundacao = atualizar_inundacao(matriz_inundacao, matriz_parede)
        while matriz_concluida == False:
            x, y, orientacao = rota_mapeamento(x, y, matriz_parede, orientacao)
            matriz_parede = atualizar_paredes(matriz_parede, x, y, orientacao)
            #API.log(matriz_inundacao)
            #API.log(matriz_parede)
            API.setColor(x, 15-y, "B")
            if not -1 in matriz_parede:
                matriz_concluida = True
                API.log(matriz_concluida)
            API.log(x)
            API.log(y)
            API.log(orientacao)
        
        melhor_caminho_para_centro(x, y, orientacao, matriz_inundacao, matriz_parede)

        

if __name__ == "__main__":
    main()