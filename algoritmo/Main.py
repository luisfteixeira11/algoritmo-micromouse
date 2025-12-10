import API 
from matriz_inundacao import atualizar_inundacao
from matriz_paredes import atualizar_paredes
import numpy as np
from rota_mapeamento import rota_mapeamento
from flood_volta import atualizar_flood_volta
from fastrun import melhor_caminho
from rota_mapeamento import atualizar_visitacao


def main():

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

    #definição da posição e orientação inicial
    x = 0
    y = 15
    orientacao = 0 
    
    # Criação das matrizes com todos elementos em -1
    matriz_parede = np.zeros((16, 16), dtype=int)-1      #matriz de paredes
    matriz_visitacao = np.zeros((16, 16), dtype=int)-1   #matriz para contar visita nas células durante o mapeamento
    matriz_volta = np.zeros((16, 16), dtype=int)-1       #matriz de flood para voltar ao start
    matriz_inundacao = np.zeros((16, 16), dtype=int)-1   #matriz de flood para ir ao centro

    #variável de controle do mapeamento
    matriz_concluida = False

    API.log("\nMapeando...")
    
    #*mapemento do labirinto
    while matriz_concluida == False:
        #atualiza a matriz de paredes
        matriz_parede = atualizar_paredes(matriz_parede, x, y, orientacao)

        #rota escolhida durante o mapeamento
        x, y, orientacao = rota_mapeamento(x, y, matriz_parede, orientacao, matriz_visitacao)
        
        #conclusão do mapeamento
        if not -1 in matriz_parede:
            matriz_concluida = True
            API.log("\nMapeamento concluido!")
            API.log(f"\nMatriz de Paredes:\n{matriz_parede}")
            break
        
        #estética do caminho mapeado
        API.setColor(x, 15-y, "B")

    API.log("\nRetornando para o Start...")
    
    #atualiza a matriz de flood para a voltar ao start
    matriz_volta = atualizar_flood_volta(matriz_volta, matriz_parede)
    API.log(f"\nMatriz de inundacao para voltar ao Start:\n{matriz_volta}")  
    
    #*volta ao start
    while True:
        #rota mais eficiente para voltar ao start
        x, y, orientacao = melhor_caminho(x, y, orientacao, matriz_volta, matriz_parede)

        #estética do caminho de volta
        API.setColor(x, 15-y, "Y")
        #para quando chega ao centro 
        if (y, x) in [(15, 0)]:
            API.log("\nMicromouse no START!")
            break

    #atualiza a matriz de inundação para ir ao centro         
    matriz_inundacao = atualizar_inundacao(matriz_inundacao, matriz_parede)
    API.log(f"\nMatriz de inundacao para ir ao Centro:\n{matriz_inundacao}")

    #*ida ao centro
    while True:
        x, y, orientacao = melhor_caminho(x, y, orientacao, matriz_inundacao, matriz_parede)
        API.setColor(x, 15-y, "R")
        #para quando chega ao centro 
        if (y, x) in [(7, 7), (8, 7), (7, 8), (8, 8)]:
            API.log("\nVoce chegou ao seu destino!!")
            break  
        
if __name__ == "__main__":
    main()