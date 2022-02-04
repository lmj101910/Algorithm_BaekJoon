def bfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
            
    return visited

def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
            
    return visited
# 입력
N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# dfs를 위해 역순 정렬
for i in range(len(graph)):
    graph[i].sort(reverse=True)
    
visited = dfs(graph, V)

for i in range(len(visited)):
    print(visited[i], end=' ')

# bfs를 위해 정렬
for i in range(len(graph)):
    graph[i].sort()
    
visited = bfs(graph, V)
print()
for i in range(len(visited)):
    print(visited[i], end=' ')
