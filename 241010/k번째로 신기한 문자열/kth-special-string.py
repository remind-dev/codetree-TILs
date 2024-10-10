n, k, t = input().split()
n, k = int(n), int(k)

arr = []
for i in range(n):
    length = len(t)
    word = input()
    if word[:length] == t:
        arr.append(word)
        
arr.sort()
print(arr[k-1])