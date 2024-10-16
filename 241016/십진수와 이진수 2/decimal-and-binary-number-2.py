n = list(map(int, input()))

def to_digits(n):
    num = 0

    for i in range(len(n)):
        num = num * 2 + n[i]

    return num

def to_binary(n):
    arr = []

    while True:
        if n < 2:
            arr.append(n)
            break

        arr.append(n % 2)
        n = n // 2

    temp = arr[::-1]
    b = ''.join(str(s) for s in temp)

    return b


print(to_binary(to_digits(n) * 17))