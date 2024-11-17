# 입력값 받기
numbers = list(map(int, input().split()))

# 각 숫자를 제곱한 후 합 구하기
sum_of_squares = sum(x ** 2 for x in numbers)

# 10으로 나눈 나머지 계산
verification_number = sum_of_squares % 10

# 결과 출력
print(verification_number)