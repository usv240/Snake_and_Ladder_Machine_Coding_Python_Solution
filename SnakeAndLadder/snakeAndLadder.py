class snakeAndLadder:

    #Currently, Snake and ladder vales are hardcoded, input can be taken from user
    #While taking the input from the user, the collission should be handeled.
    #There cannot be a snake at 100th position

    snake = {33: 6, 41: 20, 49: 9, 56: 53, 62: 5, 87: 16, 93: 73, 95: 75, 98: 64} #key is head of snake and value is the tail.
    ladder={2:37,10:32,27:46,51:68,61:79,65:84,71:91,81:100} #key is the bottom of ladder and value is the top of ladder.

    #Returns the tail value
    def getTail(self,key):
        print("Snake bite at "+ str(key) + " and down to "+ str(self.snake.get(key)))
        return self.snake.get(key)

    #Return the Top of ladder value
    def getLadderTop(self,key):
        print("Ladder at "+ str(key) + " and up to "+ str(self.ladder.get(key)))
        return self.ladder.get(key)
