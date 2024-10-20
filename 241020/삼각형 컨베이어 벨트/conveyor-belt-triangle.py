n, t = map(int, input().split())
belt = [list(map(int,input().split())) for _ in range(3)]

for _ in range(t):
    temp1 = belt[0][-1]
    temp2 = belt[1][-1]
    temp3 = belt[2][-1]

    for i in range(n-2, -1, -1):
        belt[0][i + 1] = belt[0][i]

    for i in range(n-2, -1, -1):
        belt[1][i + 1] = belt[1][i]

    for i in range(n-2, -1, -1):
        belt[2][i + 1] = belt[2][i]

    belt[0][0] = temp3
    belt[1][0] = temp1
    belt[2][0] = temp2

for i in belt:
    for j in i:
        print(j, end= ' ')
    print()