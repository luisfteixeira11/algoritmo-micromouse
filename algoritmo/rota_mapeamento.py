import API 
import numpy as np

def rota_mapeamento(x,y,matriz):

    matriz_concluida = False

    if matriz != -1: #se nenhuma celula da matriz estiver -1 (não visitada)
        matriz_concluida = True

    while matriz_concluida == False:
        #encurralado
        if API.WallFront() and API.WallLeft() and API.WallRight():
            API.turnRight90()
            API.turnRight90()

        #bifurcação parede na frente
        elif API.WallFront() and API.WallLeft()==False and API.WallRight()==False:
            if matriz[x-1][y] == -1:
                API.turnLeft90()
            else:
                API.turnRight90()

        #bifurcação parede esquerda
        elif API.WallFront()==False  and API.WallLeft() and API.WallRight()==False:
            if matriz[x][y-1] == -1:
                continue
            else:
                API.turnRight90()

        #bifurcação parede direita
        elif API.WallFront()==False  and API.WallLeft()==False and API.WallRight():
            if matriz[x][y-1] == -1:
                continue
            else:
                API.turnLeft90()

        #trifurcação
        elif API.WallFront()==False and API.WallLeft()==False and API.WallRight()==False:
            if matriz [x][y-1] == -1:
                continue
            else:
                if matriz[x-1][y] == -1:
                    API.turnLeft90()
                else:
                    API.turnRight90()
                
        API.moveForward()
