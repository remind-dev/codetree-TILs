k, n = map(int, input().split())

def permutations(cnt, current):
    if cnt == n:
        print(current)
        return

    for i in range(1, k + 1):
        permutations(cnt + 1, current + str(i) + ' ')

permutations(0, "")