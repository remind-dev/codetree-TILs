def move():  
    location = [[[] for _ in range(N)] for _ in range(N)]  
    for i, m in enumerate(marbles):  
        if not m:  
            continue  
        si, sj, d, w = m  
        ni, nj = si+di[d], sj+dj[d]  
        if 0<=ni<N and 0<=nj<N:  
            si, sj = ni, nj  
            marbles[i] = [ni, nj, d, w]  
        else:  
            marbles[i] = [si, sj, (d+2)%4, w]  
        location[si][sj].append(i)  
    remove(location)  

def remove(location):  
    for i in range(N):  
        for j in range(N):  
            if len(location[i][j]) >= 2:  
                temp = sorted(location[i][j], reverse=True)  
                val = marbles[temp[0]][3]  
                for t in range(1, len(temp)):  
                    val += marbles[temp[t]][3]  
                    marbles[temp[t]] = []  
                marbles[temp[0]][3] = val  



N, M, T = map(int, input().split())  
di, dj = [1, 0, -1, 0], [0, -1, 0, 1]  
marbles = []  
convert= {'L':1, 'R': 3, 'U':2, 'D':0}  
for _ in range(M):  
    a, b, c, d = map(str, input().split())  
    marbles.append([int(a)-1, int(b)-1, convert[c], int(d)])  
for _ in range(T):  
    move()  

cnt, weight = 0, 0  
for i in marbles:  
    if i:  
        cnt += 1  
        weight = max(weight, i[3])  
print(cnt, weight)