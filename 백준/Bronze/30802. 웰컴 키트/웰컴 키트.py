# 입력 받기
N = int(input())  # 참가자 수
S, M, L, XL, XXL, XXXL = map(int, input().split())  # 티셔츠 사이즈별 신청 수
T, P = map(int, input().split())  # 티셔츠와 펜의 묶음 크기

# 티셔츠 주문 계산
# 각 사이즈별로 필요한 묶음 수를 계산하고 합산
total_shirts = S + M + L + XL + XXL + XXXL
shirts_bundles = 0
for count in [S, M, L, XL, XXL, XXXL]:
    shirts_bundles += -(-count // T)  # 올림 계산

# 펜 주문 계산
pens_bundles = N // P  # 펜 묶음으로 최대 주문 가능한 개수
remaining_pens = N % P  # 묶음으로 주문한 후 남는 펜 개수

# 결과 출력
print(shirts_bundles)  # 티셔츠 묶음 수
print(pens_bundles, remaining_pens)  # 펜 묶음 수와 남는 펜 개수
