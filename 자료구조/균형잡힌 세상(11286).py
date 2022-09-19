import sys
import heapq

num = int(sys.stdin.readline())
heap_queue = []

for i in range(num):
    operate = int(sys.stdin.readline())

    if operate != 0:
        heapq.heappush(heap_queue, (abs(operate), operate))
    else:
        if not heap_queue:
            print(0)
        else:
            print(heapq.heappop(heap_queue)[1])
