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
        # matriz que marca células visitadas durante o mapeamento (-1 = não visitado)
        matriz_visitado = np.zeros((16, 16), dtype=int)-1
        matriz_concluida = False
        while matriz_concluida == False:
            # atualiza paredes conhecidas a partir da célula atual
            matriz_parede = atualizar_paredes(matriz_parede, x, y, orientacao)
            matriz_visitado[y, x] = 1

            comando, prox = rota_mapeamento(x, y, matriz_visitado, orientacao, matriz_parede)
            if comando is None:
                matriz_concluida = True
                API.log("Mapeamento concluido!")
                break

            # Executa comando relativo retornado pelo planejador
            if comando == "F":
                API.moveForward()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
            elif comando == "D":
                API.turnRight()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
                API.moveForward()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
            elif comando == "E":
                API.turnLeft()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
                API.moveForward()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
            elif comando == "B":
                API.turnRight()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
                API.turnRight()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
                API.moveForward()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)

            API.setColor(x, 15-y, "B")
        
        matriz_volta = flood_volta(matriz_volta, matriz_parede)
        API.log(f"\nMatriz inundação para a volta:\n{matriz_volta}\n")
        API.log(f"\nMatriz paredes:\n{matriz_parede}\n")
        while True:
            x, y, orientacao = melhor_caminho(x, y, orientacao, matriz_volta, matriz_parede)
            #para quando chega ao centro 
            if (y, x) in [(15, 0)]:
                API.log("Micromouse no START!")
                break
        
        matriz_inundacao = atualizar_inundacao(matriz_inundacao, matriz_parede)
        API.log(f"\nMatriz de inundação:\n{matriz_inundacao}\n")
        while True:
            x, y, orientacao = melhor_caminho(x, y, orientacao, matriz_inundacao, matriz_parede)
            #para quando chega ao centro 
            if (y, x) in [(7, 7), (8, 7), (7, 8), (8, 8)]:
                API.log("Você chegou ao seu destino!!")
                break  
        break

        

if __name__ == "__main__":
    main()