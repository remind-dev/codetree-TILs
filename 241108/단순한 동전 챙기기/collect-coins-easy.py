n = int(input())
grid = [list(input()) for _ in range(n)]

def find_pos():
    coins_pos = []
    start = end = None

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
            elif grid[i][j].isdigit():
                # 동전 번호를 첫 번째 요소로 추가
                coins_pos.append((grid[i][j], i, j))

    # 동전 번호 기준으로 정렬
    coins_pos.sort()

    return start, end, coins_pos

# 시작점과 도착점, 동전 위치 정보
start, end, coins_pos = find_pos()

# 최소 이동 횟수 초기화
min_moves = float('inf')

# 현재 선택한 동전 위치들을 담는 리스트
curr_coin_pos = []

# 이동 거리 계산 함수
def calc_move(start, end, curr_coin_pos):
    move = 0
    x, y = start

    for _, nx, ny in curr_coin_pos:
        move += (abs(x - nx) + abs(y - ny))
        x, y = nx, ny

    # 마지막 동전 위치에서 도착점까지의 거리 추가
    move += (abs(x - end[0]) + abs(y - end[1]))

    return move

# 백트래킹 함수
def backtrack(cur_idx, cnt):
    global min_moves

    # 모든 동전을 확인한 경우
    if cur_idx == len(coins_pos):
        if cnt >= 3:
            min_moves = min(min_moves, calc_move(start, end, curr_coin_pos))
        return

    # 동전 선택하는 경우 (동전 번호가 증가하는 순서로 선택)
    curr_coin_pos.append(coins_pos[cur_idx])
    backtrack(cur_idx + 1, cnt + 1)
    curr_coin_pos.pop()

    # 동전 선택하지 않는 경우
    backtrack(cur_idx + 1, cnt)

# 백트래킹 시작
backtrack(0, 0)

# 결과 출력
print(min_moves if min_moves != float('inf') else -1)