import API
import random
import fastrun as fr

def rota_mapeamento(x, y, matriz_paredes, orientacao):

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

    #encurralado
    if API.wallFront() and API.wallLeft() and API.wallRight():
        #volta de 180°
        API.turnRight90()
        x, y, orientacao = (API.atualizar_coordenada_orientacao(x, y, "D", orientacao))
        API.turnRight90()
        x, y, orientacao = (API.atualizar_coordenada_orientacao(x, y, "D", orientacao))

        
    #bifurcação parede na frente
    elif API.wallFront() and API.wallLeft()==False and API.wallRight()==False:
<<<<<<< HEAD
        #verificadores
        #API.log(f"matriz direita: {matriz[direita]}")
        #API.log(f"matriz esquerda: {matriz[esquerda]}")
        API.log("bifurcacao parede na frente")
=======
>>>>>>> e3f5d98d9bccac0a84f47c97ce8fb17d4e9fe3fa

        #se a esquerda nem a direita tiver sido visitada: vire a esquerda
        if matriz_paredes[esquerda] == -1 and matriz_paredes[direita] == -1:
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)

        #se a esquerda já tiver sido visitada e a direita não: vire a direita
        elif matriz_paredes[direita] == -1 and matriz_paredes[esquerda] != -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)

        #se a direita e a esquerda já estiver explorada: escolha aleatória para evitar loops
        elif matriz_paredes[esquerda] != -1 and matriz_paredes[direita] != -1:
            
            escolha = random.choice(["D", "E"])
            if escolha == "E":
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            else:
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)       
            

    #bifurcação parede esquerda
    elif API.wallFront()==False and API.wallLeft() and API.wallRight()==False:
<<<<<<< HEAD
        #verificadores
        #API.log(f"matriz cima: {matriz[cima]}")
        #API.log(f"matriz direita: {matriz[direita]}")
        API.log("Bifurcacao parede na esquerda")
=======
>>>>>>> e3f5d98d9bccac0a84f47c97ce8fb17d4e9fe3fa

        #se a frente nem a direita tiver sido visitada: siga em frente
        if matriz_paredes[cima] == -1 and matriz_paredes[direita] == -1:
            pass #leva direto para o moveForward

        #se a frente já tiver sido visitada e a direita não: vire a direita
        elif matriz_paredes[cima] != -1 and matriz_paredes[direita] == -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            
        #se a direita e a frente já estiver explorada: escolha aleatória para evitar loops
        elif matriz_paredes[cima] != -1 and matriz_paredes[direita] != -1:
            escolha = random.choice(["D", "F"])
            if escolha == "D":
                API.turnRight90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            else:
                pass

<<<<<<< HEAD
    #*bifurcação parede direita
    elif API.wallFront()==False  and API.wallLeft()==False and API.wallRight():
        #verificadores
        #API.log(f"matriz cima: {matriz[cima]}")
        #API.log(f"matriz esquerda: {matriz[esquerda]}")
        API.log("Bifurcacao parede na direita")
=======
>>>>>>> e3f5d98d9bccac0a84f47c97ce8fb17d4e9fe3fa

    #bifurcação parede direita
    elif API.wallFront()==False  and API.wallLeft()==False and API.wallRight():

        #se a frente nem a esquerda tiver sido visitada: siga em frente
        if matriz_paredes[cima] == -1 and matriz_paredes[esquerda] == -1:
            pass

        #se a frente já tiver sido visitada e a esquerda não: vire a esquerda
        elif matriz_paredes[cima] != -1 and matriz_paredes[esquerda] == -1:
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)

        #se a esquerda e a frente já estiver explorada: escolha aleatória para evitar loops
        elif matriz_paredes[cima] != -1 and matriz_paredes[esquerda] != -1: 
            escolha = random.choice(["E", "F"])
            if escolha == "E":
                API.turnLeft90()
                x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
            else:
                pass
            
    #trifurcação
    elif API.wallFront()==False and API.wallLeft()==False and API.wallRight()==False:
<<<<<<< HEAD
        #verificadores
        #API.log(f"matriz cima: {matriz[cima]}")
        #API.log(f"matriz esquerda: {matriz[esquerda]}")
        #API.log(f"matriz direita: {matriz[direita]}")
        API.log("trifurcacao")
=======
>>>>>>> e3f5d98d9bccac0a84f47c97ce8fb17d4e9fe3fa

        #se a frente não tiver sido explorada: siga em frente
        if matriz_paredes[cima] == -1 and matriz_paredes[direita] == -1 and matriz_paredes[esquerda] == -1:
            pass

        #se a frente já foi explorada: vire a esquerda
        elif matriz_paredes[esquerda] == -1 and matriz_paredes[cima] != -1 and matriz_paredes[direita] == -1: 
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)

        #se a frente e a esquerda já foram exploradas: vire a direita
        elif matriz_paredes[direita] == -1 and matriz_paredes[esquerda] != -1 and matriz_paredes[cima] != -1:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)

        #se todos os adjascentes já foram explorados: escolha aleatória para evitar loops
        elif matriz_paredes[cima] != -1 and matriz_paredes[esquerda] != -1 and matriz_paredes[direita] != -1:
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
        

    #só tem como virar para a esquerda
    elif API.wallFront() and API.wallRight():
        API.turnLeft90()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
        

    #só tem seguir em frente
    elif API.wallRight() and API.wallLeft():
        pass

    #depois de cada turn, é necessário seguir em frente, e o código vem logo em seguida para esse moveForward
    #quando não acontecerá nenhum turn, mas somente seguir em frente, o código também vem para esse moveForward com um pass
    if not API.wallFront():
        API.moveForward()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
    else:
    # Se a frente está bloqueada, não avance.
        escolha = random.choice(["D", "E"])
        
        if escolha == "E":
            API.turnLeft90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)
        else:
            API.turnRight90()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
        

    return x, y, orientacao
