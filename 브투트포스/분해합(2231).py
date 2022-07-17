num = int(input())

init_num = 0

while True:
  
  if num < init_num:
    print(0)
    break

  digit = list(str(init_num))
  result = init_num
  
  for i in range(len(digit)):
    result += int(digit[i])
  
  if num == result:
    print(init_num)
    break
  
  init_num += 1
