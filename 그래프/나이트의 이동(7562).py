from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

def bfs(start_x, start_y, target_x, target_y):
  
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    queue = deque()
    queue.append((start_x, start_y))
    
    while queue:
        x, y = queue.popleft()
      
        if x == target_x and y == target_y:
            return chess[target_x][target_y]
        
        for i in range(8):
            moved_x = x + dx[i]
            moved_y = y + dy[i]
          
            if 0 <= moved_x < size and 0 <= moved_y < size:
                if chess[moved_x][moved_y] == 0:
                    queue.append((moved_x, moved_y))
                    chess[moved_x][moved_y] = chess[x][y] + 1
        

for _ in range(n):
    size = int(input())
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    chess = [[0] * size for _ in range(size)]
    print(bfs(start_x, start_y, target_x, target_y))
