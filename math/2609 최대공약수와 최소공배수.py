n, m = map(int, input().split())

def gcd(num1, num2):
    if num2 == 0:
        return num1;
    else:
        return gcd(num2, num1 % num2);

a = gcd(n, m)
b = n * m / a

print(a)
print(int(b))
