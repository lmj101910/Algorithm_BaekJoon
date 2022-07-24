import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())

y_list = deque()
answer = deque()
index = 0

for i in range(1, N+1):
  y_list.append(i)


while y_list:
  index = (index + K -1) % len(y_list)
  answer.append(y_list[index])
  y_list.remove(y_list[index])
  
sys.stdout.write('<' + ", ".join(map(str,answer)) + '>')
