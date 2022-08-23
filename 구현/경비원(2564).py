import sys


def distance(x, y):
    if x == 1:
        return y
    elif x == 2:
        return w + h + w - y
    elif x == 3:
        return w + h + w + h - y
    elif x == 4:
        return w + y


w, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

dist = []
count = 0

for _ in range(n+1):
    x, y = map(int, sys.stdin.readline().split())
    dist.append(distance(x, y))

for i in range(n):
    clockwise = abs(dist[-1] - dist[i])
    counter_clockwise = 2*(w+h) - clockwise
    count += min(clockwise, counter_clockwise)

print(count)
