n = int(input())
storage = list(map(int, input().split()))

# d[i]: i번째를 털었을 때의 최대값
d = [0] * 101
# 0번째는 당연히 털었을 때가 최대
d[0] = storage[0]
# 1번째는 '0번째를 털었을 때' vs '0번째를 생략하고 1번째를 털었을 떄'의 최대값
d[1] = max(storage[1], storage[0])

for i in range(2, n):
    # i번째는 '자신의 전칸을 털었을 때의 최대값' vs '자신의 전전칸을 털었을 때의 최대값 + 자신의 값'의 최대값
    d[i] = max(storage[i-1], storage[i-2] + storage[i])

print(d[n-1])
