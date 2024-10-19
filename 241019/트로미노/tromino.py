n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def rotate_90(arr):
    temp = zip(*arr[::-1])
    return [list(i) for i in temp]


ans = 0
temp_arr = arr
for _ in range(4):
    temp_arr = rotate_90(temp_arr)
    n, m = m, n

    for i in range(n):
        for j in range(m):

            if i+1 < n and j+1 < m:
                shape1 = temp_arr[i][j] + temp_arr[i+1][j] + temp_arr[i+1][j+1]

            if j+2 < m:
                shape2 = temp_arr[i][j] + temp_arr[i][j+1] + temp_arr[i][j+2] 

            ans = max(ans, shape1, shape2)

print(ans)