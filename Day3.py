# AoC Day 3 - Part 1

file1 = open("input3.txt", "r")
binaries = []
for line in file1:
    binaries.append(line.replace("\n", ""))
# print(int("10110", 2))  # Converting from binary to decimal
file1.close()

tot_bin_lth = len(binaries)
bin_lth = len(binaries[0])
cnt_0 = 0
cnt_1 = 0
# print(bin_lth)
gamma = ""
epsilon = ""

for j in range(0, bin_lth):
    for i in binaries:
        if i[j] == "0":
            cnt_0 += 1
        elif i[j] == "1":
            cnt_1 += 1
    if cnt_0 > cnt_1:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    elif cnt_1 > cnt_0:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        pass
    cnt_0 = 0
    cnt_1 = 0

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print(f"--- Part 1 ---\n"
      f"Gamma rate: {gamma} or {gamma_dec}\n"
      f"Epsilon rate: {epsilon} or {epsilon_dec}\n"
      f"Power consumption: {gamma_dec * epsilon_dec}\n")

# --- Part 2 ---
bins1 = binaries.copy()
bins2 = binaries.copy()
tot_bin_lth1 = len(bins1)
tot_bin_lth2 = len(bins2)

while tot_bin_lth1 > 1:
    for j in range(0, bin_lth):
        tot_bin_lth1 = len(bins1)
        if tot_bin_lth1 == 1:
            break
        for i in bins1:
            if i[j] == "0":
                cnt_0 += 1
            elif i[j] == "1":
                cnt_1 += 1

        tmp1 = []
        if cnt_0 > cnt_1:
            for i in bins1:
                if i[j] == "1":
                    x = bins1.index(i)
                    tmp1.append(x)
        elif cnt_1 > cnt_0:
            for i in bins1:
                if i[j] == "0":
                    x = bins1.index(i)
                    tmp1.append(x)
        elif cnt_0 == cnt_1:
            for i in bins1:
                if i[j] == "0":
                    x = bins1.index(i)
                    tmp1.append(x)
        cnt_0 = 0
        cnt_1 = 0

        for index in sorted(tmp1, reverse=True):
            del bins1[index]
            tot_bin_lth1 = len(bins1)
            if tot_bin_lth1 == 1:
                break

oxy = bins1[0]

while tot_bin_lth2 > 1:
    for j in range(0, bin_lth):
        tot_bin_lth2 = len(bins2)
        if tot_bin_lth2 == 1:
            break
        for i in bins2:
            if i[j] == "0":
                cnt_0 += 1
            elif i[j] == "1":
                cnt_1 += 1

        tmp2 = []
        if cnt_0 > cnt_1:
            for i in bins2:
                if i[j] == "0":
                    x = bins2.index(i)
                    tmp2.append(x)
        elif cnt_1 > cnt_0:
            for i in bins2:
                if i[j] == "1":
                    x = bins2.index(i)
                    tmp2.append(x)
        elif cnt_0 == cnt_1:
            for i in bins2:
                if i[j] == "1":
                    x = bins2.index(i)
                    tmp2.append(x)
        cnt_0 = 0
        cnt_1 = 0

        for index in sorted(tmp2, reverse=True):
            del bins2[index]
            tot_bin_lth2 = len(bins2)
            if tot_bin_lth2 == 1:
                break

co2 = bins2[0]


oxy_dec = int(oxy, 2)
co2_dec = int(co2, 2)

print(f"--- Part 2 ---\n"
      f"Oxygen generator rating: {oxy} or {oxy_dec}\n"
      f"CO2 scrubber rating: {co2} or {co2_dec}\n"
      f"Life support rating: {oxy_dec * co2_dec}\n")
