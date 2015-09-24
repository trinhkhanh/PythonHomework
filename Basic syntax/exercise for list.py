__author__ = 'trinhkhanh'

fruits = ['Cam', 'Tao', 'Dua', 'Dua', 'Cam', 'Oi', 'Cam', 'Tao', 'Chanh', 'Le', 'Nho']

uniqueList = []

for fruit in fruits:
    if uniqueList.count(fruit) == 0:
        uniqueList.append(fruit)

print(uniqueList)


