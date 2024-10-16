n = int(input())

offset = 100
arr = [[0 for _ in range(201)] for _ in range(201)]

cnt = 0

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            if arr[offset + x][offset + y] == 0:
                cnt += 1
                arr[offset + x][offset + y] = 1

print(cnt)