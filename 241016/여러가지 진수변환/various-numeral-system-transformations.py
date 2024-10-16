n, b = map(int, input().split())

arr = []

while True:
    if n < 4:
        arr.append(n)
        break

    arr.append(n % b)
    n = n // b

for i in arr[::-1]:
    print(i, end='')