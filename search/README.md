# 'in' 키워드로 값 찾기 속도

set == dict >> list

# 문자열 검색

## 1. Naive

- 전체 문자열을 차례대로 하나씩 비교하는 방식
- O(N\*M) (N: 전체 문자열 길이, M: 찾으려는 문자열 길이)

## 2. Rabin Karp

- 해시 함수를 통해 문자열을 비교
- sum(2 ^ len(chunk) - 1 - i \* chunk[i])
- O(n)

## 3. KMP

-
