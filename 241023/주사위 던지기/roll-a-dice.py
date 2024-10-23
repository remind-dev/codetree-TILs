n, m, r, c = map(int,input().split())

dice = [1,2,3,4,5,6]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

dir_map = {
    'U' : 0,
    'D' : 1,
    'L' : 2,
    'R' : 3
}

def roll(direction):
    global dice

    if direction == 0:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif direction == 1:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif direction == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    else:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

r, c = r - 1, c - 1

direction = list(input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]
arr[r][c] = dice[5]

for i in range(m):

    cur_dir = dir_map[direction[i]]

    nr, nc = r + dxs[cur_dir] , c + dys[cur_dir]

    if in_range(nr, nc):
        roll(cur_dir)
        arr[nr][nc] = dice[5]

        r, c = nr, nc

print(sum(sum(row) for row in arr))