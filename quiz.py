# Quiz Game
class Quiz:
    def __init__(self):
        self.q = None
        self.total = []

    # 5 question, if correct, it adds 1 point to the total list
    def q1(self):
        self.q = int(input('2+2 equals to ?\n'))
        res = 4
        if self.q == res:
            self.total.append(1)
        self.q2()

    def q2(self):
        self.q = int(input('5+5 equals to ?\n'))
        res = 10
        if self.q == res:
            self.total.append(1)
        self.q3()

    def q3(self):
        self.q = int(input('-5-3 equals to ?\n'))
        res = -8
        if self.q == res:
            self.total.append(1)
        self.q4()

    def q4(self):
        self.q = int(input('-5+1 equals to ?\n'))
        res = -4
        if self.q == res:
            self.total.append(1)
        self.q5()
    
    # after question five, game over
    def q5(self):
        self.q = int(input('-5-5 equals to ?\n'))
        res = -10
        if self.q == res:
            self.total.append(1)
        self.game_over()

    def start(self):
        self.q1()

    # when its game over, if score equals to 5, exit()
    # if is not equals to 5, promt a question to restart. If yes, start()
    def game_over(self):
        score = sum(self.total)
    
        if score == 5:
            print('Well played! Thanks for play.')
            exit()
        else:
            i = input(f'You scored {score}/5\n Try again for a better match?\n Type yes or no\n')
            if i == 'yes':
                self.total = []
                self.start()
            else:
                print('thanks for play!')

# if call the module, start the came
# __name__ is a built-in method
if __name__ == '__main__':
    start_quiz = Quiz()
    start_quiz.start()


