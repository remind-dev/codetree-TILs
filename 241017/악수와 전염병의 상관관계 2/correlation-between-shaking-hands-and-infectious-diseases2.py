n, k, p, t = map(int, input().split())

element = [tuple(map(int, input().split())) for _ in range(t)]
element.sort()

parasite = [0 for _ in range(n+1)]
parasite[p] = k

ans = [0 for _ in range(n+1)]
ans[p] = 1

for s, n1, n2 in element:
    if parasite[n1] and not parasite[n2] and ans[n1] and not ans[n2]:
        parasite[n1] -= 1
        parasite[n2] = k
        ans[n2] = 1
    elif parasite[n2] and not parasite[n1] and ans[n2] and not ans[n1]:
        parasite[n2] -= 1
        parasite[n1] = k
        ans[n1] = 1
    elif parasite[n1] and parasite[n1] and ans[n1] and ans[n2]:
        parasite[n1] -= 1
        parasite[n2] -= 1

for i in ans[1:]:
    print(i, end='')