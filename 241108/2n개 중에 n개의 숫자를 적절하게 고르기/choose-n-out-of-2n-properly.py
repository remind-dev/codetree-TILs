n = int(input())

arr = list(map(int, input().split()))

def calc(nums):
    sum1 = sum(nums)

    sum2 = 0
    for i in arr:
        if not i in nums:
            sum2 += i

    return abs(sum1 - sum2)

ans = float('inf')
nums = []
def backtrack(curr_idx, cnt):
    global ans

    if curr_idx == 2*n:
        if cnt == n:
            ans = min(ans, calc(nums))
        return


    nums.append(arr[curr_idx])
    backtrack(curr_idx + 1, cnt + 1)
    nums.pop()

    backtrack(curr_idx + 1, cnt)

backtrack(0, 0)
print(ans)