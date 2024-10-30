n = int(input())

def is_beautiful(number):
    # 주어진 숫자가 아름다운 수인지 확인
    i = 0
    length = len(number)
    while i < length:
        count = 1
        while i + 1 < length and number[i] == number[i + 1]:
            count += 1
            i += 1
        if int(number[i]) != count:
            return False
        i += 1
    return True

def count_beautiful_numbers(current):
    # 현재 문자열이 길이 n에 도달했을 때 아름다운 수인지 확인
    if len(current) == n:
        return 1 if is_beautiful(current) else 0
    
    count = 0
    for digit in range(1, 5):
        count += count_beautiful_numbers(current + str(digit))
    return count

# 길이 n의 아름다운 수의 개수 출력
result = count_beautiful_numbers("")
print(result)