import sys

N, M = map(int, sys.stdin.readline().split())

tree_list = [int(x) for x in sys.stdin.readline().split()]

def binary(max_value, M, tree_list):
  start = 0
  end = max_value

  while start <= end:
    count = 0
    middle = (start + end) // 2

    for tree in tree_list:
      if tree >= middle:
        count +=  tree - middle

    if count >= M:
      start = middle + 1
    elif count < M:
      end = middle - 1

  print(end)

binary(max(tree_list), M, tree_list)
