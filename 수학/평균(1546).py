n = int(input())
subject = list(map(int,input().split()))

max_score = max(subject)
result = 0

for i in range(n):
  result += subject[i]

result = result / (n * max_score) * 100 

print(result)
