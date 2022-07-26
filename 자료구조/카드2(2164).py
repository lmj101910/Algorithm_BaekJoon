from collections import deque

N = int(input())

queue = deque()

for i in range(1, N+1):
  queue.append(i)

while True:
  if len(queue) == 1:
    print(queue[0])
    break
  queue.popleft()
  index = queue.popleft()
  queue.append(index)
