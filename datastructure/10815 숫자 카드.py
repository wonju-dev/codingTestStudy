import sys

input = sys.stdin.readline


def has(card, cards):
    head = 0
    tail = len(cards) - 1

    while head <= tail:
        mid = (head + tail) // 2

        if cards[mid] > card:
            tail = mid - 1
        elif cards[mid] < card:
            head = mid + 1
        else:
            return True
    
    return False

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    if has(t, cards):
        print(1, end=" ")
    else:
        print(0, end=" ")