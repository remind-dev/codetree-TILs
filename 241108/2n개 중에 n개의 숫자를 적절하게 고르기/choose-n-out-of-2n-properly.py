n = int(input())

arr = list(map(int, input().split()))

ans = float('inf')

def backtrack(curr_idx, cnt, diff):
    global ans

    if curr_idx == 2*n:
        if cnt == n:
            ans = min(ans, abs(diff))
        return


    backtrack(curr_idx + 1, cnt + 1, diff + arr[curr_idx])

    backtrack(curr_idx + 1, cnt, diff - arr[curr_idx])

backtrack(0, 0, 0)
print(ans)