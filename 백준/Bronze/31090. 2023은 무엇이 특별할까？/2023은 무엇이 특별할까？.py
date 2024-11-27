t = int(input()) 

for _ in range(t):
    n = int(input())            
    last_two_digits = n % 100
    next_year = n + 1

    # 조건 확인
    if next_year % last_two_digits == 0:
        print("Good")
    else:
        print("Bye")