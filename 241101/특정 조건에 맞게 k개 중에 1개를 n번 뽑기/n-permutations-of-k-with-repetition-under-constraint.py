k, n = map(int, input().split())

num = []

def print_number():
    for i in num:
        print(i, end=' ')
    print()

def backtrack(cnt):
    if cnt == n:
        print_number()
        return

    for i in range(1, k+1):
        if len(num) >= 2 and num[-1] == i and num[-2] == i:
            continue
        else:
            num.append(i)
            backtrack(cnt + 1)
            num.pop()

backtrack(0)