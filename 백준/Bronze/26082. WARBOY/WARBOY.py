# 입력
a, b, c = map(int, input().split())

# 계산
# 경쟁사 제품의 가성비
calc_other = b // a

# WARBOY의 가성비
calc_warboy = calc_other * 3

# WARBOY의 성능
effect = calc_warboy * c

# 출력
print(effect)
