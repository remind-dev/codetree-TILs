n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

r,c = map(int, input().split())

r, c = r-1, c-1


temp = [[0 for _ in range(n)] for _ in range(n)]

boom = []
boom.append((r,c))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

for dx, dy in zip(dxs, dys):
    x, y = r, c
    for _ in range(a[r][c]-1):
        boom.append((x + dx, y + dy))
        x, y = x + dx, y + dy


for col in range(n):
    idx = n-1
    for row in range(n-1, -1, -1):
        if (row,col) not in boom:
            temp[idx][col] = a[row][col]
            idx -= 1

for i in range(n):
    for j in range(n):
        print(temp[i][j], end=' ')

    print()