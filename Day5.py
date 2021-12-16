import numpy as np
# AoC Day 5 - Part 1


def gte_arr_coords(value, array):
    # Defining a function to determine the index location of the value entered within an numpy array
    # and if it is equal to or greater than specified value
    crd = []
    """Finds the index location of the specified value within the specified array"""
    xy = np.where(array >= value)
    coords_list = zip(xy[0], xy[1])
    for coord in coords_list:
        crd.append(coord)
    return crd


file1 = open("input5.txt", "r")

xy1 = []
xy2 = []
xy_all = []
count = 0

for line in file1:
    str_split = line.replace("\n", "").split(" -> ")
    str_len = len(str_split)
    for i in range(0, str_len):
        count += 1
        if count % 2 == 0:
            tmp = str_split[i].split(",")
            map_xy2 = map(int, tmp)
            tmp1 = list(map_xy2)
            xy2.append(tmp1)
            xy_all.append(tmp1[0])
            xy_all.append(tmp1[1])
        else:
            tmp2 = str_split[i].split(",")
            map_xy1 = map(int, tmp2)
            tmp3 = list(map_xy1)
            xy1.append(tmp3)
            xy_all.append(tmp3[0])
            xy_all.append(tmp3[1])

xy_len = len(xy1)
grid_len = max(xy_all) + 1

j = 0
hv = []
tmp = []
# Determining horizontal or vertical lines
for i in range(0, xy_len):
    if xy1[i][0] == xy2[i][0]:
        # x values are the same
        if xy1[i][1] < xy2[i][1]:
            tmp = []
            for j in range(xy1[i][1], xy2[i][1]+1):
                tmp.append([xy1[i][0], j])
        elif xy2[i][1] < xy1[i][1]:
            tmp = []
            for j in range(xy2[i][1], xy1[i][1]+1):
                tmp.append([xy2[i][0], j])
        hv.append(tmp)
    elif xy1[i][1] == xy2[i][1]:
        # y values are the same
        if xy1[i][0] < xy2[i][0]:
            tmp = []
            for j in range(xy1[i][0], xy2[i][0]+1):
                tmp.append([j, xy1[i][1]])
        elif xy2[i][0] < xy1[i][0]:
            tmp = []
            for j in range(xy2[i][0], xy1[i][0]+1):
                tmp.append([j, xy2[i][1]])
        hv.append(tmp)

# print(hv)

arr0 = np.zeros((grid_len, grid_len))

hv_flat = [item for sublist in hv for item in sublist]
for i in hv_flat:
    y = i[1]
    x = i[0]
    arr0[y, x] += 1

coords = gte_arr_coords(2, arr0)
print(f"--- Part 1a ---\n"
      f"The number of points where at least two lines overlap is: {len(coords)}\n")
# --- Part 2 ---


def diagonal_coord_increment(x1, x2, y1, y2):
    """To determine the diagonal incrementing coordinates please
    enter the values in the order of x1, x2, y1, y2"""
    if x1 < x2:
        if y1 < y2:
            temp1 = []
            temp2 = []
            for num in range(x1, x2 + 1):
                temp1.append(num)
            for num in range(y1, y2 + 1):
                temp2.append(num)
            r = [list(a) for a in zip(temp1, temp2)]
        if y1 > y2:
            temp1 = []
            temp2 = []
            for num in range(x1, x2 + 1):
                temp1.append(num)
            for num in range(y2, y1 + 1):
                temp2.append(num)
            temp2.reverse()
            r = [list(a) for a in zip(temp1, temp2)]
    elif x1 > x2:
        if y1 < y2:
            temp1 = []
            temp2 = []
            for num in range(x2, x1 + 1):
                temp1.append(num)
            for num in range(y1, y2 + 1):
                temp2.append(num)
            temp1.reverse()
            r = [list(a) for a in zip(temp1, temp2)]
        if y1 > y2:
            temp1 = []
            temp2 = []
            for num in range(x2, x1 + 1):
                temp1.append(num)
            for num in range(y2, y1 + 1):
                temp2.append(num)
            temp1.reverse()
            temp2.reverse()
            r = [list(a) for a in zip(temp1, temp2)]
    return r


xy_len = len(xy1)
grid_len = max(xy_all) + 1

j = 0
hv = []
tmp = []

for i in range(0, xy_len):
    if xy1[i][0] == xy2[i][0]:
        # x values are the same
        if xy1[i][1] < xy2[i][1]:
            tmp = []
            for j in range(xy1[i][1], xy2[i][1]+1):
                tmp.append([xy1[i][0], j])
        elif xy2[i][1] < xy1[i][1]:
            tmp = []
            for j in range(xy2[i][1], xy1[i][1]+1):
                tmp.append([xy2[i][0], j])
        hv.append(tmp)
    elif xy1[i][1] == xy2[i][1]:
        # y values are the same
        if xy1[i][0] < xy2[i][0]:
            tmp = []
            for j in range(xy1[i][0], xy2[i][0]+1):
                tmp.append([j, xy1[i][1]])
        elif xy2[i][0] < xy1[i][0]:
            tmp = []
            for j in range(xy2[i][0], xy1[i][0]+1):
                tmp.append([j, xy2[i][1]])
        hv.append(tmp)
    else:
        hv.append(diagonal_coord_increment(xy1[i][0], xy2[i][0], xy1[i][1], xy2[i][1]))

arr0 = np.zeros((grid_len, grid_len))

hv_flat = [item for sublist in hv for item in sublist]
for i in hv_flat:
    y = i[1]
    x = i[0]
    arr0[y, x] += 1

coords = gte_arr_coords(2, arr0)

print(f"--- Part 1b ---\n"
      f"The number of points where at least two lines overlap is: {len(coords)}\n")



