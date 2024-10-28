BLANK = -1
COLLIDE = -2

# 변수 선언 및 입력
t = int(input())
n, m = 0, 0
curr_dir = list()
next_dir = list()

# 입력으로 주어진 방향을 정의한 dx, dy에 맞도록
# 변환하는데 쓰이는 dict를 정의합니다.
mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}


# 해당 위치가 격자 안에 들어와 있는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 해당 위치에 dir 방향을 갖는 구슬이 새롭게 추가되는 경우에 대한
# 처리를 합니다.
def update_next_dir(x, y, move_dir):
    # 빈 곳이었다면 해당 구슬을 넣어주고
    if next_dir[x][y] == BLANK:
        next_dir[x][y] = move_dir
    # 빈 곳이 아니었다면 이미 다른 구슬이 놓여져 있는 것이므로
    # 충돌 표시를 해줍니다.
    else:
        next_dir[x][y] = COLLIDE


def move(x, y, move_dir):
    # 구슬이 벽에 부딪혔을 때의 처리를 간단히 하기 위해
    # dir 기준 0, 3이 대칭 1, 2가 대칭이 되도록 설정합니다.
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    
    # 바로 앞에 벽이 있는지를 판단합니다.
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    
    # Case 1 : 벽이 없는 경우에는 그대로 한 칸 전진합니다.
    # 따라서 그 다음 위치에 같은 방향을 갖는 구슬이 있게 됩니다.
    if in_range(nx, ny):
        update_next_dir(nx, ny, move_dir)
        
    # Case 2 : 벽이 있는 경우에는 방향을 반대로 틀어줍니다.
    # 따라서 같은 위치에 반대 방향을 갖는 구슬이 있게 됩니다.
    else:
        update_next_dir(x, y, 3 - move_dir)   


# 구슬을 전부 한 번씩 움직여봅니다.
def move_all():
    global next_dir
    
    # 그 다음 각 위치에서의 방향들을 전부 초기화 해놓습니다.
    next_dir = [
        [BLANK for _ in range(n + 1)]
        for _ in range(n + 1)
    ]
    
    # (i, j) 위치에 구슬이 있는경우
    # 움직임을 시도해보고, 그 결과를 전부 next_dir에 기록합니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if curr_dir[i][j] != BLANK:
                move(i, j, curr_dir[i][j])
    
    # next_dir 값을 다시 curr_dir에 복사합니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            curr_dir[i][j] = next_dir[i][j]


# 충돌이 일어나는 구슬을 전부 지워줍니다.
def remove_duplicate_marbles():
    # 충돌이 일어난 구슬들이 있는 위치만 빈 곳으로 설정하면 됩니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if curr_dir[i][j] == COLLIDE:
                curr_dir[i][j] = BLANK


# 조건에 맞춰 시뮬레이션을 진행합니다.
def simulate():
    # Step1
    # 구슬을 전부 한 번씩 움직여봅니다.
    move_all()
    
    # Step2
    # 움직임 이후에 충돌이 일어나는 구슬들을 골라 목록에서 지워줍니다.
    remove_duplicate_marbles()


for _ in range(t):
    # 입력
    n, m = tuple(map(int, input().split()))
    
    # 새로운 테스트 케이스가 시작될때마다 기존에 사용하던 값들을 초기화해줍니다.
    curr_dir = [
        [BLANK for _ in range(n + 1)]
        for _ in range(n + 1)
    ]
    
    for _ in range(m):
        x, y, d = tuple(input().split())
        x, y = int(x), int(y)
        curr_dir[x][y] = mapper[d]
    
    # 2 * n번 이후에는 충돌이 절대 일어날 수 없으므로
    # 시뮬레이션을 총 2 * n번 진행합니다.
    for _ in range(2 * n):
        simulate()
        
    marble_cnt = sum([
        curr_dir[i][j] != BLANK
        for i in range(1, n + 1)
        for j in range(1, n + 1)
    ])
    
    # 출력
    print(marble_cnt)