import sys


def switch_light(index):
    if switch[index] == 0:
        switch[index] = 1
    elif switch[index] == 1:
        switch[index] = 0
    return


num_switch = int(sys.stdin.readline())
switch = [0] + list(map(int, sys.stdin.readline().split()))
num_student = int(sys.stdin.readline())

for _ in range(num_student):
    gender, index = map(int, sys.stdin.readline().split())

    if gender == 1:
        for i in range(index, num_switch + 1, index):
            #print(index, switch[index])
            switch_light(i)
    elif gender == 2:
        switch_light(index)
        for i in range(1, len(switch) // 2):
            if index - i > 0 and index + i < len(switch):
                if switch[index - i] == switch[index + i]:
                    switch_light(index - i)
                    switch_light(index + i)
                else:
                    break

for i in range(1, len(switch)):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
