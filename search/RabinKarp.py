def getHash(chunk):
    # value = sum(2 ^ (chunk 길이 - 1 - i) * chunk[i]의 ASCII코드 값)
    # abc
    # a : 2 ^ 2 * ord(chunk[0])
    # b : 2 ^ 1 * ord(chunk[1])
    # c : 2 ^ 0 * ord(chunl[2])
    value = 0
    for i in range(len(chunk) - 1, -1, -1):
        value += 2 ** i * ord(chunk[len(chunk) -1 - i])
    return value;

string = "abcdababcdabeabcabc"
target = "abc"
count = 0

# 첫 번째 chunk(abc)의 해시값
hashValue = getHash(string[:len(target)])
# 찾으려는 문자열(abc)의 해시값
targetHash = getHash(target)

if hashValue == targetHash:
    count += 1

for i in range(1, len(string) - len(target) + 1):
    # 다음 chunk의 해시 값 = 2 * (이전 chunk 해시값 - 맨 앞 글자의 해시값) + 다음 chunk의 마지막 해시값
    hashValue = 2 * (hashValue - (2 ** (len(target) - 1)) * ord(string[i - 1])) + ord(string[i + len(target) - 1])
    if hashValue == targetHash:
        count += 1

print(count)

