from itertools import product


def join(tuple):
    return int("".join(list(map(str, tuple))))


n = input()
m = int(input())
brokens = list(map(int, input().split()))
buttons = [_ for _ in range(0, 10)]
count = 0
closeLocation = ""

if int(n) == 100:
    print(0)
elif len(brokens) == 10 and int(n) < 100:
    print(100 - int(n))
elif len(brokens) == 10 and int(n) > 100:
    print(int(n) - 100)
else:
    for b in brokens:
        buttons.remove(b)

    channels = list(map(join, list(product(buttons, repeat=len(n)))))
    closest = channels[0]
    for c in channels:
        if abs(int(n) - c) < abs(int(n) - closest):
            closest = c

    print(len(str(closest)) + abs(int(n) - closest))
