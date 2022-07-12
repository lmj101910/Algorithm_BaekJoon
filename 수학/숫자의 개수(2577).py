A = int(input())
B = int(input())
C = int(input())

mul = A * B * C

mul = list(str(mul))
mul.sort()

num_count_list = []
count = 0

for i in range(10):
  for j in range(len(mul)):
    if i == int(mul[j]):
      count += 1
  num_count_list.append(count)
  count = 0
    
for i in range(len(num_count_list)):
  print(num_count_list[i])
