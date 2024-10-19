n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def rect_sum(x1, y1, x2, y2):
    return sum([grid[i][j] for i in range(x1, x2 + 1) for j in range(y1, y2 + 1)])


MAX = -100000000000000
ans = 0

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if MAX < rect_sum(i, j, k, l):
                    MAX = rect_sum(i, j, k, l)
                    ans = (k - i + 1) * (l - j + 1)


print(ans)