n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for row in range(n):
    cnt = 1
    for col in range(n):
        if col == 0:
            temp = arr[row][col]
            continue

        if temp == arr[row][col]:
            cnt += 1
        else:
            cnt = 1
            temp = arr[row][col]
        
        if cnt >= m:
            ans += 1
            break

for col in range(n):
    cnt = 1
    for row in range(n):
        if row == 0:
            temp = arr[row][col]
            continue

        if temp == arr[row][col]:
            cnt += 1
        else:
            cnt = 1
            temp = arr[row][col]
        
        if cnt >= m:
            ans += 1
            break

print(ans)