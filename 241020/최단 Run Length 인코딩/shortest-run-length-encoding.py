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
            length += string[i-1] + str(cnt)
            cnt = 1

    length += string[-1] + str(cnt)
    return len(length)


MIN = 21
for _ in range(n):
    shift()
    MIN = min(MIN, check())

print(MIN)