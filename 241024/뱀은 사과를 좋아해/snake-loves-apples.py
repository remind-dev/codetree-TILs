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
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

ans = 0
for _ in range(k):
    d, p = input().split()
    p = int(p)

    for i in range(p):
        ans += 1
        nx, ny = x + dx[dir_map[d]], y + dy[dir_map[d]]

        if not in_range(nx, ny):
            print(ans)
            sys.exit(0)
        else:
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
            else:
                snake.popleft()

            if (nx, ny) in snake:
                print(ans)
                sys.exit(0)
            else:
                snake.append((nx,ny))


            x, y = nx, ny
        
print(ans)