import math

n = int(input())
i = 1

for i in range(n):
    # 리스트 초기화
    li_len = list()
    i += 1
    
    # 값 입력받기
    a, b, c = map(int, input().split())
    li_len.append(a)
    li_len.append(b)
    li_len.append(c)
    
    # 리스트 sort
    li_len.sort()
    
    # 계산 & 출력
    if li_len[2] == math.sqrt((li_len[0] ** 2) + (li_len[1]) ** 2):
        print(f'Scenario #{i}:')
        print('yes')
        print()
    
    else:
        print(f'Scenario #{i}:')
        print('no')
        print()
    
    i += 1