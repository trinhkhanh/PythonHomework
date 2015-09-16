__author__ = 'trinhkhanh'
x = [9, 2, 3, 2, 1, 2]
y = [4, 5, 6, 7, 12, 15]
zipped = list()

for x, y in zip(x, y):
    if (x+y) <= 10:
        zipped.append([x,y])
print (zipped)
