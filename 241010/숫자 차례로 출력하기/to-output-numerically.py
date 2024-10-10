n = int(input())
i = 1
def recursion(n):
    if n == 8:
        return

    print(n, end=' ')
    recursion(n+1)
    if n == 7:
        print()
    print(n, end=' ')
    
recursion(i)