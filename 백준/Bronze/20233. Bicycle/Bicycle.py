# 입력 받기
a = int(input())  # 첫 번째 요금제의 월 요금
x = int(input())  # 첫 번째 요금제의 추가 시간당 비용
b = int(input())  # 두 번째 요금제의 월 요금
y = int(input())  # 두 번째 요금제의 추가 시간당 비용
T = int(input())  # 하루 동안 자전거 이용 시간 (분)

# 첫 번째 요금제 계산
extra_time_1 = max(0, T - 30)
cost_option_1 = a + extra_time_1 * x * 21

# 두 번째 요금제 계산
extra_time_2 = max(0, T - 45)
cost_option_2 = b + extra_time_2 * y * 21

# 결과 출력
print(cost_option_1, cost_option_2)
