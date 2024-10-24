n, m, r, c = map(int,input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]
r, c =r-1, c-1

arr[r][c] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

bomb_list = ((r,c),)

for t in range(1, m+1):
    move = 2 ** (t - 1)

    temp = ()

    for x, y in bomb_list:
        for dx ,dy in zip(dxs, dys):
            nx = x + dx*move
            ny = y + dy*move

            if in_range(nx, ny):
                arr[nx][ny] = 1
                temp += (nx, ny)

    bomb_list += temp

print(sum(sum(row) for row in arr))