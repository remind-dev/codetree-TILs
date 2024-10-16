n , k = map(int, input().split())

arr = [0 for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    
    for j in range(a-1, b):
        arr[j] += 1

print(max(arr))