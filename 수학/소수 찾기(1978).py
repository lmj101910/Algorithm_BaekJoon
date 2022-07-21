n = int(input())

num = map(int,input().split())
count = 0

for i in num:
  check = 0
  if i > 1:
    for j in range(2, i):
      if i % j == 0:
        check += 1
        break
    if check == 0:
      count += 1

print(count)
