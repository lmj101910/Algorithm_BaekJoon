import sys

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [0 for _ in range(N)]


def dfs(start):
    for i in range(N):
        if graph[start][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0 for _ in range(N)]
