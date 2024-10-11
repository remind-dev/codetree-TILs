m1, d1, m2, d2 = map(int, input().split())

def cal_day(m, d):
    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = 0

    for i in range(1, m):
        total += num_of_days[i]

    return total + d

diff_day = cal_day(m2, d2) - cal_day(m1, d1)

day_of_the_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
current = 1

if diff_day < 0:
    diff_day = abs(diff_day) % 7
    if current - diff_day < 0:
        print(day_of_the_week[ 7 + current - diff_day])
    else:
        print(day_of_the_week[current - diff_day])
else:
    diff_day = diff_day % 7
    print(day_of_the_week[current + diff_day])