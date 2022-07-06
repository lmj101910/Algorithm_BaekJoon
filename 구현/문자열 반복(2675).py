n = int(input())
repeat_list = []

for _ in range(n):
  repeats = tuple(input().split())

  repeat_list.append(repeats)

for i in range(n):
  for j in range(len(repeat_list[i][1])):
    print(repeat_list[i][1][j] * int(repeat_list[i][0]), end='')
    if j == len(repeat_list[i][1]) - 1:
      print()
