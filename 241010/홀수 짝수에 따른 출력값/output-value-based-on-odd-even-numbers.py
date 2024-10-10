n = int(input())

def recur(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return recur(n-2) + n

print(recur(n))