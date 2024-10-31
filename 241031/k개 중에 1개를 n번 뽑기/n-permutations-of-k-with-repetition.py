k, n = map(int, input().split())

p = []


def print_per():
    for i in p:
        print(i, end=' ')
    print()

def permutation(cnt):

    if cnt == n:
        print_per()
        return


    for i in range(1, k+1):
        p.append(i)
        permutation(cnt + 1)
        p.pop()


permutation(0)