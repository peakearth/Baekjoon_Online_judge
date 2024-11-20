# 입력받은 문장들을 저장할 리스트
list_of_str = list()  

# 입력 처리
while True:
    # 문장 입력 받기
    input_word = input()
    
    # 종료 조건
    if input_word == "Was it a cat I saw?":  
        break
    
    # 리스트에 문장 추가
    list_of_str.append(input_word)

# 출력 처리

# 줄 번호는 1부터 시작
for i, sentence in enumerate(list_of_str, start=2):  
    # i번째 줄은 i칸 간격으로 문자 선택
    decoded = sentence[::i]  
    print(decoded)