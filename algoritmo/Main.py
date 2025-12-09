import API 
from matriz_inundacao import atualizar_inundacao
from matriz_paredes import atualizar_paredes
import numpy as np
from rota_mapeamento import rota_mapeamento
from flood_volta import atualizar_flood_volta
from fastrun import melhor_caminho


def main():
    x = 0
    y = 15
    orientacao = 0 
    
    # Criação da matriz de paredes com todos os elementos -1
    matriz_parede = np.zeros((16, 16), dtype=int)-1
    
    # Criação da matriz de inundaçao com todos elementos em -1
    matriz_volta = np.zeros((16, 16), dtype=int)-1

    #estética do start e do end
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
    

    while True:
        matriz_concluida = False
        
        #mapemento
        while matriz_concluida == False:
            matriz_parede = atualizar_paredes(matriz_parede, x, y, orientacao)

            #criação e atualização da matriz de inundação
            matriz_inundacao = np.zeros((16, 16), dtype=int)-1
            matriz_inundacao = atualizar_inundacao(matriz_inundacao, matriz_parede)
            
            #conclusão do mapeamento
            if not -1 in matriz_parede:
                matriz_concluida = True
                API.log("Mapeamento concluido!")
                API.log("Retornando para o Start...")
                break
            
            #roda escolhida durante o mapeamento
            x, y, orientacao = rota_mapeamento(x, y, matriz_parede, orientacao, matriz_inundacao)
            
            API.setColor(x, 15-y, "B")
        
        #atualiza a matriz de flood para a volta ao start
        matriz_volta = atualizar_flood_volta(matriz_volta, matriz_parede)

        #volta ao start
        while True:
            x, y, orientacao = melhor_caminho(x, y, orientacao, matriz_volta, matriz_parede)
            API.setColor(x, 15-y, "Y")
            #para quando chega ao centro 
            if (y, x) in [(15, 0)]:
                API.log("Micromouse no START!")
                break
        
        #ida ao centro
        while True:
            x, y, orientacao = melhor_caminho(x, y, orientacao, matriz_inundacao, matriz_parede)
            API.setColor(x, 15-y, "R")
            #para quando chega ao centro 
            if (y, x) in [(7, 7), (8, 7), (7, 8), (8, 8)]:
                API.log("Voce chegou ao seu destino!!")
                break  
        break


if __name__ == "__main__":
    main()