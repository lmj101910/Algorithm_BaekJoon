from collections import deque

def bfs(x, y):
    # 방향
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            moved_x = x + dx[i]
            moved_y = y + dy[i]
            
            if 0 <= moved_x < h and 0 <= moved_y < w:
                if graph[moved_x][moved_y] == 1 and visited[moved_x][moved_y] == False:
                    visited[moved_x][moved_y] = True
                    queue.append((moved_x, moved_y))
                    
while True:
    w, h = map(int, input().split())  
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    island_count = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                island_count += 1
    print(island_count)
