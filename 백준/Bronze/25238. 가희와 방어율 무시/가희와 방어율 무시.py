a, b = map(int, input().split())

a_percent = a * b/100
fin_a = a - a_percent

if fin_a >= 100:
    print('0')
else:
    print('1')