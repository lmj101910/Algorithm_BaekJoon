import collections

#string1 = list(map(str, input().split()))
string1 = input()
string1 = list(string1.upper())
#print(string1)

Max_list = []
count = 0

dict = collections.Counter(string1)
#print(dict)

for k in dict.keys():
  if count < dict[k]:
    Max_list.clear()
    Max_list.append(k)
    count = dict[k]
  elif count == dict[k]:
    Max_list.append(k)

#print(count_list)

if len(Max_list) == 1:
  print(Max_list[0])
else:
  print('?')
