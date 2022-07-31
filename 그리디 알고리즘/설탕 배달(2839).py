import sys

N = int(sys.stdin.readline())
count = 0

while N%5 != 0:
  N -= 3
  count += 1
  if N < 3:
    break

count += (N//5)
N = N%5

if N != 0:
  print(-1)
else:
  print(count)
