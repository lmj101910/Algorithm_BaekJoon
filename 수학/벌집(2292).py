n = int(input())

count = 1
fold = 1
hexa = 1

while n > hexa :
  hexa += 6 * fold
  fold += 1
  count += 1

print(count)
