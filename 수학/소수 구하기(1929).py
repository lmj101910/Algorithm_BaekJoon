import sys
N, K = map(int, sys.stdin.readline().split())

for i in range(N, K+1):
  count = 0
  if i == 1:
    continue
  for j in range(2, int(i**0.5)+1):
      if (i % j) == 0:
        count += 1
        break
  if count == 0:
    print(i)
