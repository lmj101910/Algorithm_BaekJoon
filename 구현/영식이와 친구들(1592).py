import sys

N, M, L = map(int, sys.stdin.readline().split())
list = [0] * N
index = 0
count = 0

while True:
  if list.count(M) == 1:
    break
  
  list[index] += 1
  count += 1
    
  if list[index] % 2 == 0:
    index = (index - L) % N
  elif list[index] % 2 != 0:
    index = (index + L) % N

print(count-1)
