T = int(input())
num_list = []

for i in range(T):
     num_tuple = tuple(map(int,input().split()))
     num_list.append(num_tuple)

for i in range(T):
     print(num_list[i][0] + num_list[i][1])
