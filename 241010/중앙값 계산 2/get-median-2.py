n = int(input())
arr= list(map(int, input().split()))

arr.sort()

for i in range(n//2 + 1):
    print(arr[i], end=' ')