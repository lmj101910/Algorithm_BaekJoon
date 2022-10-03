import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

m, n, h = map(int, input().split())
tomato = [[list(map(int,
                    input().split())) for i in range(n)] for depth in range(h)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append([i, j, k])

while queue:
    z, y, x = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1
                queue.append([nz, ny, nx])

check = 1
day = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                check = 0
            day = max(day, tomato[i][j][k])

if check == 0:
    print(-1)
else:
    print(day - 1)
