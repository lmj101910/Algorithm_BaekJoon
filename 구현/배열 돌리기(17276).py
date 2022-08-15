import sys

def roll(n, d, array):
  if d < 0:
    d = (d+360)//45
  else:
    d = d//45

  for _ in range(d):
    temp = []
    
    for j in range(n):  temp.append(array[j][j])
    for j in range(n):  array[j][j] = array[((n+1)//2)-1][j]
    for j in range(n):  array[((n+1)//2)-1][j] = array[n-1-j][j]
    for j in range(n):  array[j][n-1-j] = array[j][((n+1)//2)-1]
    for j in range(n):  array[j][((n+1)//2)-1] = temp[j]

  for i in array:
    for j in i:
      print(j, end=' ')
    print()
      

T = int(sys.stdin.readline())

for _ in range(T):
  n, d = map(int,sys.stdin.readline().split())
  array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

  # print(array)
  roll(n, d, array)
