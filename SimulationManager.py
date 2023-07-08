from Engine import *
from Config import Config, config

from Player import *



class SimulationManager:
    def __init__(self, players: dict, config: Config):
        self.players = players
        self.config = config
        self.create_ranklist()

    def create_ranklist(self):
        self.ranklist = {}
        for player in players.keys():
            self.ranklist[player] = 0

    def run_simulation(self, player_1, player_2):
        eng = Engine(
            # added dictionary unpacking
            **self.config.get_conf(),
            player_1=player_1,
            player_2=player_2
        )

        return eng.run()

    def run(self):
        p = self.players.keys()
        for _ in range(len(p)):
            p1 = p.pop(0)
            for p2 in p:
                print(p1, "plays with", p2)
                res_p1, res_p2 = self.run_simulation(self.players[p1], self.players[p2])
                print(p1, "gained" if res_p1 >0 else "lost", res_p1, "points")
                print(p2, "gained" if res_p2 >0 else "lost", res_p2, "points")
                self.ranklist[p1] += res_p1
                self.ranklist[p2] += res_p2
                print(p1, "now has", self.ranklist[p1])
                print(p2, "now has", self.ranklist[p2])

        for player in self.ranklist.keys():
            print(player, "-", self.ranklist[player])


