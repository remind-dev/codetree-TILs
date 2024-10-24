from collections import deque
import sys

n, m, k = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]

x, y = 0, 0
snake = deque([(0,0)])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_map = {
    'R' : 0,
    'D' : 1,
    'L' : 2,
    'U' : 3
}

def in_range(x, y):
    return 0 <= x < n and 0 <= y <n

for _ in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

ans = 0
for _ in range(k):
    d, p = input().split()
    p = int(p)

    for i in range(p):
        nx, ny = x + dx[dir_map[d]], y + dy[dir_map[d]]

        if not in_range(nx, ny) and (nx, ny) in snake:
            print(ans)
            sys.exit(0)
        else:
            ans += 1
            snake.append((nx,ny))
            if arr[nx][ny]:
                arr[nx][ny] = 0
            else:
                snake.popleft()

            x, y = nx, ny
        
print(ans)