def getHash(chunk):
    value = 0
    for i in range(len(chunk) - 1, -1, -1):
        value += 2 ** i * ord(chunk[len(chunk) -1 - i])
    return value;

n = int(input())
pn = "IO" * n + "I"
pnHash = getHash(pn)

m = int(input())
string = input()
hash = getHash(string[:n * 2 + 1])

count = 0
if pnHash == hash:
    count += 1

for i in range(1, m - (n * 2 + 1)):
    # 다음 chunk의 해시 값 = 2 * (이전 chunk 해시값 - 맨 앞 글자의 해시값) + 다음 chunk의 마지막 해시값
    hash = 2 * (hash - 2 ** (n * 2) * ord(string[i - 1])) + ord(string[i + n * 2])

    if pnHash == hash:
        count += 1

print(count)