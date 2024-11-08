n = int(input())
grid = [list(input()) for _ in range(n)]


def find_pos():
    coins_pos = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i,j)
            elif grid[i][j] == 'E':
                end = (i, j)
            elif grid[i][j].isdigit():
                coins_pos.append((grid[i][j].isdigit(), i, j))

    coins_pos.sort()

    return start, end, coins_pos

min_moves = float('inf')
curr_coin_pos = []

def calc_move():
    move = 0
    x, y = start

    for _, nx, ny in curr_coin_pos:
        move += (abs(x - nx) + abs(y - ny))
        x, y = nx, ny


    move += (abs(x - end[0]) + abs(y - end[1]))

    return move
    

def backtrack(cur_idx, cnt):
    global min_moves

    if cur_idx == len(coins_pos):
        if cnt >= 3:
            min_moves = min(min_moves, calc_move())
        return

    curr_coin_pos.append(coins_pos[cur_idx])
    backtrack(cur_idx + 1, cnt + 1)
    curr_coin_pos.pop()

    backtrack(cur_idx + 1, cnt)

start, end, coins_pos = find_pos()

backtrack(0, 0)

print(min_moves)