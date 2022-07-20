import time


def recursive(x):
    if x == 1 or x == 2:
        return 1
    else:
        return recursive(x - 1) + recursive(x - 2)


d = [0] * 101
def DP(x):
    for i in range(1, 101):
        if i not in (1, 2):
            d[i] = d[i-1] + d[i-2]
        else:
            d[i] = 1



st = time.time()
print(recursive(40))
print(time.time() - st)

st = time.time()
DP(40)
print(d[40])
print(time.time() - st)


