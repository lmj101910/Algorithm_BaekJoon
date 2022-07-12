n = input()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(alphabet)):
  for j in range(len(n)):
    if alphabet[i] == n[j]:
      alphabet[i] = j
      break
    if j == (len(n)-1) and alphabet[i] != n[j]:
      alphabet[i] = '-1'

for i in alphabet:
  print(i, end = ' ')
  
  """
S = input()
arr = []
for i in range(26):
    arr.append(-1)
for i in range(len(S)):
    if arr[ord(S[i]) - 97] == -1:
        arr[ord(S[i]) - 97] = i
for i in arr:
    print(i, end = ' ')
    
 
S = input()
arr = list(range(97, 123))

for i in arr:
    print(S.find(chr(i)))
    
출처 : https://afterdawncoding.tistory.com/56
  """
