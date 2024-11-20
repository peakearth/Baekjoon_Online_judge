n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            current_sum = cards[i] + cards[j] + cards[k]
            if current_sum <= m and current_sum > max_sum:
                max_sum = current_sum

print(max_sum)