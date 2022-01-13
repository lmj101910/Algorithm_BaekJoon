n = int(input())
atm_list = list(map(int,input().split()))
atm_list.sort()
time = 0
for i in range(len(atm_list)):
    for j in range(i+1):
        time += atm_list[j]

print(time)
