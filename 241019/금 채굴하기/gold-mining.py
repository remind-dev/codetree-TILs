n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def find_gold(k, x, y):
    cnt = 0
    for dx in range(-k, k+1):
        for dy in range(-k, k+1):
            if (abs(dx) + abs(dy)) <= k:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                    cnt += 1
    return cnt




for k in range(0, n):
    pay = k*k + (k+1)*(k+1)

    for x in range(n):
        for y in range(n):
            cnt_gold = find_gold(k, x, y)
            if pay <= cnt_gold*m:
                ans = max(ans, cnt_gold)

print(ans)