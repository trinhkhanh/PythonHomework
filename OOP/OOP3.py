__author__ = 'trinhkhanh'
class BMI:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    def getBMI(self):
        return (self.weight * 0.45359237)/(self.height*0.0254)**2

    def getstatus(self):
        if self.getBMI() >= 18.5:
            if self.getBMI() < 25:
                print('{:.2f} Normal'.format(self.getBMI()))
            else:
                if self.getBMI() == 25 and self.getBMI() < 30:
                    print('{:.2f} overweight'.format(self.getBMI()))
                else:
                    print('{:.2f} obese'.format(self.getBMI()))
        else:
            print('{:.2f} underweight'.format(self.getBMI()))

class UseBMIClass(BMI):
    def display(self):
        print('The BMI for ', self.name, 'is', self.getBMI(), ' ', self.getstatus())


bmi1 = ('Kim Yang', 18, 145, 70)
bmi2 = ('Susan King', 18, 215, 70)

bmi1.display()





