a, b, c = map(int, input().split())

day = a - 11
mins = (b * 60 + c) - (11 * 60 + 11)

print(day * 24 * 60 + mins)