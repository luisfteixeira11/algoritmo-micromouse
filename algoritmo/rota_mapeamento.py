import collections
import API
from typing import Tuple, Optional


def rota_mapeamento(x: int, y: int, matriz_visitado, orientacao: int, paredes) -> Tuple[Optional[str], Tuple[int, int]]:
    """
    Planejador simplificado para mapeamento do labirinto.

    - Faz BFS (largura) na grade para encontrar a célula não-visitada
      mais próxima (visitado == -1).
    - Retorna um comando relativo para o primeiro passo: "F","D","E","B",
      ou `None` se não houver célula não visitada.

    Parâmetros:
    - x, y: posição atual (x=coluna, y=linha)
    - matriz_visitado: numpy array 2D com -1 = não visitado
    - orientacao: 0=N,1=E,2=S,3=W
    - paredes: matriz 2D com bits de parede por célula, -1 = desconhecido

    Retorno: (comando, (nova_linha, nova_coluna)) — note que a posição
    retornada é em (y,x) para compatibilidade com a base de código.
    """

    altura, largura = paredes.shape

    # nomes locais mais descritivos
    linha_atual = y
    coluna_atual = x
    visitado = matriz_visitado

    # DIRECTIONS: (dLinha, dColuna, bit) ordem absoluta N,E,S,W (0..3)
    DIRECTIONS = [(-1, 0, 3), (0, 1, 0), (1, 0, 2), (0, -1, 1)]

    # ordem de expansão relativa: preferir frente, direita, esquerda, trás
    ordem_relativa = [orientacao, (orientacao + 1) % 4, (orientacao + 3) % 4, (orientacao + 2) % 4]

    fila = collections.deque()
    fila.append((linha_atual, coluna_atual))
    came_from = {(linha_atual, coluna_atual): None}
    alvo = None

    while fila:
        l, c = fila.popleft()
        # se não visitado (e não a célula atual), escolhe como alvo
        if visitado[l, c] == -1 and not (l == linha_atual and c == coluna_atual):
            alvo = (l, c)
            break

        # expandir em ordem relativa (frente, direita, esquerda, trás)
        for idx in ordem_relativa:
            dl, dc, bit = DIRECTIONS[idx]
            nl, nc = l + dl, c + dc
            if not (0 <= nl < altura and 0 <= nc < largura):
                continue

            # se parede conhecida bloqueia o movimento, pula
            cel = paredes[l, c]
            if cel != -1 and ((cel >> bit) & 1) == 1:
                continue

            if (nl, nc) in came_from:
                continue

            came_from[(nl, nc)] = (l, c)
            fila.append((nl, nc))

    if alvo is None:
        return None, (x, y)

    # reconstrói caminho e pega o primeiro passo
    caminho = []
    cur = alvo
    while cur is not None:
        caminho.append(cur)
        cur = came_from[cur]
    caminho.reverse()

    if len(caminho) < 2:
        return None, (x, y)

    prox_linha, prox_coluna = caminho[1]
    dlinha, dcoluna = prox_linha - linha_atual, prox_coluna - coluna_atual

    # mapa deslocamento -> direção absoluta
    if dlinha == -1 and dcoluna == 0:
        direcao_absoluta = 0
    elif dlinha == 0 and dcoluna == 1:
        direcao_absoluta = 1
    elif dlinha == 1 and dcoluna == 0:
        direcao_absoluta = 2
    elif dlinha == 0 and dcoluna == -1:
        direcao_absoluta = 3
    else:
        return None, (x, y)

    diff = (direcao_absoluta - orientacao) % 4
    if diff == 0:
        comando = "F"
    elif diff == 1:
        comando = "D"
    elif diff == 3:
        comando = "E"
    else:
        comando = "B"

    return comando, (prox_linha, prox_coluna)
