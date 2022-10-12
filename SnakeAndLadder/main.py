from Player import Player
from Dice import Dice
from Board import board

class startGame():
    p1 = Player()
    b = board()
    d = Dice()

    def start(self):
        n = 1 #Taking n=1 to make it infinite loop
        while n > 0:
            turn = self.d.getTurn()
            dice = self.d.moveDice()

            oldMove = self.p1.position(turn) #To print the old move
            temp = self.p1.position(turn) + dice #To retain the move if the position is >100
            if temp > self.b.maxBoard:  #To check if the new move is >100
                continue
            elif temp <= self.b.maxBoard:  #if Move is <100 then update the position
                self.p1.playerName[turn]=temp

            print(str(turn) + " rolled a " + str(dice) + " and moved from " + str(oldMove) + " to " + str(temp))
            self.b.isWin(turn)
            # Check if the player won or Snake bite or got ladder.
            self.b.snakeBite(turn, self.p1.position(turn))
            self.b.ladderBite(turn, self.p1.position(turn))
            self.b.isWin(turn)


s = startGame()
s.start()

