n = int(input())

result = 'F'

if n >= 90 and n <= 100:
  result = 'A'
elif n >= 80 and n <= 89:
  result = 'B'
elif n >= 70 and n <= 79:
  result = 'C'
elif n >= 60 and n <= 69:
  result = 'D'

print(result)
