lst = ['x','x','j','f','a','d','q','x','f']
dup = [x for x in lst if lst.count(x) > 1]
dup = set(dup)
# for v in lst:
#     if lst.count(v) > 1:
#         if v not in dup:
#             dup.append(v)

print(dup)

