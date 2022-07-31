import sys

K = int(sys.stdin.readline())
stack= []
for i in range(K):
  num = int(sys.stdin.readline())
  if len(stack) != 0 and num == 0:
    stack.pop()
  elif num != 0:
    stack.append(num)

print(sum(stack))
