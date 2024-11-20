# 1. 입력받을 코드의 열 입력
c = int(input())

list_code = []
max_count = 0

# 2. c개의 줄에 걸쳐서 코드를 입력받기
for i in range(c):
    # 문자열로 입력 받기
    code = input()
    list_code.append(code)

# 3. 각 줄에서 "for"와 "while"의 최대 개수를 계산
for code in list_code:
    # "for"와 "while"이 몇 번 나오는지 세기
    count_for = code.count("for")
    count_while = code.count("while")
    
    # 같은 줄에서의 반복문의 합
    total_count = count_for + count_while
    
    # 최대값 갱신
    if total_count > max_count:
        max_count = total_count

# 4. 출력
print(max_count)