# 입력 받기
n = int(input())

# DP 테이블 초기화
dp = [0] * (n + 1)

# 점화식에 따라 DP 계산
for i in range(2, n + 1):
    # 기본적으로 1을 뺀 경우
    dp[i] = dp[i - 1] + 1
    
    # 2로 나누어 떨어지면 최소값 갱신
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    # 3으로 나누어 떨어지면 최소값 갱신
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# 결과 출력
print(dp[n])