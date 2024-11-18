# 입력 받을 테스트 케이스의 개수
t = int(input())

# 각 테스트 케이스에 대해 점수를 계산
for _ in range(t):
    result = input().strip()  # OX 결과 문자열 입력

    score = 0  # 총 점수
    consecutive_O = 0  # 연속된 O의 개수

    # 결과 문자열을 하나씩 확인하면서 점수 계산
    for char in result:
        if char == 'O':  # 맞춘 경우
            consecutive_O += 1  # 연속된 O의 개수 증가
            score += consecutive_O  # 점수에 추가
        else:  # 틀린 경우
            consecutive_O = 0  # 연속된 O의 개수 초기화

    # 각 테스트 케이스에 대해 점수 출력
    print(score)