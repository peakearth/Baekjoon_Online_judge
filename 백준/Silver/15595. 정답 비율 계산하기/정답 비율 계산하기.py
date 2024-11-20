# 입력 처리
n = int(input())

# 데이터 저장
user_attempts = {}  # 사용자별 틀린 횟수 기록
correct_users = set()  # 문제를 맞힌 사용자 기록

for _ in range(n):
    # 입력 파싱
    num_id, user_id, result, memory, time, lang, len_of_code = input().split()
    result = int(result)

    # 관리자의 제출 무시
    if user_id == "megalusion":
        continue

    # 사용자별 틀린 횟수 추적
    if user_id not in user_attempts:
        user_attempts[user_id] = 0

    if result == 4:  # 정답 제출
        correct_users.add(user_id)
    else:  # 오답 제출
        if user_id not in correct_users:  # 이미 맞힌 사람은 틀린 횟수 추가 안 함
            user_attempts[user_id] += 1

# 문제를 맞힌 사용자 수와 틀린 횟수 합산
correct_count = len(correct_users)
total_wrong_attempts = sum(user_attempts[user] for user in correct_users)

# 정답 비율 계산
if correct_count == 0:
    answer_rate = 0.0
else:
    answer_rate = (correct_count / (correct_count + total_wrong_attempts)) * 100

# 결과 출력
print(answer_rate)