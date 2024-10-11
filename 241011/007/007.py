# 변수 선언 및 입력
s_code, m_point, given_time = tuple(input().split())

# tuple 생성
s = (s_code, m_point, int(given_time))

# tuple 원소들을 각 변수에 대입
secret_code, meeting_point, time = s

# 출력
print(f"secret code : {secret_code}")
print(f"meeting point : {meeting_point}")
print(f"time : {time}")