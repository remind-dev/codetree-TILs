n = int(input())

def recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return recursion(n // 3) + recursion(n-1)

print(recursion(n))