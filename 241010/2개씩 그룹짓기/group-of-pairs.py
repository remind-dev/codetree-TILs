n = int(input())
arr = list(map(int, input().split()))

arr.sort()

group_max = 0
for i in range(n):
    group_sum = arr[i] + arr[2*n-1-i]
    if group_sum > group_max:
        group_max = group_sum

print(group_max)