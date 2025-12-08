from matriz_paredes import atualizar_paredes 
from matriz_inundacao import atualizar_inundacao
import API
#função checa ao redor do micromouse, todas as 4 direções para checar onde tem paredes
def vizinhos_livres(x, y, paredes):
    livres = []

    #checa se ha paredes na direita (1)
    if (paredes[y, x] & 1) == 0:
        livres.append((x+1, y))

    #checa se ha paredes a  esquerda (2)
    if (paredes[y, x] & 2) == 0:
        livres.append((x-1, y))

    #checa se ha pardes em baixo (4)
    if (paredes[y, x] & 4) == 0:
        livres.append((x, y+1))

    #checa se ha paredes em cima (8)
    if (paredes[y, x] & 8) == 0:
        livres.append((x, y-1))
    
    #retorna uma lista das celúlas vizinhas livres
    return livres

def escolher_melhor_vizinho(x, y, matriz, paredes):
    #usa a lista criada na função vizinhos_livres
    vizinhos = vizinhos_livres(x, y, paredes)
    #cria as variaveis
    melhor = None 
    menor_valor = 999
    #loop que checa entre os livres qual tem menor valor na matriz de inundação
    for (vx, vy) in vizinhos:
        if matriz[vy, vx] < menor_valor:
            menor_valor = matriz[vy, vx]
            melhor = (vy, vx)
    return melhor 
#função que converte a coordenada achada em um movimento, baseada na orientação que ele se encontava antes 
def converter_movimento(x, y, orientacao, vx, vy):
    N = 0
    L = 1
    S = 2
    O = 3
    # norte = y-1
    if vy == y-1:
        melhor = N
    # sul = y+1
    elif vy == y+1:
        melhor = S
    # leste = x+1
    elif vx == x+1:
        melhor = L
    # oeste = x-1
    else:
        melhor = O

    # diferença entre orientação atual e direção desejada
    dif = (melhor - orientacao) % 4

    if dif == 0:
        return "F"   # frente
    if dif == 1:
        return "D"   # virar direita
    if dif == 3:
        return "E"   # virar esquerda
    if dif == 2:
        return "B"   # virar 180°
    
def melhor_caminho_para_centro(x, y, orientacao, matriz_inundacao, matriz_paredes):
    while True:
        #atualiza as paredes da célula atual
        matriz_paredes = atualizar_paredes(matriz_paredes, x, y, orientacao)
        #atualiza a matriz de inundação
        matriz_inundacao = atualizar_inundacao(matriz_inundacao, matriz_paredes)
        #escolhe o vizinho com menor valor na matriz de inundação
        caminho = escolher_melhor_vizinho(x, y, matriz_inundacao, matriz_paredes)

        vx, vy = caminho 
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
            API.turnRight()
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)
            x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "D", orientacao)


        API.moveForward()
        #atualiza as coordenadas depois de cada movimento 
        x, y, orientacao = API.atualizar_coordenada_orientacao(x, y, "F", orientacao)

        #para quando chega ao centro 
        if (x, y) in [(7,7), (7,8), (8,7), (8,8)]:
            break  
