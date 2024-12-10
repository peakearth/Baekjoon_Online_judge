import sys

input = sys.stdin.readline

N, K = map(int, input().split())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# 조합 공식 nCk = n!/(n-k)!k!
print(factorial(N) // (factorial(N-K) * factorial(K)))