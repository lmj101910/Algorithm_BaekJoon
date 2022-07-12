n = int(input())

result = 0

if n % 400 == 0:
  result = 1
elif n % 4 == 0 and n % 100 != 0:
  result = 1

print(result)
