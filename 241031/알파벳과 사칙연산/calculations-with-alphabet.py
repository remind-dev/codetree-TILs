from itertools import product

def calculate_expression(expression, values):
    # 현재 알파벳에 값 할당
    expr = ""
    index = 0
    for ch in expression:
        if 'a' <= ch <= 'f':
            expr += str(values[ord(ch) - ord('a')])
        else:
            expr += ch
    
    # 연산자가 모두 같은 우선순위를 가지므로 순서대로 계산
    result = int(expr[0])
    i = 1
    while i < len(expr):
        operator = expr[i]
        operand = int(expr[i + 1])
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        i += 2
    return result

def find_max_expression_value(expression):
    max_value = -float('inf')
    
    # 각 알파벳을 1부터 4까지 할당
    for values in product(range(1, 5), repeat=6):
        result = calculate_expression(expression, values)
        max_value = max(max_value, result)
    
    return max_value

# 입력 예시
expression = input().strip()
print(find_max_expression_value(expression))