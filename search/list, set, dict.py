import random
import time


myList = [i for i in range(1, 1000001)]
mySet = set(myList)
myDict = {}
for i in range(1, 1000001):
    myDict[i] = 1

print("find first")
# 리스트 첫 번째 값 찾기
st = time.time()
if 1 in myList:
    print(time.time() - st)
"""
6.9141387939453125e-06
"""

# 셋 가장 먼저 삽입한 값 찾기
st = time.time()
if 1 in mySet:
    print(time.time() - st)
"""
6.9141387939453125e-06
"""


# 딕셔너리 가장 먼저 삽입한 값 찾기
st = time.time()
if 1 in myDict:
    print(time.time() - st)
"""
7.152557373046875e-07
"""

print("find last")
# 리스트 마지막 값 찾기
st = time.time()
if 1000000 in myList:
    print(time.time() - st)
"""
0.006685972213745117
"""

# 셋 가장 마지막에 삽입한 값 찾기
st = time.time()
if 1000000 in mySet:
    print(time.time() - st)
"""
1.1920928955078125e-06
"""

# 딕셔너리 가장 마지막에 삽입한 값 찾기
st = time.time()
if 1000000 in myDict:
    print(time.time() - st)
"""
9.5367431640625e-07
"""


print("find random")
randomNumber = random.randint(1, 1000001)


# 리스트 랜덤 값 찾기
st = time.time()
if randomNumber in myList:
    print(time.time() - st)
"""
0.0005042552947998047
"""

# 셋 랜덤 값 찾기
st = time.time()
if randomNumber in mySet:
    print(time.time() - st)
"""
9.5367431640625e-07
"""

# 딕셔너리 랜덤 값 찾기
st = time.time()
if randomNumber in myDict:
    print(time.time() - st)
"""
3.0994415283203125e-06
"""


"""
결론: 'in' 키워드로 값 찾기 속도

set == dict >> list
"""