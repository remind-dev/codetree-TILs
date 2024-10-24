n = int(input())
x, y = map(int, input().split())

arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    row = input()
    for j, elem in enumerate(row, start=1):
        arr[i][j] = elem

visited = [[[False for _ in range(4)] for _ in range(n+1)] for _ in range(n+1)]

DIR = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 < x <= n and 0 < y <= n

def wall_exist(x,y):
    return in_range(x, y) and arr[x][y] == '#'

ans = 0
while in_range(x, y):
    if visited[x][y][DIR]:
        ans = -1
        break

    visited[x][y][DIR] = True

    nx , ny = x + dx[DIR], y + dy[DIR]

    if wall_exist(nx, ny):
        DIR = (4 + DIR - 1) % 4

    elif not in_range(nx, ny):
        x, y = nx, ny
        ans += 1 
    else:
        rx = nx + dx[(DIR + 1) % 4]
        ry = ny + dy[(DIR + 1) % 4]

        if wall_exist(rx, ry):
            x, y = nx, ny
            ans += 1
        else:
            x, y = rx, ry
            DIR = (DIR + 1) % 4
            ans += 2


print(ans)