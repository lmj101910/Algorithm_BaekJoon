import sys

N = int(sys.stdin.readline())
hand = sorted(list(map(int,sys.stdin.readline().split())))
M = int(input())
check_list = list(map(int, sys.stdin.readline().split()))
count = {}

for i in hand:
  if i in count:
    count[i] += 1
  else:
    count[i] = 1

def binarySearch(arr, target, start, end):
  if start > end:
    return 0

  mid = (start + end) // 2
  
  if arr[mid] == target:
    return count.get(target)
  elif arr[mid] < target:
    return binarySearch(arr, target, mid+1, end)
  else:
    return binarySearch(arr, target, start, mid-1)

for target in check_list:
  print(binarySearch(hand, target, 0, len(hand)-1), end=' ')
