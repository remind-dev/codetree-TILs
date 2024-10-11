a, b, c = map(int, input().split())


mins = (a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11)

print(mins)