class Conversor:
    def __init__(self, convert):
        self.convert = convert

    # Farenheit to Celsius
    def ftoC(self):
        x = self.convert - 32
        return x * .5556
    
    # Farenheit to Kelvin
    def ftoK(self):
        x = self.convert + 459.67
        return x * .5556

    # Celsius to Farenheit
    def ctof(self):
        x = self.convert * 1.8
        return x + 32
    
    # Celsius to Kelvin
    def ctoK(self):
        x = self.convert + 273.15
        return x

    # Kelvin to Farenheit
    def ktoF(self):
        x = self.convert * 1.8
        return x - 459.67

    # Kelvin to Celsius
    def ktoC(self):
        return self.convert - 273.25


    def convertion(self):
        q1 = input('You want to convert from: F, C, K\n')
        global q2 
        q2 = input('You want to convert to: F, C, K\n')

        # Farenheit
        if q1 == 'f' and q2 == 'c':
            return self.ftoC()
        
        if q1 == 'f' and q2 == 'k':
            return self.ftoK()
        
        # Celsius
        if q1 == 'c' and q2 == 'f':
            return self.ctof()
        
        if q1 == 'c' and q2 == 'k':
            return self.ctoK()

        # Kelvin
        if q1 == 'k' and q2 == 'f':
            return self.ktoF()

        if q1 == 'k' and q2 == 'c':
            return self.ktoC()



q3 = input('set the unit to convert\n')

calc = Conversor(int(q3))
res = calc.convertion()
print(f'{res} {q2}')

    
