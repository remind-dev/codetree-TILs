m1, d1, m2, d2 = map(int, input().split())

def cal_day(m, d):
    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total = 0

    for i in range(1, m):
        total += num_of_days[i]

    return total + d

diff_day = cal_day(m2, d2) - cal_day(m1, d1)

day_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

while diff_day < 0:
    diff_day += 7

print(day_of_the_week[diff_day % 7])