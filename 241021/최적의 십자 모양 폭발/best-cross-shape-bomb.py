import sys  
input = sys.stdin.readline  
from copy import deepcopy  

# 폭탄 터트리기  
def bomb(temp, si, sj):  
    cnt = temp[si][sj]  
    temp[si][sj] = 0  
    # 가로의 경우 터진 곳 저장  
    # 세로의 경우 가장 윗 칸과 가장 아랫 칸 저장    
    width = []  
    height = [(si, sj)]  
    for d in range(4):  
        ni, nj = si, sj  
        now = cnt - 1  
        while now and 0<=ni+di[d]<N and 0<=nj+dj[d]<N:  
            ni += di[d]  
            nj += dj[d]  
            if d == 1 or d == 3:  
                width.append((ni, nj))  
            else:  
                height.append((ni, nj))  
            temp[ni][nj] = 0  
            now -= 1  

    gravity(temp, width, height)  

# 중력 떨어트리기  
def gravity(temp, width, height):  
    # 가장 윗칸인 경우 width는 무시하고 진행  
    if width and not width[0][0] == 0:  
        for wi, wj in width:  
            while wi - 1 >= 0:  
                temp[wi][wj] = temp[wi-1][wj]  
                temp[wi-1][wj] = 0  
                wi -= 1  
    # 가장 아랫 칸과 윗 칸을 변수에 할당 해주고  
    # 가장 윗 칸 -1 => 옮겨야 되는 칸이 범위 내이고 현재 칸이 폭탄이 터진 경우 계속 옮겨준다.    
    height.sort(reverse=True)  
    if not height[-1][0] == 0:  
        hi, hj, mi, mj = height[0][0], height[0][1], height[-1][0], height[-1][1]  
        mi, mj = mi-1, mj  
        while mi >= 0 and mi < N and temp[hi][hj] == 0:  
            temp[hi][hj] = temp[mi][mj]  
            temp[mi][mj] = 0  
            hi -= 1  
            mi -= 1  
    check(temp)  

def check(temp):  
    global result  
    cnt = 0  
    for ti in range(N):  
        for tj in range(N):  
            if temp[ti][tj]:  
                flag = temp[ti][tj]  
                # 아래와 오른쪽만 체크해준다.  
                for d in range(2):  
                    nti, ntj = ti + di[d], tj + dj[d]  
                    if 0<=nti<N and 0<=ntj<N:  
                        if flag == temp[nti][ntj]:  
                            cnt += 1  
    if cnt > result:  
        result = cnt  

N = int(input())  
arr = [list(map(int, input().split())) for _ in range(N)]  
result = 0  
di, dj = [1, 0, -1, 0], [0, 1, 0, -1]  

for i in range(N):  
    for j in range(N):  
        temp = deepcopy(arr)  
        bomb(temp, i, j)  
print(result)