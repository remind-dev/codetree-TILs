BLANK = -1

n, m, t, k = map(int, input().split())
bead_list = list()

mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

def move(bead_list):

    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]

    x, y, move_dir, distance = bead_list
    
    # 바로 앞에 벽이 있는지를 판단합니다.
    for _ in range(distance):
        nx, ny = x + dxs[move_dir], y + dys[move_dir]

        if in_range(nx, ny):
            x, y = nx, ny
        else:
            move_dir = 3 - move_dir
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
            x, y = nx, ny
    
    return (x, y, move_dir, distance)

def move_all():
    for i, bead in enumerate(bead_list):
        bead_list[i] = move(bead)

def duplicate_exist(target_idx):
    target_x, target_y, _, _ = bead_list[target_idx]

    cnt = 0
    for i, (x, y, _, _) in enumerate(bead_list):
        if i != target_idx and (x, y) == (target_x, target_y):
            cnt += 1
        
        if cnt >= k:
            return True

    return False

def remove_duplicate():
    global bead_list

    bead_list = [
        bead
        for i, bead in enumerate(bead_list) if not duplicate_exist(i)
    ]

def simulate():

    move_all()

    remove_duplicate()



for _ in range(m):
    x, y, move_dir, distance = tuple(input().split())
    x, y, distance = int(x), int(y), int(distance)
    bead_list.append((x, y, mapper[move_dir], distance))

for _ in range(t):
    simulate()

print(len(bead_list))