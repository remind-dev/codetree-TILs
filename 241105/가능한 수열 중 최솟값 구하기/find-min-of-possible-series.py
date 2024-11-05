n = int(input())

def check():
    cont_n = len(seq) // 2

    for i in range(1, cont_n+1):
        for j in range(len(seq)-i):

            if seq[j:j+i] == seq[j+i:j+i+i]:
                return False

    return True

def example_check():

    if check():
        print(1)
    else:
        print(0)

seq = []
ans = []
def backtrack(cnt):
    global ans

    if cnt == n:
        if check() and not ans:
            ans = seq[:]
        return

    for i in range(4, 7):
        if ans:
            return
        seq.append(i)
        backtrack(cnt + 1)
        seq.pop()

backtrack(0)

for i in ans:
    print(i, end='')