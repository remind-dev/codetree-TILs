n = int(input())
arr = [int(input()) for _ in range(n)]


for _ in range(2):
    temp = []
    s, e = map(int, input().split())

    for i in range(len(arr)):
        if s-1 <= i <= e-1:
            continue
        else:
            temp.append(arr[i])


    arr = temp

print(len(temp))
for i in temp:
    print(i)