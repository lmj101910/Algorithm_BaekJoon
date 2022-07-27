import sys

N = int(sys.stdin.readline())
people = []
rank = []
for _ in range(N):
  weight, height = map(int, sys.stdin.readline().split())
  people.append([weight, height])

for i in range(N):
  count = 1
  for j in range(N):
    if (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]):
      count += 1
  rank.append(count)

for i in range(N):
  print(rank[i])
