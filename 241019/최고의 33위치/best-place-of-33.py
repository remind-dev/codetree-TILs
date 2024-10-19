n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

def find(x, y):
    cnt = 0

    for i in range(x, x+3):
        for j in range(y, y+3):
            cnt += arr[i][j]

    return cnt

max_total = 0
for i in range(n):
    if (i+2) >= n:
        continue
    for j in range(n):
        if (j+2) >= n:
            continue

        total = find(i, j)
        max_total = max(max_total, total)

print(max_total)