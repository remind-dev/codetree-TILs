n = int(input())

arr = list(map(int, input().split()))

def max_value(n):
    if n == 0:
        return arr[n]

    return max(max_value(n-1), arr[n])

print(max_value(n-1))