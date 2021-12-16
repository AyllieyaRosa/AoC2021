import numpy as np
# AoC Day 5 - Part 1

file1 = open("input6.txt", "r")
nums = []
for line in file1:
    x = line.split(",")
    map_nums = map(int, x)
    nums = list(map_nums)

# each iteration decrease by 1, if number is 0 becomes 6 and adds 8 to end of list
days = 80
res = nums.copy()
while days > 0:
    for i in range(0, len(res)):
        if res[i] != 0:
            res[i] = res[i] - 1
        else:
            res[i] = 6
            res.append(8)
    days -= 1
    if days == 0:
        break
print(f"--- Part 1a ---\n"
      f"The total number of lanternfish is: {len(res)}\n")

g = np.zeros(9)
# Counting original frequency
for n in nums:
    g[n] += 1
# print(g)

for day in range(256):
    # Rolls back the values in the array by one for every day passed
    g = np.roll(g, -1)
    # Accounts for when there's and increase in fish due to the days reaching 0
    # and their cycle starts again
    g[6] += g[8]
    # the sum of the frequencies becomes the number of fish
    # better way of answering this question and part a, as it is faster and uses less memory
print(f"--- Part 1b ---\n"
      f"The total number of lanternfish is: {int(sum(g))}\n")
