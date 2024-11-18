# 정의
def calc_at_mars(expression):
    result = float(expression[0])
    
    for i in range(1, len(expression)):
        if expression[i] == '@':
            result *= 3
        elif expression[i] == '%':
            result += 5
        elif expression[i] == '#':
            result -= 7
    
    return f"{result:.2f}"

# 입력
t = int(input())
for _ in range(t):
    inp = input().split()
    print(calc_at_mars(inp))