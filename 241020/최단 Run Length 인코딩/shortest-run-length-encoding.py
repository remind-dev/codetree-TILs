string = list(input())

n = len(string)

def shift():
    return string.insert(0, string.pop())

def check():
    length = 2
    for i in range(1, n):
        if string[i] == string[i - 1]:
            continue
        else:
            length += 2

    return length

MIN = 21
for _ in range(n):
    shift()
    MIN = min(MIN, check())

print(MIN)