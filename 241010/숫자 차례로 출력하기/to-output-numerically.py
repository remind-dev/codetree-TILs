n = int(input())
i = 1
def recursion(i, n):
    if i == n+1:
        return

    print(i, end=' ')
    recursion(i+1, n)
    if i == n:
        print()
    print(i, end=' ')
    
recursion(i, n)