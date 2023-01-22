# Jackpot game
import random

class Jackpot:
    def __init__(self):
        self.money = 50

    def start(self):
        print('JackPot game!')
        input('Press enter to start!')
        self.game()

    def game(self):
        # start with a default of 10$
        print(f'Your total of money is: {self.money}$')

        # if there is money to play
        while self.money > 0:
            # Generate random numbers
            self.x1 = random.randint(1,9)
            self.x2 = random.randint(1,9)
            self.x3 = random.randint(1,9)
            qty = int(input('Set a qty to play:\n'))

            # if the qty is more than the remaining
            if qty > self.money:
                print('You dont have that QTY of money to play !')
                continue
            # start the logic
            self.logic(qty)

    def logic(self, qty):
        # keep track of the remaining 
        self.money -= qty
        # if all the numbers are equals
        if self.x1 == self.x2 == self.x3:
            self.money += qty * 50
            print('Good job!')
        # if 0, automaticaly leave the game
        elif self.money == 0:
            print('out of money!')
            exit()
        # by default, keep playing until reach 0
        else:
            print(f'Remaining: {self.money}$')

        print(self.x1, self.x2, self.x3)
    
if __name__ == '__main__':
    start = Jackpot()
    start.start()