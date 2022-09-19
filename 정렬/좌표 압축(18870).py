import sys

times = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
answer_dict = {}

numset = set(num_list)
num_list_sorted = list(numset)
num_list_sorted.sort()

for i in range(len(num_list_sorted)):
    answer_dict[num_list_sorted[i]] = i

for i in num_list:
    print(answer_dict[i], end=' ')
