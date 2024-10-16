n = int(input())
cnt = 1
ans = 0
for i in range(n):

    cur = int(input())
    if i == 0:
        temp = cur
        continue

    if temp == cur:
        cnt += 1
    else:
        ans = max(ans, cnt)
        temp = cur
        cnt = 1

ans = max(ans,cnt)

print(ans)