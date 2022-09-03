def isEvenWhite(row, col):
    return row % 2 == 0 and col % 2 == 0

def isOddWhite(row, col):
    return row % 2 == 1 and col % 2 == 1


ROW_LENGTH = 8
COL_LENGTH = 8

graph = []

for row in range(ROW_LENGTH):
    graph.append(list(input()))        

count = 0 
for row in range(ROW_LENGTH):
    for col in range(COL_LENGTH):
        if isEvenWhite(row, col) or isOddWhite(row, col):
            if graph[row][col] == "F":
                count += 1
print(count)