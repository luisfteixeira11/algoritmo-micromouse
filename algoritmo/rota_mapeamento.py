import API
import random

def rota_mapeamento(x,y,matriz, orientacao):

    cima = (y-1, x)
    baixo = (y+1, x)
    esquerda = (y, x-1)
    direita = (y, x+1)

    N = 0
    L = 1
    S = 2
    O = 3

    def frente():
        pass


    direita_ou_esquerda=[API.turnLeft, API.turnRight]
    direita_ou_frente=[frente, API.turnRight]
    esquerda_ou_frente=[API.turnLeft, frente]
    direita_ou_esquerda_ou_frente=[API.turnLeft, API.turnRight, frente]

    #sentido = orientacao

    # Altera a orientação do robô para ele considerar sempre a parte visual do labirinto
    if orientacao == L:
        cima, direita, baixo, esquerda = direita, baixo, esquerda, cima
    elif orientacao == N:
        cima, direita, baixo, esquerda = cima, direita, baixo, esquerda
    elif orientacao == S:
        cima, direita, baixo, esquerda = baixo, esquerda, cima, direita
    elif orientacao == O:
        cima, direita, baixo, esquerda = esquerda, cima, direita, baixo

    #encurralado
    if API.wallFront() and API.wallLeft() and API.wallRight():
        API.turnRight90()
        x, y, orientacao = (API.atualizar_coordenada_orientacao(x, y, "D", orientacao))
        #sentido = (sentido + 1) % 4
        API.turnRight90()
        x, y, orientacao = (API.atualizar_coordenada_orientacao(x, y, "D", orientacao))
        #sentido = (sentido + 1) % 4

    #bifurcação parede na frente
    elif API.wallFront() and API.wallLeft()==False and API.wallRight()==False:
        #esquerda visitada?
        if matriz[esquerda] == -1:
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            #sentido = (sentido - 1) % 4
        elif matriz[esquerda] != -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            #sentido = (sentido + 1) % 4
        else: #evitar loops quando os adjascentes já foram visitados
            random.choice(direita_ou_esquerda)

    #bifurcação parede esquerda
    elif API.wallFront()==False and API.wallLeft() and API.wallRight()==False:
        #frente visitada?
        if matriz[cima] == -1:
            pass
        elif matriz[cima] != -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            #sentido = (sentido + 1) % 4
        else:#evitar loops quando os adjascentes já foram visitados
            random.choice(direita_ou_frente)

    #bifurcação parede direita
    elif API.wallFront()==False  and API.wallLeft()==False and API.wallRight():
        #frente visitada?
        if matriz[cima] == -1:
            pass
        elif matriz[cima] != -1:
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            #sentido = (sentido - 1) % 4

    #trifurcação
    elif API.wallFront()==False and API.wallLeft()==False and API.wallRight()==False:
        #frente visitada?
        if matriz [cima] == -1:
            API.log(f"orientacao que deveria ser 1: {orientacao}")
            pass
        else:
            #esquerda visitada?
            if matriz[esquerda] == -1:
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
                #sentido = (sentido - 1) % 4
            else:
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
                #sentido = (sentido + 1) % 4

    #só tem como virar para a direita
    elif API.wallFront() and API.wallLeft():
        API.turnRight90()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
        #sentido = (sentido + 1) % 4

    #só tem como virar para a esquerda
    elif API.wallFront() and API.wallRight():
        API.turnLeft90()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
        #sentido = (sentido - 1) % 4

    #só tem seguir em frente
    elif API.wallRight() and API.wallLeft():
        pass

    API.moveForward()
    x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)

    
    return x, y, orientacao
