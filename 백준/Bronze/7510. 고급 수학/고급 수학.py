import math

n = int(input())

for i in range(1, n + 1):
    # 세 변의 길이 입력받기
    a, b, c = map(int, input().split())
    
    # 가장 긴 변과 나머지 두 변을 찾기
    li_len = sorted([a, b, c])
    a, b, c = li_len[0], li_len[1], li_len[2]
    
    # 피타고라스 정리 확인
    if c == math.sqrt(a ** 2 + b ** 2):
        print(f"Scenario #{i}:")
        print("yes\n")
    else:
        print(f"Scenario #{i}:")
        print("no\n")