import sys
sys.setrecursionlimit(2000)

n = int(input())
grid = [list(input()) for _ in range(n)]

def find_pos():
    coins = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
            elif grid[i][j].isdigit():
                coins.append((i, j, int(grid[i][j])))
    coins.sort(key=lambda x: x[2])
    return start, end, coins

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

min_moves = float('inf')
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()  # 방문한 위치와 상태 기록

def dfs(x, y, collected_coins, moves, last_coin):
    global min_moves
    
    if (x, y) == end and len(collected_coins) >= 3:
        min_moves = min(min_moves, moves)
        return

    # 방문한 상태 기록 (위치와 마지막 수집한 동전 번호)
    state = (x, y, last_coin)
    if state in visited:
        return
    visited.add(state)
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if in_range(nx, ny):
            cell = grid[nx][ny]

            if cell.isdigit():
                coin_number = int(cell)
                if coin_number > last_coin:
                    dfs(nx, ny, collected_coins + [coin_number], moves + 1, coin_number)
            elif cell == '.' or cell == 'E':
                dfs(nx, ny, collected_coins, moves + 1, last_coin)

    # DFS 백트래킹 단계에서 방문 기록 제거
    visited.remove(state)

start, end, coins = find_pos()
dfs(start[0], start[1], [], 0, 0)

# 결과 출력
print(min_moves if min_moves != float('inf') else -1)