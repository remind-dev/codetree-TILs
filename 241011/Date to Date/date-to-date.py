m1 , d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = 11
day = 5
elapsed_time = 0

while True:

    if month == 12 and day == 21:
        break

    elapsed_time += 1
    day += 1

    if day > num_of_days[month]:
        month += 1
        day = 1

print(elapsed_time + 1)