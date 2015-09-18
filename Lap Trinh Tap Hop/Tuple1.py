__author__ = 'trinhkhanh'
l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']

t = list(zip(l1, l2[::-1]))

print('t = ', str(t))