import sys

for line in sys.stdin:
    values = list(map(int, line.split()))
    for i in range(0, len(values), 2):
        n, s = values[i], values[i + 1]
        n_for_calc = n + 1  
        ans_calc = s // n_for_calc
        print(ans_calc)
