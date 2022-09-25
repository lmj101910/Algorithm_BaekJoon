import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [[0] * N for _ in range(N)]

def bfs(start):
    queue = deque()
    queue.append(start)
    check = [0 for _ in range(N)]

    while queue:
        node = queue.popleft()

        for i in range(N):
            if check[i] == 0 and graph[node][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[start][i] = 1

for i in range(0, N):
    bfs(i)

for i in visited:
    print(*i)
