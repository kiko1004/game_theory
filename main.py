# 2 players
# bank?
# complex logic
# final aim - simulation
from Config import config
from Engine import *
from Player import *

if __name__ == "__main__":

    players = {
        "Socializer": Socializer,
        "CooperativePlayer": CooperativePlayer,
        "RevengefulPlayer": RevengefulPlayer,
        "AggressivePlayer": AggressivePlayer,
        "CopyPlayer": CopyPlayer,
        "Killer": Killer,
        "RandomPlayer": RandomPlayer
    }
    

