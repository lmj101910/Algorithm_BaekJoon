import sys

N, M, B = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time = 100000000000000000

for target in range(257):
  max_target, min_target = 0, 0

  for i in range(N):
    for j in range(M):

      if land[i][j] >= target:
        max_target += land[i][j] - target

      else:
         min_target += target - land[i][j]
 

  if max_target + B >= min_target:
    if min_target + (max_target * 2) <= time:
      time = min_target + (max_target * 2)
      floor = target

print(time, floor)
