import sys
import math

num = int(sys.stdin.readline())

fac_num = list(str(math.factorial(num)))
count = 0

for i in range(len(fac_num) - 1, -1, -1):
    if fac_num[i] == '0':
        count += 1
    else:
        break

print(count)
