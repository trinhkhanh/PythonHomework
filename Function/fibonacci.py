__author__ = 'trinhkhanh'
def Fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(7))