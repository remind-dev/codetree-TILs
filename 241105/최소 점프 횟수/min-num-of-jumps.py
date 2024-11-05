n = int(input())
arr = list(map(int, input().split()))

ans = 11
def backtrack(curr, cnt):
    global ans

    if curr >= n:
        ans = min(ans, cnt)
        return

    for i in range(1, arr[curr]+1):
        backtrack(curr + i, cnt + 1)


backtrack(0, 0)

print(ans-1)