import sys

N = int(sys.stdin.readline())

for i in range(N):
  count = 0
  ps = list(input())
  for j in ps:
    if j == '(':
      count += 1
    elif j == ')':
      count -= 1
    if count < 0:
      print('NO')
      break

  if count == 0:
    print('YES')
  elif count > 0:
    print('NO')
