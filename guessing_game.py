from random import randint

answer = randint(1,10)

while True:
    try:
        guess = int(input('guess a number 1-10\n'))
        if guess > 0 and answer < 11:
            if guess == answer:
                print('great job!')
                break
        else:
            print('between 1-10...')
    except ValueError:
        print('enter a number, please')
        continue