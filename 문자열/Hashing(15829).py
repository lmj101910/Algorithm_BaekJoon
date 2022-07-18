n = int(input())
alphabet = list(input())

result = 0

for i in range(len(alphabet)):
  result += ((ord(alphabet[i])-96) * (31**i))

print(result % 1234567891)
