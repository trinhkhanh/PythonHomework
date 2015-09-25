__author__ = 'trinhkhanh'

import math

def heSo(a, b, c):
    if a!= 0:
        delta = b**2 - 4*a*c
        if delta > 0:
            return (-b - math.sqrt(delta))/(2*a), (-b + math.sqrt(delta))/(2*a)
        elif delta < 0:
            return ('Phuong trinh vo nghiem')
        else:
            return -b/(2*a)
    else:
        if b != 0:
            return -c/b
        else:
            return None


print(heSo(1, -6, 4))




