__author__ = 'trinhkhanh'

fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)

print(fib(12))