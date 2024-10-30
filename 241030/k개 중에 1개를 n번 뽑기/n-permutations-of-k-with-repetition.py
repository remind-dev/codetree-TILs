k, n = map(int, input().split())

answer = []

def print_permutation():
    for num in answer:
        print(num, end=' ')
    print()

def permutations(cnt):
    if cnt == n:
        print_permutation()
        return

    for i in range(1, k+1):
        answer.append(i)
        permutations(cnt+1)
        answer.pop()

permutations(0)