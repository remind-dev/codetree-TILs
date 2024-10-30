# 입력 받기
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
segments.sort()  # 시작점을 기준으로 정렬하여 탐색 시 효율성을 높임

max_count = 0  # 최대 개수를 저장할 변수

def is_non_overlapping(selected_segments, new_segment):
    # 새로운 선분이 현재 선택된 선분들과 겹치지 않는지 확인
    for x1, x2 in selected_segments:
        y1, y2 = new_segment
        # 겹치는지 확인: 끝점이 겹치거나 교차하면 겹침
        if not (x2 <= y1 or y2 <= x1):
            return False
    return True

def backtrack(index, selected_segments):
    global max_count
    # 선택된 선분의 개수로 최대 개수 갱신
    max_count = max(max_count, len(selected_segments))

    # 모든 선분을 다 확인했다면 종료
    if index == n:
        return
    
    
    # 현재 선분을 포함하는 경우 (겹치지 않는다면)
    current_segment = segments[index]
    if is_non_overlapping(selected_segments, current_segment):
        selected_segments.append(current_segment)
        backtrack(index + 1, selected_segments)
        selected_segments.pop()  # 선택 해제 (백트래킹)

# 백트래킹 시작
backtrack(0, [])
print(max_count)