import API 
from matriz_inundacao import atualizar_inundacao
from matriz_paredes import atualizar_paredes
import numpy as np
from rota_mapeamento import rota_mapeamento
from flood_volta import flood_volta
from fastrun import melhor_caminho


def main():
    x = 0
    y = 15
    orientacao = 0 
    
    # Criação da matriz de paredes com todos os elementos -1
    matriz_parede = np.zeros((16, 16), dtype=int)-1
    
    # Criação da matriz de inundaçao com todos elementos em -1
    matriz_inundacao = np.zeros((16, 16), dtype=int)-1
    matriz_volta = np.zeros((16, 16), dtype=int)-1

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
        while matriz_concluida == False:
            matriz_parede = atualizar_paredes(matriz_parede, x, y, orientacao)
            if not -1 in matriz_parede:
                matriz_concluida = True
                API.log("Mapeamento concluido!")
                break
            x, y, orientacao = rota_mapeamento(x, y, matriz_parede, orientacao)
            API.setColor(x, 15-y, "B")
        
        matriz_volta = flood_volta(matriz_volta, matriz_parede)
        API.log(matriz_volta)
        API.log(matriz_parede)
        while True:
            x, y, orientacao = melhor_caminho(x, y, orientacao, matriz_volta, matriz_parede)
            #para quando chega ao centro 
            if (y, x) in [(15, 0)]:
                API.log("Micromouse no START!")
                break
        
        matriz_inundacao = atualizar_inundacao(matriz_inundacao, matriz_parede)
        API.log(matriz_inundacao)
        while True:
            x, y, orientacao = melhor_caminho(x, y, orientacao, matriz_inundacao, matriz_parede)
            #para quando chega ao centro 
            if (y, x) in [(7, 7), (8, 7), (7, 8), (8, 8)]:
                API.log("Você chegou ao seu destino!!")
                break  
        break

        

if __name__ == "__main__":
    main()