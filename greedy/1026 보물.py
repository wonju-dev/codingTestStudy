n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def getMinIndex(a):
    index = 0
    for i in range(len(a)):
        if a[i] < a[index]:
            index = i

    return index

def getMaxIndex(b):
    index = 0
    for i in range(len(a)):
        if b[i] > b[index]:
            index = i

    return index

summation =  0
for i in range(n):
    aMinIndex = getMinIndex(a)
    bMaxIndex = getMaxIndex(b)
    summation += a[aMinIndex] * b[bMaxIndex]
    a = a[:aMinIndex] + a[aMinIndex + 1:]
    b = b[:bMaxIndex] + b[bMaxIndex + 1:]

print(summation)