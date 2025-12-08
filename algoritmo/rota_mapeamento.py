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

    
    direita_ou_esquerda=[API.turnLeft90, API.turnRight90]
    direita_ou_frente=[frente, API.turnRight90]
    esquerda_ou_frente=[API.turnLeft90, frente]
    direita_ou_esquerda_ou_frente=[API.turnLeft90, API.turnRight90, frente]

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
        #verificadores
        #API.log(f"matriz direita: {matriz[direita]}")
        #API.log(f"matriz esquerda: {matriz[esquerda]}")
        #API.log("bifurcação parede na frente")

        #esquerda visitada?
        if matriz[esquerda] == -1 and matriz[direita] == -1:
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            #sentido = (sentido - 1) % 4
        elif matriz[direita] == -1 and matriz[esquerda] != -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            #sentido = (sentido + 1) % 4
        elif matriz[esquerda] != -1 and matriz[direita] != -1: #evitar loops quando os adjascentes já foram visitados
            escolha = random.choice(["D", "E"])
            
            if escolha == "E":
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            else:
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            

    #bifurcação parede esquerda
    elif API.wallFront()==False and API.wallLeft() and API.wallRight()==False:
        #verificadores
        #API.log(f"matriz cima: {matriz[cima]}")
        #API.log(f"matriz direita: {matriz[direita]}")
        #API.log("Bifurcação parede na esquerda")

        #frente visitada?
        if matriz[cima] == -1 and matriz[direita] == -1:
            pass
        elif matriz[cima] != -1 and matriz[direita] == -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            #sentido = (sentido + 1) % 4
        elif matriz[cima] != -1 and matriz[direita] != -1:#evitar loops quando os adjascentes já foram visitados
            escolha = random.choice(["D", "F"])
            if escolha == "D":
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            else:
                pass

    #bifurcação parede direita
    elif API.wallFront()==False  and API.wallLeft()==False and API.wallRight():
        #verificadores
        #API.log(f"matriz cima: {matriz[cima]}")
        #API.log(f"matriz esquerda: {matriz[esquerda]}")
        #API.log("Bifurcação parede na direita")

        #frente visitada?
        if matriz[cima] == -1 and matriz[esquerda] == -1:
            pass
        elif matriz[cima] != -1 and matriz[esquerda] == -1:
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            #sentido = (sentido - 1) % 4
        elif matriz[cima] != -1 and matriz[esquerda] != -1: 
            escolha = random.choice(["E", "F"])
            if escolha == "E":
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            else:
                pass

    #trifurcação
    elif API.wallFront()==False and API.wallLeft()==False and API.wallRight()==False:
        #verificadores
        #API.log(f"matriz cima: {matriz[cima]}")
        #API.log(f"matriz esquerda: {matriz[esquerda]}")
        #API.log(f"matriz direita: {matriz[direita]}")
        #API.log("trifurcação")

        #frente visitada?
        if matriz[cima] == -1 and matriz[direita] == -1 and matriz[esquerda] == -1:
            pass
        elif matriz[esquerda] == -1 and matriz[cima] != -1 and matriz[direita] == -1: #esquerda visitada?
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            #sentido = (sentido - 1) % 4
        elif matriz[direita] == -1 and matriz[esquerda] != -1 and matriz[cima] != -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            #sentido = (sentido + 1) % 4
        elif matriz[cima] != -1 and matriz[esquerda] != -1 and matriz[direita] != -1:
            escolha = random.choice(["D", "E", "F"])
            if escolha == "D":
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            elif escolha == "E":
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            else:
                pass

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

    if not API.wallFront():
        API.moveForward()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
    else:
    # Se a frente está bloqueada, não avance.
        API.log("Parede à frente, não avançando.")

    
    return x, y, orientacao
