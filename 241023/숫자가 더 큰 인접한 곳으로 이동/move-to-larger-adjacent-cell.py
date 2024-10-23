n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = r-1, c-1
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

print(arr[r][c], end=' ')

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
    

while True:
    flag = False

    for dx, dy in zip(dxs, dys):
        nr, nc = r + dx, c + dy

        if in_range(nr, nc):
            if arr[nr][nc] > arr[r][c]:
                print(arr[nr][nc], end=' ')
                r, c = nr, nc
                flag = True
                break

    if not flag:
        break