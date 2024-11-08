n = int(input())

arr = list(map(int, input().split()))

def calc(nums, idx_list):
    sum1 = sum(nums)

    sum2 = 0
    for i in range(len(arr)):
        if not i in idx_list:
            sum2 += arr[i]

    return abs(sum1 - sum2)

ans = float('inf')
nums = []

def backtrack(curr_idx, cnt, idx_list):
    global ans

    if curr_idx == 2*n:
        if cnt == n:
            ans = min(ans, calc(nums, idx_list))
        return


    nums.append(arr[curr_idx])
    backtrack(curr_idx + 1, cnt + 1, idx_list + [curr_idx])
    nums.pop()

    backtrack(curr_idx + 1, cnt, idx_list)

backtrack(0, 0, [])
print(ans)