import random
import string

# Really very basic encoded password
class Encoded:
    def __init__(self):
        # input ask for password
        self.psw = input('type your password...\n')

        # variables to encode the password

        # sign
        self.sign = ['+','-','%','*','/','$','#']

        # number 1
        self.n1 = str(random.randint(1,99))
        # number 2
        self.n2 = str(random.randint(1,99))

        # random lowecase 1
        self.l1 = random.choice(string.ascii_lowercase)
        # random lowercase 2
        self.l2 = random.choice(string.ascii_lowercase)

        # random upper case 1
        self.u1 = random.choice(string.ascii_uppercase)
        # random upper case 2
        self.u2 = random.choice(string.ascii_uppercase)

        # random sign 1
        self.r2 = random.choice(self.sign)
        # random sign 2
        self.r1 = random.choice(self.sign)

        self.encoded = self.n1 + self.n2 + self.l1 + self.l2 + self.u1 + self.u2 + self.r1 + self.r1
        self.encoded_list = list(self.encoded)
        random.shuffle(self.encoded_list)
        self.shuffled_e = ''.join(self.encoded_list)

    def generate(self):
        # Logic
        if len(self.psw) != 8:
            print('length characters must be at least 8')
        else:
            e = input(f'Your password is: {self.psw}\n Do you want to encode it?\n')
            if e == 'no':
                print("We do recommend to encode it...\n We'll encode it automatically")
                print(self.shuffled_e)
            elif e == 'yes':
                print(self.shuffled_e)

if __name__ == '__main__':
    gen = Encoded()
    gen.generate()

# chr() transform an integer to its unicode
# ord() transform a letter to its unicode integer


