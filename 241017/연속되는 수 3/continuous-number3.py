n = int(input())

cnt = 1
temp = 0
ans = 0
for i in range(n):

    cur = int(input())

    if i == 0:
        temp = cur
        continue

    
    if temp < 0 and cur < 0:
        cnt += 1
        temp = cur
    elif temp > 0 and cur > 0:
        cnt += 1
        temp = cur
    else:
        ans = max(ans, cnt)
        cnt = 1
        temp = cur

ans = max(ans, cnt)

print(ans)