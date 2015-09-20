__author__ = 'trinhkhanh'
import random
characterList = []
# Goi ra list tu a-z
for x in range(ord('a'), ord('z')+1):
    characterList.append(x)
# Lay ra 5 - 10 ky tu trong list va sap xep theo thu tu
randomList = random.sample(characterList, random.randint(5, 10))
for i in range(0, len(randomList) - 1):
    for j in range(i + 1, len(randomList)):
        if randomList[i] > randomList[j]:
            temp = randomList[i]
            randomList[i] = randomList[j]
            randomList[j] = temp
# In ra man hinh ket qua
resultList = []
for randomList in reversed(randomList):
    randomList = (str(chr(randomList))).upper()
    resultList.append(randomList)
print(resultList)










