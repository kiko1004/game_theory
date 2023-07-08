from Config import config
from Player import *
from SimulationManager import SimulationManager

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

    sim = SimulationManager(players, config)
    sim.run()


