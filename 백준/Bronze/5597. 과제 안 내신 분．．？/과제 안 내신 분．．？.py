list_num = list(range(1, 31))

for i in range(28):
    a = int(input())
    list_num.remove(a)

print(min(list_num))
print(max(list_num))