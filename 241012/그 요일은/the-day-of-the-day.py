m1, d1, m2, d2 = map(int, input().split())
week = input()

def cal_day(m, d):
    num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = 0

    for i in range(1, m):
        total += num_of_days[i]

    return total + d

diff = cal_day(m2, d2) - cal_day(m1, d1)

day_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

week_idx = day_of_the_week.index(week)

if diff < week_idx:
    print(0)
else:
    diff -= week_idx
    print(1 + diff // 7)