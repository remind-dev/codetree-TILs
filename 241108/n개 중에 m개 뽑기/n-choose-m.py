n, m = map(int, input().split())

ans = []
def print_ans():
    for i in ans:
        print(i, end = ' ')
    print()

def choose(curr, cnt):

    if curr == n + 1:
        if cnt == m:
            print_ans()
        return

    ans.append(curr)
    choose(curr+1, cnt + 1)
    ans.pop()

    choose(curr + 1, cnt)

choose(1, 0)