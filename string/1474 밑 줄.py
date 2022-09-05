from collections import deque


n, m = map(int, input().split())

# 단어 목록
words = deque()
# 단어 길이 총합
length = 0
for _ in range(n):
    word = input()
    
    length += len(word)
    words.append(word)

# 한 단어당 가져갸아 하는 언더바
chunks = [0] * (n - 1)
if length < m:
    remain = m - length
    for i in range(remain):
        chunks[i % (n - 1)] += 1
        remain -= 1
chunks = deque(chunks)
    
def getAsciiDistance(a, b):
    return abs(ord(a) - ord(b))

answer = ""
while len(words) != 1:
    wordA = words.popleft()
    wordB = words.popleft()

    # words[i]와 words[i]의 첫글자 간격과, words[i]와 '_'의 간격을 비교
    # 간격 = ascii 차이
    if getAsciiDistance(wordA[0], wordB[0]) > getAsciiDistance(wordA[0], "_"):
        words.appendleft(wordA + "_" * chunks.popleft() + wordB)
    else:
        words.appendleft(wordA + "_" * chunks.pop() + wordB)

print(words[0])