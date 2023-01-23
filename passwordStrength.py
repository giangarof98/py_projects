class Checker:
    def __init__(self):
        self.x = input('type your new password\n')
        

    def psw(self):
        self.n = str([0,1,2,3,4,5,6,7,8,9])
        self.s = ['!','@','#','$','&','+','-','*','/','^','%',',','.',';',':','{','}','[',']']
        self.upper = sum(1 for u in self.x if u.isupper())
        self.lower = sum(1 for l in self.x if l.islower())
        self.numbers = [num for num in self.n if str(num) in self.x]
        self.simbol = [sim for sim in self.s if str(sim) in self.x]

        self.check()

    def check(self):
        if len(self.x) < 8:
            print('must be at least 8 characters')
        elif len(self.numbers) < 2:
            print('must contain two number')
        elif len(self.simbol) < 2:
            print('must contain two symbols')
        elif self.upper < 1:
            print('must contain a uppercase letter')
        elif self.lower < 1:
            print('must contain a lowercase letter')
        else:
            print('password meet all the requirements')

if __name__ == '__main__':
    start = Checker()
    start.psw()