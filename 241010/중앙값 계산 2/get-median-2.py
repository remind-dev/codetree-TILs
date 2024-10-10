n = int(input())
arr= list(map(int, input().split()))

for i in range(n):
    if (i+1) % 2 != 0:
        temp = arr[:i+1]
        temp.sort()
        print(temp[(i+1) // 2], end=' ')