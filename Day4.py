import numpy as np
from pprint import pprint
# AoC Day 4 - Part 1


def arr_coords(value, array):
    # Defining a function to determine the index location of the value entered within an numpy array
    crd = []
    """Finds the index location of the specified value within the specified array"""
    xy = np.where(array == value)
    coords_list = zip(xy[0], xy[1])
    for coord in coords_list:
        crd.append(coord)
    return crd


file1 = open("input4.txt", "r")

boards = []
nums = []

for line in file1:
    if line == "\n":  # skipping any blank lines
        pass
    elif len(line) > 15:  # accounting for the numbers that are to be drawn as there are more total characters
        x = line.strip().replace("\n", "").split(",")
        map_nums = map(int, x)
        nums = list(map_nums)
    else:
        y = line.strip().replace("  ", " ").replace("\n", "").split(" ")
        map_boards = map(int, y)  # Mapping the numbers as integers for use in summation later
        board_rows = list(map_boards)  # Converting the map to a list of the now integer values.
        boards.append(board_rows)

# Zipping every five rows into a list then creating a list of lists where each
# element is a list of 25 numbers (a bingo board)
boards = [a + b + c + d + e for a, b, c, d, e in zip(boards[0::5], boards[1::5], boards[2::5], boards[3::5],
                                                     boards[4::5])]
arr_boards = []
# converting the list of lists into a list of numpy arrays
for i in boards:
    an_array = np.array(i)
    reshaped_array = np.reshape(an_array, (5, 5))
    arr_boards.append(reshaped_array)

# copying the original so that doesn't get changed and can be referred back to later if needed
arr_boards1 = list(np.array(arr_boards, copy=True))
arr_boards2 = list(np.array(arr_boards, copy=True))

board = 0
sum_total = 0
board_num = 0
lst_num = 0
bingo = False

for num in nums:
    if bingo:
        # checks to see if bingo has been called, if it hasn't it continues without issue.
        # otherwise it breaks the loop
        break
    for board in arr_boards1:
        if num in board:
            # determining where the index location of the num is within the board
            coords = arr_coords(num, board)
            y = coords[0][0]
            x = coords[0][1]
            board[y, x] = -1  # setting the location to equal = -1

            # checking to see if any row or column has all -1's i.e bingo
            check_row = np.all((board == -1), axis=1)
            check_row = np.ndarray.tolist(check_row)

            check_clm = np.all((board == -1), axis=0)
            check_clm = np.ndarray.tolist(check_clm)
            if True in check_row or True in check_clm:
                # sets bingo to true and retains the last number called for sums later
                # then breaks the loop
                bingo = True
                lst_num = num
                break
        else:
            continue

board_num = [np.array_equal(board, boards) for boards in arr_boards1].index(True) + 1

winner = np.ndarray.tolist(board)
winner = [item for sublist in winner for item in sublist]
total = []
for num in winner:
    if num == -1:
        pass
    else:
        total.append(num)
sum_total = sum(total)

print(f"--- Part 1a ---\n"
      f"The winning board is: {board_num}\n"
      f"\nThe total sum of all unmarked numbers is: {sum_total}\n"
      f"\nThe final score is: {sum_total} x {lst_num} = {sum_total * lst_num}\n")

# --- Part 2 ---
count = 0
start = True
bingo = False
restart = False
win_order = []
while start:
    if bingo:
        count += 1
        print(f"{count} board down ")
        win_order.append(board)
        board_num = [np.array_equal(board, boards) for boards in arr_boards2].index(True)
        arr_boards2.pop(board_num)
        bingo = False
        restart = False
        if len(arr_boards2) == 0:
            start = False
            restart = True
            break

    for num in nums:

        if restart:
            break
        for brd in arr_boards:
            for board in arr_boards2:
                if num in board:
                    coords = arr_coords(num, board)
                    y2 = coords[0][0]
                    x2 = coords[0][1]
                    board[y2, x2] = -1
                if num in brd:
                    coords1 = arr_coords(num, brd)
                    y1 = coords1[0][0]
                    x1 = coords1[0][1]
                    brd[y1, x1] = -1

                check_row = np.all((board == -1), axis=1)
                check_row = np.ndarray.tolist(check_row)

                check_clm = np.all((board == -1), axis=0)
                check_clm = np.ndarray.tolist(check_clm)
                if (True in check_row) or (True in check_clm):
                    bingo = True
                    restart = True
                    lst_num = num
                    break
                else:
                    continue
# win order vs arr_boards comparison
lst_board = win_order[-1]
board_num = [np.array_equal(lst_board, boards) for boards in arr_boards].index(True)
winner = np.ndarray.tolist(lst_board)
winner = [item for sublist in winner for item in sublist]
total = []
for num in winner:
    if num == -1:
        pass
    else:
        total.append(num)
sum_total = sum(total)

print(f"\n--- Part 1b ---\n"
      f"The winning board is: {board_num}\n"
      f"\nThe total sum of all unmarked numbers is: {sum_total}\n"
      f"\nThe final score is: {sum_total} x {lst_num} = {sum_total * lst_num}")