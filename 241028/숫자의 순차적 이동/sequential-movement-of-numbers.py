n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_max(x, y):
    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]

    MAX = 0
    max_x, max_y = 0, 0

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny):
            if MAX < grid[nx][ny]:
                MAX = grid[nx][ny]
                max_x = nx
                max_y = ny

    return (max_x, max_y)


for i in range(m):
    start = 1
    while start <= (n*n):
        for j in range(n):
            for k in range(n):
                if grid[j][k] == start:
                    temp = grid[j][k]
                    x, y = find_max(j, k)
                    grid[j][k] = grid[x][y]
                    grid[x][y] = temp
                    
                    start += 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=  ' ')

    print()