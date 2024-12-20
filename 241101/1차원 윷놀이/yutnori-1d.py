n, m, k = map(int,input().split())
distance = list(map(int, input().split()))

hores = [0] * k


def arrive():
    point = 0
    for dis in hores:
        if dis >= m-1:
            point += 1

    return point


ans = 0
def yutnori(cnt):
    global ans

    if cnt == n:
        ans = max(ans, arrive())
        return

    for i in range(k):
        hores[i] += distance[cnt]
        yutnori(cnt + 1)
        hores[i] -= distance[cnt]


yutnori(0)
print(ans)