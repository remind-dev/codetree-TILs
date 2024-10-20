string = list(input())

n = len(string)

def shift():
    return string.insert(0, string.pop())

def check():
    length = ''
    cnt = 1
    for i in range(1, n):
        if string[i] == string[i - 1]:
            cnt += 1
        else:
            length = string[i-1] + str(cnt)

    if cnt > 1:
        length = string[i] + str(cnt)
        return len(length)
    else:
        return len(length) + 2


MIN = 21
for _ in range(n):
    shift()
    MIN = min(MIN, check())

print(MIN)