import API
from Main import atualizar_coordenada_orientacao

def rota_mapeamento(x,y,matriz):

    matriz_concluida = False

    while matriz_concluida == False:
        #se nenhuma celula da matriz estiver -1 (não visitada)
        if matriz != -1: 
            matriz_concluida = True
        
        #encurralado
        if API.wallFront() and API.wallLeft() and API.wallRight():
            API.turnRight90()
            API.turnRight90()
            x, y, orientacao = (atualizar_coordenada_orientacao(x, y, "D", orientacao))*2

        #bifurcação parede na frente
        elif API.wallFront() and API.wallLeft()==False and API.wallRight()==False:
            if matriz[x-1][y] == -1:
                API.turnLeft90()
                x, y, orientacao = atualizar_coordenada_orientacao(x, y, "E", orientacao)
            else:
                API.turnRight90()
                x, y, orientacao = atualizar_coordenada_orientacao(x, y, "D", orientacao)

        #bifurcação parede esquerda
        elif API.wallFront()==False and API.wallLeft() and API.wallRight()==False:
            if matriz[x][y-1] == -1:
                pass
                x, y, orientacao = atualizar_coordenada_orientacao(x, y, "F", orientacao)
            else:
                API.turnRight90()
                x, y, orientacao = atualizar_coordenada_orientacao(x, y, "D", orientacao)

        #bifurcação parede direita
        elif API.wallFront()==False  and API.wallLeft()==False and API.wallRight():
            if matriz[x][y-1] == -1:
                pass
                x, y, orientacao = atualizar_coordenada_orientacao(x, y, "F", orientacao)
            else:
                API.turnLeft90()
                x, y, orientacao = atualizar_coordenada_orientacao(x, y, "E", orientacao)


        #trifurcação
        elif API.wallFront()==False and API.wallLeft()==False and API.wallRight()==False:
            if matriz [x][y-1] == -1:
                pass
                x, y, orientacao = atualizar_coordenada_orientacao(x, y, "F", orientacao)
            else:
                if matriz[x-1][y] == -1:
                    API.turnLeft90()
                    x, y, orientacao = atualizar_coordenada_orientacao(x, y, "E", orientacao)
                else:
                    API.turnRight90()
                    x, y, orientacao = atualizar_coordenada_orientacao(x, y, "D", orientacao)

        #só tem como virar para a direita
        elif API.wallFront() and API.wallLeft():
            API.turnRight90()
            x, y, orientacao = atualizar_coordenada_orientacao(x, y, "D", orientacao)

        #só tem como virar para a esquerda
        elif API.wallFront() and API.wallRight():
            API.turnLeft90()
            x, y, orientacao = atualizar_coordenada_orientacao(x, y, "E", orientacao)

        #só tem seguir em frente
        elif API.wallRight() and API.wallLeft():
            pass
            x, y, orientacao = atualizar_coordenada_orientacao(x, y, "F", orientacao)


        API.moveForward()
