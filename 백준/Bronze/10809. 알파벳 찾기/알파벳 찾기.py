# 입력받기
S = input()  

# 알파벳 소문자 리스트 생성 (a부터 z까지)
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# 각 알파벳의 처음 등장 위치를 저장할 리스트 생성
positions = []

# 각 알파벳에 대해 위치 찾기
for char in alphabet:
    if char in S:
        positions.append(S.index(char))  # 단어에서의 첫 번째 등장 위치
    else:
        positions.append(-1)  # 단어에 없는 경우 -1 추가

# 결과 출력
print(" ".join(map(str, positions)))