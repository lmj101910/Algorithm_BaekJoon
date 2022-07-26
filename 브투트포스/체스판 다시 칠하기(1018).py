N, M = map(int, input().split())
count = []
chess = []

for _ in range(N):
  chess.append(input())

for i in range(N-7):
  for j in range(M-7):
    start_black = 0
    start_white = 0
    for k in range(i, i+8):
      for l in range(j, j+8):
        if(k + l) % 2 == 0:
          if chess[k][l] == 'W':
            start_black += 1
          if chess[k][l] == 'B':
            start_white += 1
        else:
          if chess[k][l] != 'W':
            start_black += 1
          if chess[k][l] != 'B':
            start_white += 1
    count.append(start_black)
    count.append(start_white)

print(min(count))
