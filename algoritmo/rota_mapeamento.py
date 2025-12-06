import API

def rota_mapeamento(x,y,matriz, orientacao):

    matriz_concluida = False

    while matriz_concluida == False:
        #se nenhuma celula da matriz estiver -1 (não visitada)
        #se não der colocar: "(matriz==-1).any()" - o nome disso é mascara boleana, pesquisar depois
        if (matriz != -1).any(): 
            matriz_concluida = True
        
        #encurralado
        if API.wallFront() and API.wallLeft() and API.wallRight():
            API.turnRight90()
            x, y, orientacao = (API.atualizar_coordenada_orientacao(x, y, "D", orientacao))
            API.turnRight90()
            x, y, orientacao = (API.atualizar_coordenada_orientacao(x, y, "D", orientacao))

        #bifurcação parede na frente
        elif API.wallFront() and API.wallLeft()==False and API.wallRight()==False:
            if matriz[x-1][y] == -1:
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            else:
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)

        #bifurcação parede esquerda
        elif API.wallFront()==False and API.wallLeft() and API.wallRight()==False:
            if matriz[x][y-1] == -1:
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
                pass
            else:
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)

        #bifurcação parede direita
        elif API.wallFront()==False  and API.wallLeft()==False and API.wallRight():
            if matriz[x][y-1] == -1:
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
                pass
            else:
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)


        #trifurcação
        elif API.wallFront()==False and API.wallLeft()==False and API.wallRight()==False:
            if matriz [x][y-1] == -1:
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
                pass
            else:
                if matriz[x-1][y] == -1:
                    API.turnLeft90()
                    x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
                else:
                    API.turnRight90()
                    x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)

        #só tem como virar para a direita
        elif API.wallFront() and API.wallLeft():
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)

        #só tem como virar para a esquerda
        elif API.wallFront() and API.wallRight():
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)

        #só tem seguir em frente
        elif API.wallRight() and API.wallLeft():
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
            pass

        API.moveForward()
