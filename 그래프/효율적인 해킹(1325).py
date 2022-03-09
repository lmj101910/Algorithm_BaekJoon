from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
  cnt = 1
  queue = deque()
  queue.append(start)
  visit = [False for _ in range(N+1)]
  visit[start] = True
  
  while queue:
    node = queue.popleft()

    for linked_node in Graph[node]:
      if not visit[linked_node]:
        visit[linked_node] = True
        cnt += 1
        queue.append(linked_node)

  return cnt

N, M = map(int, input().split())
Graph = [[] for _ in range(N+1)]
compare_value = 1
result = []

for _ in range(M):
    end, start = map(int, input().split())
    Graph[start].append(end)

for i in range(1, N + 1):
    tmp = bfs(i)
    if compare_value <= tmp:
        if compare_value < tmp:
            result.clear()
        compare_value = tmp
        result.append(i)
          
print(*result)
