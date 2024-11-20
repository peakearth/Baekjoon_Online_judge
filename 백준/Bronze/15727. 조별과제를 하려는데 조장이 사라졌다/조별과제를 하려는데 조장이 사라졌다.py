# 입력
distance = int(input())

# 5로 나눈 몫과 나머지 계산
minutes = distance // 5
if distance % 5 != 0:  # 나머지가 있으면 1분 추가
    minutes += 1

# 결과 출력
print(minutes)