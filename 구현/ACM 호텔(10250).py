T = int(input())

for i in range(T):
  H, W, N = map(int, input().split())

  Room_num = (N // H) + 1
  Floor = N % H

  if Floor == 0:
    Room_num = N // H
    Floor = H

  print(Floor*100+Room_num)
