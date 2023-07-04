class Player:
    def __init__(self, spoints: int, pwn: int, pwp: int, plp: int, pln: int):
        self.pln = pln
        self.plp = plp
        self.pwp = pwp
        self.pwn = pwn
        self.decision = None
        self.points = spoints

    def make_decision(self, positive: bool):
        if positive:
            self.decision = "positive"
        else:
            self.decision = "negative"

    def outcome(self, positive: bool, win: bool):
        if positive and win:
            self.points += self.pwp
        elif positive and not win:
            self.points -= self.plp
        elif not positive and win:
            self.points += self.pwn
        elif not positive and not win:
            self.points -= self.pln

class Socializer(Player):
    def make_decision(self, **kwargs):
        super().make_decision(True)


