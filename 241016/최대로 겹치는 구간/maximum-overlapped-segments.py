n = int(input())

arr = [0 for _ in range(203)]
for i in range(n):
    a, b = map(int, input().split())
    a = 100 + a
    b = 100 + b

    for j in range(a, b):
        arr[j] += 1

print(max(arr))