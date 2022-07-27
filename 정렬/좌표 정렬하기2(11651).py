import sys

N = int(sys.stdin.readline())
coordinate = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

coordinate.sort(key=lambda x:(x[1],x[0]))

for i in range(N):
  print(coordinate[i][0], coordinate[i][1])
