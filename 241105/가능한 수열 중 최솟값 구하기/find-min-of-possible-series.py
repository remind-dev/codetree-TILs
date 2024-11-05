n = int(input())

def is_valid(seq):
    cont_n = len(seq) // 2
    for i in range(1, cont_n + 1):
        if seq[-i:] == seq[-2 * i:-i]:  # 최근 추가한 부분만 검사
            return False
    return True

def backtrack(cnt):
    global ans

    if cnt == n:
        print("".join(map(str, seq)))  # 가능한 수열을 찾았으면 출력
        return True  # 정답을 찾았으므로 종료
    
    for i in range(4, 7):  # 사전순으로 가장 앞선 수열을 찾기 위해 4, 5, 6 순서로 시도
        seq.append(i)
        if is_valid(seq):  # 유효성 검사 후 백트래킹 진행
            if backtrack(cnt + 1):  # 정답을 찾았으면 더 이상 탐색하지 않음
                return True
        seq.pop()  # 다음 숫자를 추가하기 전 상태로 복구
    
    return False

seq = []
backtrack(0)