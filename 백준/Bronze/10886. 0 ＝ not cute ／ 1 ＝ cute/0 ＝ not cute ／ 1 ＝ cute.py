n = int(input())
list_ans = list()

for i in range(n):
    ans = int(input())
    list_ans.append(ans)

neg = list_ans.count(0)
pos = list_ans.count(1)

if neg > pos:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")