__author__ = 'trinhkhanh'
class UseBMIClass:

    def __int__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    def bMI(self):
        self.BMI = self.weight/self.height**2

    def checkBMI(self):
        if self.BMI >= 18.5:
            if self.BMI < 25:
                print('The BMI for ', str(self.name),'is', self.BMI, 'normal')
            else:
                if self.BMI == 25 and self.BMI < 30:
                    print('The BMI for ', str(self.name),'is', self.BMI, 'overweight')
                else:
                    print('The BMI for ', str(self.name),'is', self.BMI, 'obese')
        else:
            print('The BMI for ', str(self.name),'is', self.BMI, 'underweight')


new1BMI = UseBMIClass('Kim Yang', 18, 145, 70)

new1BMI.checkBMI()
