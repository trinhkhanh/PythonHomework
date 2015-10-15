__author__ = 'trinhkhanh'
class BMI:

    def __init__(self, name, age, weight, height):
        self.name = str(name)
        self.age = int(age)
        self.weight = weight
        self.height = height
    def getBMI(self):
        return (self.weight * 0.45359237)/(self.height*0.0254)**2

    def getStatus(self):
        if self.getBMI() >= 18.5:
            if self.getBMI() < 25:
                return ('{:.2f} Normal'.format(self.getBMI()))
            else:
                if self.getBMI() == 25 and self.getBMI() < 30:
                    return ('{:.2f} Overweight'.format(self.getBMI()))
                else:
                    return ('{:.2f} Obese'.format(self.getBMI()))
        else:
            print('{:.2f} Underweight'.format(self.getBMI()))

class UseBMIClass(BMI):

    def __init__(self, name, age, weight, height):
        BMI.__init__(self, name, age, weight, height)

    def getUseBMIClass(self):
        print ('The BMI for' , self.name, 'is', self.getStatus())


bmi1 = UseBMIClass('Kim Yang', 18, 145, 70)
bmi2 = UseBMIClass('Susan King', 20, 215, 70)

bmi1.getUseBMIClass()
bmi2.getUseBMIClass()





