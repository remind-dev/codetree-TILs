n, m = map(int, input().split())

pos = []
for i in range(n):
    x, y = map(int, input().split())
    pos.append((x,y))

pos.sort(key=lambda x: (x[0], x[1]))

ans = float('inf')
select_pos = []

def calc():
    x1, y1 = pos[0]
    x2, y2 = pos[-1]

    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def backtrack(idx, cnt):
    global ans

    if cnt == m:
        ans = min(ans ,calc())
        return
    
    if idx == n:
        return


    select_pos.append(pos[idx])
    backtrack(idx + 1, cnt + 1)
    select_pos.pop()

    backtrack(idx + 1, cnt)

backtrack(0, 0)
print(ans)