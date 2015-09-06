__author__ = 'trinhkhanh'

fruits = ['Cam', 'Tao', 'Dua','Chanh', 'Dua', 'Cam', 'Oi', 'Cam', 'Tao', 'Chanh', 'Le', 'Nho']

uniqueList = []

for j in fruits:
    l = fruits.count(j)
    if l == 1:
        uniqueList.append(j)
print(uniqueList)


