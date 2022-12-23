target = int(input())
# +, - 으로 이동한 횟수로 초기화
ans = abs(100 - target)
m = int(input())

if m != 0 :
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001):
    for n in str(num):
        if n in broken:
            break
    # 버튼으로 누를 수 있는 숫자에 한해서 검증
    else:
        # 이전 최소값 vs 해당번호로 버튼 눌러서 이동 + '+, -' 으로 이동한 횟수
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)