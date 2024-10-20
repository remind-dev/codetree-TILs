n, t = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(2)]

for _ in range(t):
    temp = belt[0][-1]
    
    for i in range(n-2, -1, -1):
        belt[0][i+1] = belt[0][i]

    belt[0][0] = belt[1][-1]

    for i in range(n-2, -1, -1):
        belt[1][i+1] = belt[1][i]

    belt[1][0] = temp


for i in belt:
    for j in i:
        print(j , end=' ')
    print()