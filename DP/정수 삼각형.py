n = int(input())

dp = [0] * 501

beforeIndex = 0
for i in range(n):
    row = list(map(int, input().split()))
    
    if i != 0:
        leftIndex = beforeIndex
        rightIndex = beforeIndex + 1
        if row[leftIndex] > row[rightIndex]:
            dp[i] = dp[i - 1] + row[leftIndex]
            beforeIndex = leftIndex
        else:
            dp[i] = dp[i - 1] + row[rightIndex]
            beforeIndex = rightIndex
    else:
        dp[i] = row[0]
        
print(dp[n - 1])