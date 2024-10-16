n = int(input())
cnt = 1
arr = [0 for _ in range(1001)]
for i in range(n):

    cur = int(input())
    if i == 0:
        temp = cur
        continue

    if temp == cur:
        cnt += 1
    else:
        arr[temp] = max(cnt, arr[temp])
        temp = cur
        cnt = 1

arr[cur] = max(cnt, arr[cur])

print(max(arr))