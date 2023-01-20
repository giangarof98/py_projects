import time

class Counter:
    def __init__(self, t):
        self.t = t
    # divmod()
        # takes two numbers and returns a pair of numbers consisting of their quotient and remainder. 

    def count(self):
        while self.t:
            # takes the remainder for the seconds
            mins, secs = divmod(self.t, 60)
            # takes the remainder for the minuts
            hours, mins = divmod(mins, 60)
            # takes the remainder for the hours
            days, hours = divmod(hours, 24)

            # format
            timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            # overrite each second
            print(timeformat, end='\r')
            time.sleep(1)
            self.t -= 1

        # when it gets done...
        print('completed')
t = 7200
if __name__ == '__main__':
    c = Counter(t)
    c.count()


# 10 -> 10 secs

# 120 -> 2 min

# 3600 -> 1h

# 7200 -> 2h


