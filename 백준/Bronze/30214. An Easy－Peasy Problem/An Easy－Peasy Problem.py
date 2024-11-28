solved_front, solved_final = map(int, input().split())

if solved_front >= (solved_final + 1) // 2:
    print('E')
else:
    print('H')