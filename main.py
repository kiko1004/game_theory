# 2 players
# bank?
# complex logic
# final aim - simulation
from Config import config
from Engine import *
from Player import *

if __name__ == "__main__":

    eng = Engine(
        **config.get_conf(),
        player_1=RandomPlayer,
        player_2=RevengefulPlayer
    )

    eng.run()

