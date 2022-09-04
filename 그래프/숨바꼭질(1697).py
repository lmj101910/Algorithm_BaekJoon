import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

location = [0] * (100001)

queue = deque()
queue.append(N)

while queue:
    current_location = queue.popleft()

    if current_location == K:
        print(location[current_location])
        break

    for i in (current_location - 1, current_location + 1,
              current_location * 2):
        if 0 <= i <= 100000 and not location[i]:
            location[i] = location[current_location] + 1
            queue.append(i)
