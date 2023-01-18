import random

class Game:
    def __init__(self):
        # Score start at 0
        self.p1 = 0
        self.p2 = 0
        # 3 options
        self.my_list = ['rock', 'paper', 'scissors']
        # if Draw
        self.draw = 'Draw'

    # start the game
    def start(self):
        # while the player score is not 3 
        while self.p1 < 3 and self.p2 < 3:
            self.move = print('Lets play Rock-Paper-Scissors!\n')
            self.q1 = input('Your move:\n P1:')
            # if the input is not in the list
            while self.q1 not in self.my_list:
                print('Invalid choice, please enter a valid one')
                self.q1 = input('Lets play Rock-Paper-Scissors!\n You go first!\n P1: ')

            # inside the first while loop, it will call the random choice, and initialize the conditions
            # check is one of the players reach the total score
            self.q2 = random.choice(self.my_list)
            self.init()
            self.game_over()

    def game_over(self):
        # game over conditions
        if self.p1 == 3:
            print('you won!')
        elif self.p2 == 3:
            print('I won!')

    def init(self):
        
        # Paper conditionals
        if self.q1 == 'paper' and self.q2 == 'paper':
            print(self.draw)
            print(f'P2: {self.q2}')
        elif self.q1 == 'paper' and self.q2 == 'rock':
            self.p1 += 1
            print(f'P2: {self.q2}\n {self.p1} - {self.p2}')
        elif self.q1 == 'paper' and self.q2 == 'scissors':
            self.p2 += 1
            print(f'P2: {self.q2}\n {self.p1} - {self.p2}')

        # Rock conditionals
        elif self.q1 == 'rock' and self.q2 == 'rock':
            print(self.draw)
            print(f'P2: {self.q2}')
        elif self.q1 == 'rock' and self.q2 == 'paper':
            self.p2 += 1
            print(f'P2: {self.q2}\n {self.p1} - {self.p2}')
        elif self.q1 == 'rock' and self.q2 == 'scissors':
            self.p1 += 1
            print(f'P2: {self.q2}\n {self.p1} - {self.p2}')

            # Scissors Conditionals
        elif self.q1 == 'scissors' and self.q2 == 'scissors':
            print(self.draw)
            print(f'P2: {self.q2}\n {self.p1} - {self.p2}')
        elif self.q1 == 'scissors' and self.q2 == 'rock':
            self.p2 += 1
            print(f'P2: {self.q2}\n {self.p1} - {self.p2}')
        elif self.q1 == 'scissors' and self.q2 == 'paper':
            self.p1 += 1
            print(f'P2: {self.q2}\n {self.p1} - {self.p2}')

# start the game when type in the command line
if __name__ == '__main__':
    start_game = Game()
    start_game.start()
