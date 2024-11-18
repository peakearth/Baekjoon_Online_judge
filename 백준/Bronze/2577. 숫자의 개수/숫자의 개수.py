A = int(input())
B = int(input())
C = int(input())

calc_result = str(A * B * C)

# 0부터 9까지 숫자의 개수를 계산
for i in range(10):
    print(calc_result.count(str(i)))