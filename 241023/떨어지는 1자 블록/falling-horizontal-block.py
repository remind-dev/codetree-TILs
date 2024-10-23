n, m ,k = map(int, input().split())

arr = [list(map(int, input().split()))for _ in range(n)]

end = k + m - 1

k = k-1

block = [1 for _ in range(m)]

cur_row = 0
while True:
    flag = False

    if sum(arr[cur_row][k:end]) == 0:
        if cur_row + 1 >= n:
            arr[cur_row][k:end] = block
            flag = True
        else:
            cur_row += 1
    else:
        if cur_row == 0:
            flag = True
        else:
            arr[cur_row-1][k:end] = block
            flag = True

    if flag:
        break


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()