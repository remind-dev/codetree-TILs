n = int(input())
cnt = 0
for i in range(n):

    cur = int(input())
    if i == 0:
        cnt += 1
        temp = cur
        continue

    if temp != cur:
        cnt += 1
        temp = cur

print(cnt)