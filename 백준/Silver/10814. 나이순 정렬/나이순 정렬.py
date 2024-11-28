n = int(input())
members = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    members.append((age, name, i))

sorted_members = sorted(members, key=lambda x: (x[0], x[2]))

for age, name, _ in sorted_members:
    print(age, name)