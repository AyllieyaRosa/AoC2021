# AoC Day 2 - Part 1
fwd = 0
depth = 0

file1 = open("input2.txt", "r")

for line in file1:
    if "forward" in line:
        fwd += int(line[-2])
    elif "down" in line:
        depth += int(line[-2])
    elif "up" in line:
        depth -= int(line[-2])

print(f"--- Part 2a ---\n"
      f"Total horizontal position: {fwd}\n"
      f"Total depth: {depth}\n"
      f"Horizontal position multiplied by depth: {fwd * depth}\n")
file1.close()

# Part 2
file1 = open("input2.txt", "r")
aim = 0
depth = 0
fwd = 0

for line in file1:
    if "down" in line:
        aim += int(line[-2])
    elif "up" in line:
        aim -= int(line[-2])
    elif "forward" in line:
        fwd += int(line[-2])
        depth += aim * int(line[-2])

print(f"--- Part 2b ---\n"
      f"Total horizontal position: {fwd}\n"
      f"Total aim: {aim}\n"
      f"Total depth: {depth}\n"
      f"Horizontal position multiplied by depth: {fwd * depth}")
