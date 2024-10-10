n = int(input())
arr = list(map(int, input().split()))

def list_(n, arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2
        

list_(n,arr)

for i in range(n):
    print(arr[i], end=' ')