__author__ = 'trinhkhanh'
class UseBMIClass:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    def BMI(self):
        return (self.weight * 0.45359237)/(self.height*0.0254)**2

    def checkBMI(self):
        if self.BMI() >= 18.5:
            if self.BMI() < 25:
                print('The BMI for {0} is {1:.2f} Normal'.format(self.name,self.BMI()))
            else:
                if self.BMI() == 25 and self.BMI() < 30:
                    print('The BMI for {0} is {1:.2f} overweight'.format(self.name,self.BMI()))
                else:
                    print('The BMI for {0} is {1:.2f} obese'.format(self.name,self.BMI()))
        else:
            print('The BMI for {0} is {1:.2f} underweight'.format(self.name,self.BMI()))


newBMI1 = UseBMIClass('Kim Yang', 18, 145, 70)
newBMI2 = UseBMIClass('Susan King',18, 215, 70)

newBMI1.checkBMI()
newBMI2.checkBMI()
