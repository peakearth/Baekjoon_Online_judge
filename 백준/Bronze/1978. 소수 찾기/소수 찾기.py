def is_prime(num):
    # 입력된 수가 소수인지 아닌지 판단하는 함수
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))

# 소수의 개수 계산
prime_count = sum(1 for num in numbers if is_prime(num))

# 결과 출력
print(prime_count)