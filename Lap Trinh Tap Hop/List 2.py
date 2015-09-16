__author__ = 'trinhkhanh'
fruits = ['Juice', 'Tomato', 'Potatoes', 'Banana', 'Tomato', 'Banana']
countFruits = []
uniqueList = []

for fruit in fruits:
    countFruits.append(fruits.count(fruit))
    if uniqueList.count(fruit) == 0:
        uniqueList.append(fruit)

print(list(zip(uniqueList, countFruits)))

