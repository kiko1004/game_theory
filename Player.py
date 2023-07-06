from pick import pick

import random


class Player:
    def __init__(self, spoints: int, pwn: int, pwp: int, plp: int, pln: int):
        self.pln = pln
        self.plp = plp
        self.pwp = pwp
        self.pwn = pwn
        self.points = spoints
        self.name = self.__class__.__name__

    @classmethod
    def create_from_engine(cls, spoints: int, pwn: int, pwp: int, plp: int, pln: int):
        return cls(spoints, pwn, pwp, plp, pln)

    def make_decision(self, positive: bool):
        self.positive = positive

    def outcome(self, win: bool):
        positive = self.positive
        if positive and win:
            print(f"{self.name} wins with a positive decision!")
            self.points += self.pwp
        elif positive and not win:
            print(f"{self.name} loses with a positive decision!")
            self.points -= self.plp
        elif not positive and win:
            print(f"{self.name} wins with a negative decision!")
            self.points += self.pwn
        elif not positive and not win:
            print(f"{self.name} loses with a negative decision!")
            self.points -= self.pln


class Socializer(Player):
    def make_decision(self, **kwargs):
        super().make_decision(True)


class CooperativePlayer(Player):
    def make_decision(self, **kwargs):
        choice = random.choices(population=[True, False], weights=[66, 33])[0]
        super().make_decision(choice)

class RevengefulPlayer(Player):
    def make_decision(self, **kwargs):
        try:
            self.counter
        except:
            self.counter = 0

        if not kwargs["previous_decision"]:
            self.counter += 1
        elif self.counter > 0:
            self.counter -= 1

        if self.counter > 0:
            super().make_decision(False)
        else:
            super().make_decision(True)


class AggressivePlayer(Player):
    def make_decision(self, **kwargs):
        choice = random.choices(population=[True, False], weights=[33, 66])[0]
        super().make_decision(choice)


class CopyPlayer(Player):
    def make_decision(self, **kwargs):
        previous_decision = kwargs['previous_decision']
        if previous_decision:
            super().make_decision(True)
        else:
            super().make_decision(False)


class Killer(Player):
    def make_decision(self, **kwargs):
        super().make_decision(False)


class CustomPlayer(Player):
    def make_decision(self, **kwargs):
        dec = bool(int(input("Enter 1 for a positive decision or 0 for a negative one: ")))
        super().make_decision(dec)


class RandomPlayer(Player):
    def make_decision(self, **kwargs):
        positive = random.choice([True, False])
        super().make_decision(positive)
