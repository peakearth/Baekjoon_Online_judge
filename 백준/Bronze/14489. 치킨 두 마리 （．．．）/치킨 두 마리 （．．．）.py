a, b = map(int, input().split())
c = int(input())

sum_ab = a + b
c_2 = c * 2

if sum_ab >= c_2:
    print(sum_ab - c_2)
else:
    print(sum_ab)