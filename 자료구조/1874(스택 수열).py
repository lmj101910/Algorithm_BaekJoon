n = int(input())

count = 1
stack = []
result = []
allow = 1

for i in range(n):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        allow = 0
        break

if allow == 1:
    print('\n'.join(result))
   
############# exit 사용 풀이 #############

#n = int(input())

#count = 1
#stack = []
#result = []

#for i in range(n):
#    data = int(input())
#    while count <= data:
#        stack.append(count)
#        count += 1
#        result.append('+')
#    if stack[-1] == data:
#        stack.pop()
#        result.append('-')
#    else:
#        print('NO')
#        exit(0)
        
#print('\n'.join(result))
