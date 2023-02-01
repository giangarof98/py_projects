my_list = [5,4,3]

# first approach
for lst in my_list:
    # print(lst)
    x = lambda y: y**2
    # print(x(lst))

# second approach
new_list = list(map(lambda x: x**2, my_list))
print(new_list)


# sorting a tupple
my_list_tupple = [(3, 2), (10, 4), (6, 8), (-4,-3)]
my_list_tupple.sort(key=lambda x: x[1])
print(my_list_tupple)
# print(sorted(my_list_tupple))
