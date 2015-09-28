__author__ = 'trinhkhanh'
import functools
#  Using lambda function to calculate the sum of odd number in the foo
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(functools.reduce(lambda x, y: x+y,list(filter(lambda x: x % 2 == 1, foo))))
print()

#  Using def function to calculate the sum of odd number in the foo
def add(x, y):
    return x+y
result =[]
for i in foo:
    if i % 2 ==1:
        result.append(i)
print(functools.reduce(add, result))







