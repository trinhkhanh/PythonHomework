__author__ = 'trinhkhanh'
import math
class Circle:
    def __init__(self, newRadius):
        self.newRadius = newRadius

    def getArea(self):
        print(math.pi*self.newRadius**2)

    def getPerimeter(self):
        print(2*self.newRadius*math.pi)

number = Circle(3)

number.getArea()
number.getPerimeter()