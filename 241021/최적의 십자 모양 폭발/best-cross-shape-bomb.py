# 변수 선언 및 입력:
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]
temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and \
           abs(x - center_x) + abs(y - center_y) < bomb_range


def bomb(center_x, center_y):
    # Step1. next_grid 값을 0으로 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    # Step2. 폭탄이 터질 위치는 0으로 채워줍니다.
    bomb_range = grid[center_x][center_y]
    
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, center_x, center_y, bomb_range):
                grid[i][j] = 0
	
    # Step3. 폭탄이 터진 이후의 결과를 next_grid에 저장합니다.
    for j in range(n):
        next_row = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j]:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1
                
    # Step4. grid로 다시 값을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


def save_grid():
    for i in range(n):
        for j in range(n):
            temp[i][j] = grid[i][j]


def load_grid():
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def meet_the_condition(x, y, nx, ny):
    return in_range(nx, ny) and grid[x][y] and grid[x][y] == grid[nx][ny]


def calc():
    max_pair = 0

    for i in range(n):
        for j in range(n-1):
            if grid[i][j] and grid[i][j] == grid[i][j+1]:
                max_pair += 1

    for j in range(n):
        for i in range(n-1):
            if grid[i][j] and grid[i][j] == grid[i+1][j]:
                max_pair += 1

    return max_pair

            

ans = 0

# 각 위치에 대해 진행해보고
# 그 중 최대 만족 횟수를 구합니다.
for i in range(n):
    for j in range(n):
        save_grid()
        bomb(i, j)
        ans = max(ans, calc())
        load_grid()

print(ans)