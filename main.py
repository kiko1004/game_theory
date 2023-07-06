# 2 players
# bank?
# complex logic
# final aim - simulation

from Engine import *
from Player import *

if __name__ == "__main__":

    eng = Engine(
        rounds=100,
        spoints=0,
        pwn=4,
        pwp=2,
        plp=4,
        pln=2,
        player_1=RandomPlayer,
        player_2=RevengefulPlayer
    )

    eng.run()

