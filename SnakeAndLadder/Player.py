
class Player:
    #Currently, only 2 players are hardcoded. Can be taken input from user.
    playerName = {"A": 0, "B": 0}

    def position(self,key):
        return self.playerName.get(key)

    def setPosition(self,key,pos):
        t=pos
        self.playerName[key]=pos

        if self.playerName.get(key)>100:
            self.playerName[key] =t
