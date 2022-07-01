n, m = map(int, input().split())

dic = {}

for i in range(n):
    key, value = map(str, input().split())
    dic[key] = value

for i in range(m):
    key = input()
    print(dic[key])
