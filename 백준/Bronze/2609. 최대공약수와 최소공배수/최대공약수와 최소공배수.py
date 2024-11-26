import math

num_1, num_2 = map(int, input().split())

gcd = math.gcd(num_1, num_2)
lcm = math.lcm(num_1, num_2)

print(gcd)
print(lcm)