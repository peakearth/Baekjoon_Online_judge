n = int(input())
list_xy = list()

for i in range(n):
    x, y = map(int, input().split())
    list_xy.append([x, y])

fin_xy = sorted(list_xy, key=lambda point: (point[1], point[0]))

for x, y in fin_xy:
    print(x, y)