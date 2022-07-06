n = int(input())
pn = "IO" * n + "I"
len_pn = len(pn)

m = int(input())
s = input()

answer = 0


for i in range(m - len_pn + 1):
    if s[i : i + len_pn] == pn:
        answer += 1

print(answer)
