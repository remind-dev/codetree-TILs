n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for row in range(n):
    cnt = 1
    temp = arr[row][0]
    for col in range(1, n):
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
    temp = arr[0][col]
    for row in range(1, n):
        if temp == arr[row][col]:
            cnt += 1
        else:
            cnt = 1
            temp = arr[row][col]
        
        if cnt >= m:
            ans += 1
            break

print(ans)