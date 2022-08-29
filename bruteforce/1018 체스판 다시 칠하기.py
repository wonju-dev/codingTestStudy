# 입력값 초기화
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

minimum = 65 

def check(row, col):
    global minimum

    count = 0
    
    # '좌측 상단'에서 '우측 하단' 방향으로 8*8 성립할 수 있으면
    if 0 <= row and row + 7 < n and 0 <= col and col + 7 < m:
        # 첫 번째 색을 기준으로 검증
        first = board[row][col]
        next = "W" if first == "B" else "B"

        for rowIndex in range(8):
            for colIndex in range(8):
                if rowIndex != 0 or colIndex != 0:
                    if board[row + rowIndex][col + colIndex] != next:
                        count += 1
                    if colIndex != 7:
                        next = "W" if next == "B" else "B"
        if minimum > count:
            minimum = count

        # 첫 번째 색과 반대 색으로 검증
        count = 0
        first = board[row][col]
        next = "B" if first == "B" else "W"
        count += 1

        for rowIndex in range(8):
            for colIndex in range(8):
                if rowIndex != 0 or colIndex != 0:
                    if board[row + rowIndex][col + colIndex] != next:
                        count += 1
                    if colIndex != 7:
                        next = "W" if next == "B" else "B"
                
        if minimum > count:
            minimum = count

# 매 위치에 대해 검증 시도
for row in range(n):
    for col in range(m):
        check(row, col)

print(minimum)
