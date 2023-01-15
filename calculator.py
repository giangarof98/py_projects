class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    def subs(self):
        return self.x - self.y
    def div(self):
        return self.x / self.y
    def mult(self):
        return self.x * self.y
    def expo(self):
        return self.x ** self.y

    def calculation(self):
        q = input('set the operation: add, subs, div, mult, expo')

        if q == 'add':
            print('You choose: add')
            return self.add()
        elif q == 'subs':
            print('You choose: substration')
            return self.subs()
        elif q == 'mult':
            print('You choose: mult')
            return self.mult()
        elif q == 'expo':
            print('You choose: expo')
            return self.expo()
        elif q == 'div':
            print('You choose: div')
            return self.div()

first = input('set the first number')
second = input('set the second number')
calc = Calculator(int(first),int(second))
res = calc.calculation()
print(res)