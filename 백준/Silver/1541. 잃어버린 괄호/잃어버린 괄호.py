""" 
1. -단위로 분리
2. +단위로 분리 & 각 trim & sum
3. 뺄샘

 """


def trim(chunk):
    return chunk.lstrip("0")


def oper(chunk):
    return sum(list(map(int, list(map(trim, chunk.split("+"))))))


n = list(map(oper, input().split("-")))
answer = n[0]

for i in range(1, len(n)):
    answer -= n[i]

print(answer)
