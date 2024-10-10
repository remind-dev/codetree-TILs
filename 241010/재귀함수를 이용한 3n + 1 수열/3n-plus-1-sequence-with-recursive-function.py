n = int(input())

def re(n):
    if n == 2:
        return 1

    if n % 2 == 0:
        return re(n // 2) + 1
    else:
        return re(n * 3 + 1) + 1

print(re(n))