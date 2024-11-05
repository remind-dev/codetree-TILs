n = int(input())
arr = list(map(int, input().split()))

ans = -1
def backtrack(curr, cnt):
    global ans

    if curr >= n-1:
        if ans != -1:
            ans = min(ans, cnt)
        else:
            ans = cnt
        return

    for i in range(1, arr[curr]+1):
        backtrack(curr + i, cnt + 1)


backtrack(0, 0)

print(ans)