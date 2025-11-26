import API as API
import sys
from matriz_inundacao import matriz_inundacao
from matriz_paredes import atualizar_paredes
import numpy as np


def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()


def main():
    log("Running...")
    parede = np.zeros((16, 16), dtype=int)
    inundacao = np.zeros((16, 16), dtype=int)
    x, y = 0, 0
    API.setColor(0, 0, "G")
    API.setText(0, 0, "abc")
    while True:
        if not API.wallLeft():
            API.turnLeft()
        while API.wallFront():
            API.turnRight()
        API.moveForward()
        inundacao = matriz_inundacao(inundacao)
        paredes = atualizar_paredes(parede, x, y)
        print(paredes)

if __name__ == "__main__":
    main()