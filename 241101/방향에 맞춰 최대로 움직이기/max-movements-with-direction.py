n = int(input())
grid =[list(map(int, input().split())) for _ in range(n)]
direction = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())
r, c = r-1, c-1 

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 0, 1, 1, 1, 0, -1, -1, -1]


ans = 0
def simulate(x, y, cnt):
    global ans

    ans = max(ans, cnt)

    for i in range(1, n):
        nx = x + dxs[direction[x][y]] * i
        ny = y + dys[direction[x][y]] * i

        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            simulate(nx, ny, cnt + 1)
    
simulate(r, c, 0)
print(ans)