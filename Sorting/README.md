# Selection Sort

- '현재 index가 x일 때, x+1부터 n까지의 최소값과 swap'을 현재 index가 n일 때 까지 반복
- 현재 데이터의 상태와 상관없이 무조건 모든 원소를 비교
- 이중 반복문 -> O(N^2)

# Insertion Sort

- [정렬 된 부분], [정렬 안 된 부분]으로 구분해서, [정렬 안 된 부분]의 맨 앞이 [정렬 된 부분]의 어느 곳에 insert될 수 있는지 확인
- 정렬이 필요할 때만 swap 수행
- 이중 반복문 -> O(N^2), 그러나 거의 정렬된 배열을 정렬할 떄 뛰어난 성능

# Quick Sort

- 기준보다 큰 데이터와, 작은 데이터 swap을 반복
- 재귀적 구현
- 'pivot을 어떻게 설정할 것인가'에 따라 여러 가지 Quick sort algorithm이 존재
- O(NlogN) / 최악 O(N^2) = 데이터가 거의 정렬되어 있는 경우

# Count Sort

- 명확한 범위의 데이터를 정렬 (무한하거나 너무 큰 범위 X)
- 0 ~ N 사이의 수로 이뤄진 수열을 오름차순으로 정렬
- O(N + K) (N은 데이터 개수, K는 데이터의 최대 크기)

```python
n = 10
data = "1 1 9 9 2 8 8 3 3 3 7 7 7 7 4 6 5 5 0 0 0"
count = [0] * 10

for num in data.split():
    count[int(num)] += 1

for i in range(n):
    for j in range(count[i]):
        print(i)
```
