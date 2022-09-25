from math import ceil

def solution(levels):
    levels.sort()
    index25 = ceil((len(levels) / 4) * 3)

    if index25 >= len(levels):
        return -1

    return levels[index25]