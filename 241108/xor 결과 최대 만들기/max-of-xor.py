n, m = map(int, input().split())
lst = list(map(int, input().split()))

ans = []
MAX = 0
def calc_xor():
    temp = ans[0]
    for i in ans[1:]:
        temp = temp ^ i 
    return temp

def backtrack(curr, cnt):
    global MAX

    if curr == n:
        if cnt == m:
            MAX = max(MAX, calc_xor())
        return


    ans.append(lst[curr])
    backtrack(curr + 1, cnt + 1)
    ans.pop()

    backtrack(curr + 1, cnt)

backtrack(0, 0)
print(MAX)