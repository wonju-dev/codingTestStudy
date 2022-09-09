case = int(input())

for i in range(1, case + 1):
    words = input().split()
    words.reverse()
    ans = " ".join(words)
    print(f"Case #{i}: {ans}")