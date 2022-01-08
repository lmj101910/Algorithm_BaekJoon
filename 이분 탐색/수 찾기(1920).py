from sys import stdin
N = stdin.readline()
N_list = sorted(map(int,stdin.readline().split()))
M = stdin.readline()
M_list = list(map(int, stdin.readline().split()))
             
def binary_search(target):
    start = 0
    end = int(N) - 1
    
    while start <= end:
        median = (start + end) // 2
        if N_list[median] == target:
            return 1
        
        if target < N_list[median]:
            end = median - 1
        elif target > N_list[median]:
            start = median +1
    if start > end:
        return 0
                  
for i in range(int(M)):
    print(binary_search(M_list[i]))
