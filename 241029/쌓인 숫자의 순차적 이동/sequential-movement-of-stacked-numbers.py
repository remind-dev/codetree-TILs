n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

num = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        grid[i][j] = [grid[i][j]]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def mmax(n):
    if n:
        return max(n)
    else:
        return 0

def find_max(x, y):
    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]

    MAX = 0
    max_x, max_y = 0, 0

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny):
            if MAX < mmax(grid[nx][ny]):
                MAX = mmax(grid[nx][ny])
                max_x = nx
                max_y = ny

    return (max_x, max_y)

for number in num:
    flag = False

    for i in range(n):
        for j in range(n):
            if number in grid[i][j] and not flag:
                x, y = find_max(i, j)
                grid[x][y] += grid[i][j][grid[i][j].index(number):]
                grid[i][j][grid[i][j].index(number):] = []
                flag = True


for i in range(n):
    for j in range(n):
        if not grid[i][j]:
            print('None', end='')
        else:
            for k in grid[i][j][::-1]:
                print(k, end = ' ')
        print()