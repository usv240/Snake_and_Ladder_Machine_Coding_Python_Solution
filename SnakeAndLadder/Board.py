from Player import Player
from snakeAndLadder import snakeAndLadder
import sys

class board:
    maxBoard = 100
    a = snakeAndLadder()
    p = Player()

    #Checks if the player won or not, if won then program exits.
    def isWin(self,turn):
        if self.p.playerName[turn] == self.maxBoard:
            print("Player " + turn + " won the game")
            sys.exit(0)

    #Checks if the player's position is in snakes head, if so then position will be replaced with tail's position
    def snakeBite(self,turn,pos):
        l=list(self.a.snake.keys())
        if pos in l:
            tail=self.a.getTail(pos)
            self.p.setPosition(turn, tail)

    # Checks if the player's position is in ladder's bottom, if so then position will be replaced with ladder's top position
    def ladderBite(self,turn,pos):
        l = list(self.a.ladder.keys())
        if pos in l:
            ladderTop = self.a.getLadderTop(pos)
            self.p.setPosition(turn, ladderTop)
