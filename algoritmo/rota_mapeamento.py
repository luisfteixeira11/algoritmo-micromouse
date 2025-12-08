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

    # Altera a orientação do robô para ele considerar sempre a parte visual do labirinto
    if orientacao == L:
        cima, direita, baixo, esquerda = direita, baixo, esquerda, cima
    elif orientacao == N:
        cima, direita, baixo, esquerda = cima, direita, baixo, esquerda
    elif orientacao == S:
        cima, direita, baixo, esquerda = baixo, esquerda, cima, direita
    elif orientacao == O:
        cima, direita, baixo, esquerda = esquerda, cima, direita, baixo

    #*encurralado
    if API.wallFront() and API.wallLeft() and API.wallRight():
        API.turnRight90()
        x, y, orientacao = (API.atualizar_coordenada_orientacao(x, y, "D", orientacao))
        
        API.turnRight90()
        x, y, orientacao = (API.atualizar_coordenada_orientacao(x, y, "D", orientacao))
        

    #*bifurcação parede na frente
    elif API.wallFront() and API.wallLeft()==False and API.wallRight()==False:
        #verificadores
        #API.log(f"matriz direita: {matriz[direita]}")
        #API.log(f"matriz esquerda: {matriz[esquerda]}")
        API.log("bifurcacao parede na frente")

        #esquerda visitada?
        if matriz[esquerda] == -1 and matriz[direita] == -1:
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)

        elif matriz[direita] == -1 and matriz[esquerda] != -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            
        elif matriz[esquerda] != -1 and matriz[direita] != -1: #evitar loops quando os adjascentes já foram visitados
            escolha = random.choice(["D", "E"])
            API.log(f"escolha aleatoria: {escolha}")
            if escolha == "E":
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            else:
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            

    #*bifurcação parede esquerda
    elif API.wallFront()==False and API.wallLeft() and API.wallRight()==False:
        #verificadores
        #API.log(f"matriz cima: {matriz[cima]}")
        #API.log(f"matriz direita: {matriz[direita]}")
        API.log("Bifurcacao parede na esquerda")

        #frente visitada?
        if matriz[cima] == -1 and matriz[direita] == -1:
            pass

        elif matriz[cima] != -1 and matriz[direita] == -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            
        elif matriz[cima] != -1 and matriz[direita] != -1:#evitar loops quando os adjascentes já foram visitados
            escolha = random.choice(["D", "F"])
            API.log(f"escolha aleatoria: {escolha}")
            if escolha == "D":
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            else:
                pass

    #*bifurcação parede direita
    elif API.wallFront()==False  and API.wallLeft()==False and API.wallRight():
        #verificadores
        #API.log(f"matriz cima: {matriz[cima]}")
        #API.log(f"matriz esquerda: {matriz[esquerda]}")
        API.log("Bifurcacao parede na direita")

        #frente visitada?
        if matriz[cima] == -1 and matriz[esquerda] == -1:
            pass

        elif matriz[cima] != -1 and matriz[esquerda] == -1:
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)

        elif matriz[cima] != -1 and matriz[esquerda] != -1: 
            escolha = random.choice(["E", "F"])
            API.log(f"escolha aleatoria: {escolha}")
            if escolha == "E":
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            else:
                pass

    #*trifurcação
    elif API.wallFront()==False and API.wallLeft()==False and API.wallRight()==False:
        #verificadores
        #API.log(f"matriz cima: {matriz[cima]}")
        #API.log(f"matriz esquerda: {matriz[esquerda]}")
        #API.log(f"matriz direita: {matriz[direita]}")
        API.log("trifurcacao")

        #frente visitada?
        if matriz[cima] == -1 and matriz[direita] == -1 and matriz[esquerda] == -1:
            pass

        elif matriz[esquerda] == -1 and matriz[cima] != -1 and matriz[direita] == -1: #esquerda visitada?
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)

        elif matriz[direita] == -1 and matriz[esquerda] != -1 and matriz[cima] != -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            
        elif matriz[cima] != -1 and matriz[esquerda] != -1 and matriz[direita] != -1:
            escolha = random.choice(["D", "E", "F"])
            API.log(f"escolha aleatoria: {escolha}")
            if escolha == "D":
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            elif escolha == "E":
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            else:
                pass

    #*só tem como virar para a direita
    elif API.wallFront() and API.wallLeft():
        API.turnRight90()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
        

    #*só tem como virar para a esquerda
    elif API.wallFront() and API.wallRight():
        API.turnLeft90()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
        

    #*só tem seguir em frente
    elif API.wallRight() and API.wallLeft():
        pass

    #*depois de cada turn, é necessário seguir em frente, e o código vem logo em seguida para esse moveForward
    #*quando não acontecerá nenhum turn, mas somente seguir em frente, o código também vem para esse moveForward
    if not API.wallFront():
        API.moveForward()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
    else:
    # Se a frente está bloqueada, não avance.
        API.log("Parede à frente, não avancando.")
        escolha = random.choice(["D", "E"])
        
        if escolha == "E":
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
        else:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)

    
    return x, y, orientacao
