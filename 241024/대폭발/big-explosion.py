n, m, r, c = map(int, input().split())

# 초기 배열을 0으로 채운 n x n 배열로 생성
arr = [[0 for _ in range(n)] for _ in range(n)]
r, c = r - 1, c - 1  # 0-based 인덱스로 변환

arr[r][c] = 1  # 폭탄이 시작하는 위치 표시

# 범위 체크 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 상하좌우 이동 방향
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 폭탄 리스트를 set으로 초기화 (중복 방지)
bomb_set = {(r, c)}

# m번 동안 반복
for t in range(1, m + 1):
    move = 2 ** (t - 1)  # t-1 단계에서의 이동 거리 계산

    temp_set = set()  # 새로운 폭탄 위치를 저장할 임시 set

    # 폭탄이 있는 모든 위치에서 상하좌우로 폭발 확산
    for x, y in bomb_set:
        for dx, dy in zip(dxs, dys):
            nx = x + dx * move
            ny = y + dy * move

            # 범위 내에 있을 경우 폭탄 확산
            if in_range(nx, ny):
                arr[nx][ny] = 1
                temp_set.add((nx, ny))  # 새로운 좌표를 set에 추가

    bomb_set.update(temp_set)  # 기존 bomb_set에 새로운 폭탄 위치들을 추가

# 1로 표시된 모든 칸의 개수 출력
print(sum(sum(row) for row in arr))