n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

count = [[0] * n for _ in range(n)]
next_count = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    count[x-1][y-1] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    max_x, max_y = 0, 0
    MAX = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny):
            if MAX < arr[nx][ny]:
                MAX = arr[nx][ny]
                max_x = nx
                max_y = ny

    return (max_x, max_y)

for i in range(t):
    next_count = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if count[i][j]:
                x, y = move(i, j)
                next_count[x][y] += 1

    for i in range(n):
        for j in range(n):
            if next_count[i][j] > 1:
                next_count[i][j] = 0

    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

print(sum(sum(row) for row in count))