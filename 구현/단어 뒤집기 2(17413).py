import sys

sentence = sys.stdin.readline().rstrip()

flag = False
word = ''
for i in range(len(sentence)):
  if sentence[i] == '<':
    print(word[::-1], end='')
    word = ''
    flag = True
    word += sentence[i]
  elif sentence[i]=='>':
    flag = False
    word += sentence[i]
    print(word, end='')
    word = ''
  elif i != '<' or i != '>':
    if sentence[i] == ' ' and flag == False:
      print(word[::-1], end=' ')
      word = ''
    else:
      word += sentence[i]
    
  if i == len(sentence) - 1:
    print(word[::-1])
