import time
import random

randomNumbers = []

for i in range(1000000):
    randomNumbers.append(random.randint(1, 10))

myList = []
st = time.time()
for n in randomNumbers:
    if n not in myList:
        myList.append(n)
print(f"list -> set: {time.time() - st}")


st = time.time()
mySet = set(randomNumbers)
print(f"set(): {time.time() - st}")


st = time.time()
myDict = {}
for n in randomNumbers:
    if n not in myDict:
        myDict[n] = 1
    else:
        myDict[n] = myDict[n] + 1
print(f"list -> dict: {time.time() - st}")

"""
1 ~ 10 범위의 백만개의 수
list -> set: 0.07041501998901367
set(): 0.004754304885864258
list -> dict: 0.11228704452514648
"""
