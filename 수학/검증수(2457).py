n = list(map(int,input().split()))

check_num = 0

for i in range(len(n)):
  check_num += (n[i] ** 2)

check_num %= 10

print(check_num)
