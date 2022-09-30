# O(n)으로 개선 가능
# 거꾸로 접근하기
case = int(input())

while case > 0:
    num = int(input())
    values = list(map(int,input().split()))
    
    maxi = values[-1]
    ans = 0

    for i in range(len(values) - 2, -1, -1):
        if values[i] > maxi:
            maxi = values[i]
        else:
            ans += maxi - values[i]
    print(ans)

    case -=1
"""
3 3 7 9 7 4

5 5 10 1 1 9

2 5 10

9 5 4

10 9 8 7 6

11 5 5 10 1 1 9

9 8 7 1 2

1 2 3 1 1
"""