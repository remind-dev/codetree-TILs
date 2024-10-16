a, b = map(int, input().split())
n = list(map(int, input()))

num = 0

for i in range(len(n)):
    num = num * a + n[i]


arr = []

while True:
    if num < b:
        arr.append(num)
        break

    arr.append(num % b)
    num //= b

for i in arr[::-1]:
    print(i, end='')