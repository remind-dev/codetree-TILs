n = int(input())
pinball = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move(x, y, next_dir):
    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]

    nx, ny = x + dxs[next_dir], y + dys[next_dir]
    return nx, ny, next_dir


def move_simulate(x, y, move_dir):
    move_cnt = 1

    while in_range(x, y):
        if pinball[x][y] == 1:
            x, y, move_dir = move(x, y, move_dir ^ 1)
        elif pinball[x][y] == 2:
            x, y, move_dir = move(x, y, 3 - move_dir)
        else:
            x, y, move_dir = move(x, y, move_dir)

        move_cnt += 1

    return move_cnt

ans = 0

for i in range(n):
    ans = max(ans, move_simulate(0, i, 0), move_simulate(n-1, i, 2), \
                move_simulate(i, 0, 3), move_simulate(i, n-1, 1))


print(ans)