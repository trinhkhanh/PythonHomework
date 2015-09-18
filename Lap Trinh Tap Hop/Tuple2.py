__author__ = 'trinhkhanh'
numList = [9, 3, 2, 5, 6, 8, 11]
list1 = []
list2= []

for i in numList:
    if i <= 5:
        list1.append(i)
    else:
        list2.append(i)

list1.sort()
list2.sort()
Result =(list1, list2)

print('Result =',str(Result))