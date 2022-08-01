import sys
from collections import Counter

N = int(sys.stdin.readline())
num_list = []


for _ in range(N):
  num = int(sys.stdin.readline())
  num_list.append(num)

num_list.sort()

max_list = Counter(num_list).most_common(2)

print(round(sum(num_list)/N))
print(num_list[N//2])
if len(max_list) > 1 and max_list[0][1] == max_list[1][1]:
  print(max_list[1][0])
else:
  print(max_list[0][0])
print(max(num_list)-min(num_list))
