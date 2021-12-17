import numpy as np
# AoC Day 6 - Part 1

file1 = open("input7.txt", "r")
nums = []
for line in file1:
    x = line.split(",")
    map_nums = map(int, x)
    nums = list(map_nums)
num_max = max(nums)


fuel = []
for i in range(1, num_max + 1):
    temp = []
    for num in nums:
        # update fuel list with difference in position
        # sum fuel list
        f = abs(num - i)
        temp.append(f)
    fuel.append(sum(temp))

f_min = min(fuel)
f_index = fuel.index(f_min) + 1

print(f"--- Part 1a ---\n"
      f"The lowest fuel is at position {f_index} and the amount of fuel used is: {f_min}\n")

# --- Part 2 ---


def consecutive_sum(num_int, first_num, last_num):
    """finds the sum of a set of consecutive numbers using
    the number of integers - num_int, the first number - first_num
    and the last number - last_num"""
    s = (num_int/2)*(first_num + last_num)
    return s


fuel = []
for i in range(1, num_max + 1):
    temp = []
    for num in nums:
        diff = abs(i - num)
        f = consecutive_sum(diff, 1, diff)
        temp.append(f)
    fuel.append(sum(temp))

f_min = int(min(fuel))
f_index = fuel.index(f_min) + 1

print(f"--- Part 1b ---\n"
      f"The lowest fuel is at position {f_index} and the amount of fuel used is: {f_min}\n")
