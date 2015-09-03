__author__ = 'trinhkhanh'
x = [ i for i in range(1, 101)]
y = []
z = []
for i in x:
    if i%3 == 0:
        y.append(i)
    elif i%5 == 0:
        z.append(i)
print(y)
print()
print(z)


