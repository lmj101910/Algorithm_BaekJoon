n = int(input())

for i in range(n):
  result = 0
  count = 1
  answer = input()

  for i in range(len(answer)):
    if answer[i] == 'O':
      result += count
      count += 1
    else:
      count = 1

    if i == len(answer) - 1:
      print(result)
