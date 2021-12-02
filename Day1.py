import numpy as np
# AoC Day 1 - Part 1

file1 = open("input1a.txt", "r")
depth_list = []
for line in file1:
    depth_list.append(int(line))


def inc_or_dec(num_list: list):
    """The chosen list must be a list of numbers"""
    inc = 0
    dec = 0
    list_j = np.array(num_list[1::])
    list_i = np.array(num_list[0:-1])

    inc_dec_list = list_j - list_i

    for value in inc_dec_list:
        if value > 0:
            inc += 1
        elif value < 0:
            dec += 1
        elif value == 0:
            pass
        else:
            print("error")
    print(f"Number of increases: {inc}\n"
          f"Number of decreases: {dec}\n")


inc_or_dec(depth_list)

# Part 1b
dep_len = len(depth_list)
win_stop = dep_len - 2  # Because a three-measurement sliding window has 2 less than the total numbers.
a, b, c = 0, 1, 2
win_sum = []

for i in range(0, win_stop):
    win_sum.append(depth_list[a] + depth_list[b] + depth_list[c])
    a += 1
    b += 1
    c += 1

inc_or_dec(win_sum)
