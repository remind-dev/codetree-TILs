n = int(input())

answer = []

def is_beautiful(number):
    i = 0
    length = len(number)
    while i < length:
        count = 1
        while i + 1 < length and number[i] == number[i+1]:
            if count == number[i]:
                break

            count += 1
            i += 1

        if count != number[i]:
            return False
        i += 1

    return True

def beutiful_num(cnt):
    if cnt == n:
        return 1 if is_beautiful(answer) else 0
    
    count = 0
    for digit in range(1, 5):
        answer.append(digit)
        count += beutiful_num(cnt+1)
        answer.pop() 

    return count

print(beutiful_num(0))