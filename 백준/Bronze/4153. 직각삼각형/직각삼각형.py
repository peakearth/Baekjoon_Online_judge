while True:
    try:
        a, b, c = map(int, input().split())
        
        if a == 0 and b == 0 and c == 0:
            break
        
        sides = [a, b, c]
        sides.sort()
        
        # 직각 삼각형 검사: 작은 두 변의 제곱합이 가장 큰 변의 제곱과 같으면 직각삼각형
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            print('right')
        else:
            print('wrong')
            
    except ValueError:
        # 값이 잘못 입력된 경우 (예: 정수가 아닌 경우)
        print("Invalid input")