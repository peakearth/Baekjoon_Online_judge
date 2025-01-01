a, b = map(int, input().split())

m = (b - a) / 400
ans = 1 / (1 + 10**m)

print(ans)