import sys

n = int(sys.stdin.readline())
people = []

for i in range(n):
  age, name = sys.stdin.readline().split()
  people.append((int(age), name))

people.sort(key=lambda x:x[0])

for i in range(len(people)):
  print(people[i][0], people[i][1])
