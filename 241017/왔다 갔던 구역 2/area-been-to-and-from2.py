def count_overlapping_areas(n, commands):
    position = 0  # 현재 위치
    visited = {}  # 위치별 방문 횟수를 저장할 딕셔너리

    # 각 명령을 처리
    for command in commands:
        x, direction = command.split()
        x = int(x)

        # 방향에 따라 이동 (경로의 모든 지점을 기록)
        if direction == "L":
            for _ in range(x):
                position -= 1
                visited[position] = visited.get(position, 0) + 1
        elif direction == "R":
            for _ in range(x):
                position += 1
                visited[position] = visited.get(position, 0) + 1

    # 2번 이상 방문한 위치의 개수 세기
    result = sum(1 for v in visited.values() if v >= 2)
    
    return result

# 입력 받기
n = int(input())  # 명령의 개수
commands = [input() for _ in range(n)]  # 명령 리스트

# 결과 출력
print(count_overlapping_areas(n, commands))