n = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(n):
    print(arr[i], end=' ')
print()
for i in range(n-1, -1, -1):
    print(arr[i], end=' ')