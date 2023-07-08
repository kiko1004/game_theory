from Player import Player

class Engine:
    def __init__(
            self,
            rounds: int,
            spoints: int,
            pwn: int,
            pwp: int,
            plp: int,
            pln: int,
            player_1: Player,
            player_2: Player
    ):
        '''
        :param spoints: players starting points
        :param pwn: if the player won with a negative decision
        :param pwp: if the player won with a positive decision
        :param plp: if the player lost with a positive decision
        :param pln: if the player lost with a negative decision
        '''
        self.player_2_base = player_2
        self.player_1_base = player_1
        self.pln = pln
        self.plp = plp
        self.pwp = pwp
        self.pwn = pwn
        self.rounds = rounds
        self.spoints = spoints
        self.previous_decisions = [True, True]
        self.initialize_players()

    def initialize_players(self):

        self.player_1 = self.player_1_base.create_from_engine(
            spoints=self.spoints,
            pln=self.pln,
            plp=self.plp,
            pwp=self.pwp,
            pwn=self.pwn
        )

        self.player_2 = self.player_2_base.create_from_engine(
            spoints=self.spoints,
            pln=self.pln,
            plp=self.plp,
            pwp=self.pwp,
            pwn=self.pwn
        )

    def decision_stage(self):
        self.player_1.make_decision(previous_decision = self.previous_decisions[1])
        self.player_2.make_decision(previous_decision = self.previous_decisions[0])

    def calculation(self):
        if self.player_1.positive and self.player_2.positive:
            self.player_1.outcome(win=True)
            self.player_2.outcome(win=True)
        elif not self.player_1.positive and self.player_2.positive:
            self.player_1.outcome(win=True)
            self.player_2.outcome(win=False)
        elif self.player_1.positive and not self.player_2.positive:
            self.player_1.outcome(win=False)
            self.player_2.outcome(win=True)
        elif not self.player_1.positive and not self.player_2.positive:
            self.player_1.outcome(win=False)
            self.player_2.outcome(win=False)

    def run(self):
        for round in range(1, self.rounds + 1):
            self.decision_stage()
            self.calculation()
            self.previous_decisions = [self.player_1.positive, self.player_2.positive]

        # print(f"{self.player_1.name} has total points of {self.player_1.points}")
        # print(f"{self.player_2.name} has total points of {self.player_2.points}")

        return self.player_1.points, self.player_2.points






