__author__ = 'trinhkhanh'
x = [ i for i in range(1, 101)]
y =[]
for i in x:
    if i%3 == 0:

        print([i], ' ', end='')

print()

for i in x:
    if i%5 == 0:
        print([i], ' ', end='')
