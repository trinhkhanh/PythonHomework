__author__ = 'trinhkhanh'
import string, random

randomList = []
for number in range (5):
    randomList.append(''.join(random.sample(string.ascii_lowercase,random.randint(5,10))))
print(randomList)

for i in range(0, len(randomList)- 1):
    for j in range(i+1,len(randomList)):
        if randomList[i] > randomList[j]:
            temp = randomList[i]
            randomList[i] = randomList[j]
            randomList[j] = temp

print(randomList)



