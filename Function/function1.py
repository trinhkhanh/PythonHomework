__author__ = 'trinhkhanh'
def Fibonaci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonaci(n-1) + Fibonaci(n-2)

print(Fibonaci(7))