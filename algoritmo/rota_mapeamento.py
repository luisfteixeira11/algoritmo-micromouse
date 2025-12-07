import API

def rota_mapeamento(x,y,matriz, orientacao):

    cima = y-1
    baixo = y+1
    esquerda = x-1
    direita = x+1

    L = 1
    S = 2
    O = 3

    orientacao = 0

    # Altera a orientação do robô para ele considerar sempre a parte visual do labirinto
    if orientacao == L:
        cima, direita, baixo, esquerda = direita, baixo, esquerda, cima
    elif orientacao == S:
        cima, direita, baixo, esquerda = baixo, esquerda, cima, direita
    elif orientacao == O:
        cima, direita, baixo, esquerda = esquerda, cima, direita, baixo

    #encurralado
    if API.wallFront() and API.wallLeft() and API.wallRight():
        API.turnRight90()
        x, y, orientacao = (API.atualizar_coordenada_orientacao(x, y, "D", orientacao))
        orientacao = (orientacao + L) % 4
        API.turnRight90()
        x, y, orientacao = (API.atualizar_coordenada_orientacao(x, y, "D", orientacao))
        orientacao = (orientacao + L) % 4

    #bifurcação parede na frente
    elif API.wallFront() and API.wallLeft()==False and API.wallRight()==False:
        #esquerda visitada?
        if matriz[esquerda][y] == -1:
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            orientacao = (orientacao - O) % 4
        else:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            orientacao = (orientacao + L) % 4

    #bifurcação parede esquerda
    elif API.wallFront()==False and API.wallLeft() and API.wallRight()==False:
        #frente visitada?
        if matriz[x][cima] == -1:
            pass
        else:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            orientacao = (orientacao + L) % 4

    #bifurcação parede direita
    elif API.wallFront()==False  and API.wallLeft()==False and API.wallRight():
        #frente visitada?
        if matriz[x][cima] == -1:
            pass
        else:
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            orientacao = (orientacao - O) % 4

    #trifurcação
    elif API.wallFront()==False and API.wallLeft()==False and API.wallRight()==False:
        #frente visitada?
        if matriz [x][cima] == -1:
            pass
        else:
            #esquerda visitada?
            if matriz[esquerda][y] == -1:
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
                orientacao = (orientacao - O) % 4
            else:
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
                orientacao = (orientacao + L) % 4

    #só tem como virar para a direita
    elif API.wallFront() and API.wallLeft():
        API.turnRight90()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
        orientacao = (orientacao + L) % 4

    #só tem como virar para a esquerda
    elif API.wallFront() and API.wallRight():
        API.turnLeft90()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
        orientacao = (orientacao - O) % 4

    #só tem seguir em frente
    elif API.wallRight() and API.wallLeft():
        pass

    API.moveForward()
    x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
    API.log(f"orientacao:{orientacao}")
    return x, y, orientacao
