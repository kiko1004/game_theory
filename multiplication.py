a = [1, 2, 3, 4]
# 1*2 + 1*3 + 1*4 + 2*3 + 2*4 + 3*4 = 35

res = 0

for _ in range(len(a)):
    x = a.pop(0)
    res += sum([j*x for j in a])

print(res)