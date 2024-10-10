a, b, c = map(int, input().split())
d = a * b * c

def recursion(n):
    if n < 10:
        return n

    return recursion(n // 10) + n % 10

print(recursion(d))