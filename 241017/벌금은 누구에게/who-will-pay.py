n, m, k = map(int, input().split())

arr = [0 for _ in range(n + 1)]
ans = -1
for i in range(1,m+1):
    p = int(input())

    arr[p] += 1
    if arr[p] >= k:
        ans = p
        break

print(ans)