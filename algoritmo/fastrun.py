from matriz_paredes import atualizar_paredes 
from matriz_inundacao import atualizar_inundacao
import API
#função checa ao redor do micromouse, todas as 4 direções para checar onde tem paredes
def vizinhos_livres(x, y, paredes):
    livres = []

    #checa se a paredes na direita (1)
    if (paredes[y, x] & 1) == 0:
        livres.append((y, x+1))

    #checa se a paredes a  esquerda (2)
    if (paredes[y, x] & 2) == 0:
        livres.append((y, x-1))

    #checa se a pardes em baixo (4)
    if (paredes[y, x] & 4) == 0:
        livres.append((y+1, x))

    #checa se a paredes em cima (8)
    if (paredes[y, x] & 8) == 0:
        livres.append((y-1, x))
    API.log(livres)
    #retorna uma lista das celúlas vizinhas livres
    return livres

def escolher_melhor_vizinho(x, y, matriz, paredes):
    #usa a lista criada na função vizinhos_livres
    vizinhos = vizinhos_livres(x, y, paredes)
    #cria as variaveis
    melhor = None 
    menor_valor = 999
    #loop que checa entre os livres qual tem menor valor na matriz de inundação
    for (vy, vx) in vizinhos:
        if matriz[vy, vx] < menor_valor:
            menor_valor = matriz[vy, vx]
            melhor = (vy, vx)
    API.log(menor_valor)
    return melhor 

#função que converte a coordenada achada em um movimento, baseada na orientação que ele se encontava antes 
def converter_movimento(x, y, orientacao, vx, vy):
    melhor = 0
    cima = (y-1, x)
    baixo = (y+1, x)
    esquerda = (y, x-1)
    direita = (y, x+1)

    N = 0
    L = 1
    S = 2
    O = 3

    # norte = y-1
    if (vy, vx) == cima:
        melhor = N
    # sul = y+1
    elif (vy, vx) == baixo:
        melhor = S
    # leste = x+1
    elif (vy, vx) == direita:
        melhor = L
    # oeste = x-1
    elif (vy, vx) == esquerda:
        melhor = O

    melhor = (melhor-orientacao) %4
    # diferença entre orientação atual e direção desejada


    if melhor == N:
        return "F"   # frente
    if melhor == L:
        return "D"   # virar direita
    if melhor == O:
        API.log("Esq")
        return "E"   # virar esquerda
    if melhor == S:
        return "B"   # virar 180°
    
def melhor_caminho(x, y, orientacao, matriz_inundacao, matriz_paredes):
    #escolhe o vizinho com menor valor na matriz de inundação
    caminho = escolher_melhor_vizinho(x, y, matriz_inundacao, matriz_paredes)

    vy, vx = caminho 
    
    #converte o caminho em comando
    movimento = converter_movimento(x, y, orientacao, vx, vy)

    #executa os comandos 
    if movimento == "F":
        pass

    elif movimento == "D":
        API.turnRight()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)

    elif movimento == "E":
        API.turnLeft()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "E", orientacao)

    elif movimento == "B":
        API.turnRight() 
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
        API.turnRight()
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)


    API.moveForward()
    #atualiza as coordenadas depois de cada movimento 
    x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)
    API.log(x)
    API.log(y)
    return x, y, orientacao
