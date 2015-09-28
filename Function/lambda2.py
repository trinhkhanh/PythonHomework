__author__ = 'trinhkhanh'

import functools

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
result =[i for i in foo if i%2 == 1]

#  Using lambda function to calculate the sum of odd number in the foo
print(functools.reduce(lambda x, y: x+y, result))
print()

#  Using def function to calculate the sum of odd number in the foo
def add(x, y):
    return x+y
print(functools.reduce(add, result))







