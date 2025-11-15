import API
import sys
import numpy as np

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def atualizar_inundação():
    # implementar a lógica de inundação na matriz
    pass

def atualizar_parede():
    # implementar a atualização da parede na célula que o robô está
    pass

def main():
    log("Running...")
    paredes = np.zeros(16, 16)
    API.setColor(0, 0, "G")
    API.setText(0, 0, "abc")
    while True:
        if not API.wallLeft():
            API.turnLeft()
        while API.wallFront():
            API.turnRight()
        API.moveForward()

if __name__ == "__main__":
    main()