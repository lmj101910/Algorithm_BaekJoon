import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0


def paper_cutting(x, y, N):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                paper_cutting(x, y, N//2)
                paper_cutting(x, y+N//2, N//2)
                paper_cutting(x+N//2, y, N//2)
                paper_cutting(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


paper_cutting(0, 0, N)
print(white)
print(blue)
