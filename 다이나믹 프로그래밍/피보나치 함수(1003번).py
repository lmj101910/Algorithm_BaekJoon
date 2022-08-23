import sys

c0 = [1,0]
c1 = [0,1]


def fibonacci(N):
  length = len(c0)
  if len(c0) <= N:
    for i in range(length, N+1):
      c0.append(c0[-1] + c0[-2])
      c1.append(c1[-1] + c1[-2])
      


T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())

  fibonacci(N)
  if N == 0:
    print(1, 0)
  elif N == 1:
    print(0, 1)
  else:
    print(c0[-1], c1[-1])
  
  c0 = [1, 0]
  c1 = [0, 1]
