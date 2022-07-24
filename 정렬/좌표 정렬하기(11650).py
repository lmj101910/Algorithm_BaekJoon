import sys

N = int(sys.stdin.readline())

coordinate = list()

for _ in range(N):
  x, y = map(int, sys.stdin.readline().split())
  coordinate.append([x, y])

coordinate.sort(key=lambda x:(x[0], x[1]))

for i in range(N):
  print(coordinate[i][0], coordinate[i][1])
