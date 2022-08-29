case = int(input())
for _ in range(case):
    a, b, c = map(int, input().split())
    count = 0
    for aa in range(1, a + 1):
        for bb in range(1, b + 1):
            for cc in range(1, c + 1):
                if aa % bb == bb % cc == cc % aa:
                    count += 1
    print(count)