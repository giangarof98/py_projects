# def fibo(number):
#     a = 0
#     b = 1
#     for i in range(number):
#         yield a
#         temp = a
#         a = b
#         b = temp + b

# for x in fibo(10):
#     print(x)

def fibo(number):
    a = 0
    b = 1
    res = []
    for i in range(number):
        res.append(a)
        temp = a
        a = b
        b = temp + b
    return res

print(fibo(1000))

