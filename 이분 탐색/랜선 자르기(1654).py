import sys
N, K = map(int, sys.stdin.readline().split())
lan = []

for _ in range(N):
  l = int(sys.stdin.readline())
  lan.append(l)

start = 1
end = max(lan)

while start <= end:
  count = 0
  mid = (start + end) // 2

  for i in range(N):
    count += (lan[i]//mid)

  if count >= K:
    start = mid + 1
  elif count < K:
    end = mid - 1

print(end)
