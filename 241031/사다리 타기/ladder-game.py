n, m = map(int, input().split())

ladder_pos = []
for _ in range(m):
    a, b = map(int, input().split())
    ladder_pos.append((a, b))

# 특정 위치에서 시작하여 사다리를 타고 내려가며 도착 위치를 반환하는 함수
def climb_line(start, ladder_map):
    pos = start
    for row in range(15):
        if pos > 0 and ladder_map[row][pos - 1]:  # 왼쪽으로 이동
            pos -= 1
        elif pos < n - 1 and ladder_map[row][pos]:  # 오른쪽으로 이동
            pos += 1
    return pos

# 현재 선택된 가로줄로 결과를 시뮬레이션하는 함수
def simulate(curr_ladders):
    # 사다리 맵을 초기화
    ladder_map = [[False] * (n - 1) for _ in range(15)]
    for x, y in curr_ladders:
        ladder_map[y - 1][x - 1] = True

    # 각 세로줄에 대해 출발점에서 도착점까지 사다리를 탑니다.
    result = []
    for i in range(n):
        result.append(climb_line(i, ladder_map))
    
    return result

# 백트래킹을 사용하여 최소 가로줄을 찾는 함수
min_count = m
def backtracking(idx, curr_ladders):
    global min_count

    if len(curr_ladders) > min_count:
        return
    
    # 현재 가로줄 선택으로 결과를 시뮬레이션
    if simulate(curr_ladders) == simulate(ladder_pos):
        min_count = min(min_count, len(curr_ladders))
        return

    # 다음 가로줄을 선택하여 백트래킹
    for i in range(idx, len(ladder_pos)):
        curr_ladders.append(ladder_pos[i])
        backtracking(i + 1, curr_ladders)
        curr_ladders.pop()

# 백트래킹을 시작
backtracking(0, [])
print(min_count)