from Player import Player
import random

class Dice:
    diceMove = [1, 2, 3, 4, 5, 6]
    p = Player()
    flag = 0

    def moveDice(self):
        a=int(random.choice(self.diceMove))
        return a

#Currently, turn is hardcoded for 2 players, can be changed.
    def getTurn(self):
        l=list(self.p.playerName.keys())

        if self.flag==0:
            self.flag=1
            return l[0]

        elif self.flag==1:
            self.flag=0
            return l[1]