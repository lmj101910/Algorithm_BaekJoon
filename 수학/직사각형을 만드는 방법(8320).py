import sys

n = int(sys.stdin.readline())

count = 0
for i in range(1, int(n**0.5)+1):
    for j in range(i, n+1):
        if i * j <= n:
          count += 1
print(count)
