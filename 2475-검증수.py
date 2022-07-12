def square(num):
    return num ** 2


print(sum(map(square, list(map(int, input().split())))) % 10)
