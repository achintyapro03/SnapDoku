from tkinter import Tk, Entry, Button, messagebox, END, Toplevel, filedialog, Frame, Label
from PIL import ImageTk, Image
import os
from recNum import numberReader

# test_sudo = [[8, 3, 0], [0, 0, 0], [4, 0, 6],
#              [0, 4, 0], [3, 9, 0], [0, 0, 0],
#              [0, 0, 6], [2, 0, 0], [0, 5, 0],
#
#              [0, 0, 0], [0, 0, 1], [0, 4, 9],
#              [0, 0, 0], [6, 7, 2], [5, 0, 0],
#              [0, 1, 0], [0, 0, 9], [8, 0, 7],
#
#              [0, 7, 0], [0, 1, 5], [0, 0, 0],
#              [0, 0, 9], [0, 6, 0], [1, 0, 5],
#              [0, 0, 0], [9, 0, 0], [3, 0, 0]]

# test_sudo = [[8, 3, 0, 0, 0, 0, 4, 0, 6],
#              [0, 4, 0, 3, 9, 0, 0, 0, 0],
#              [0, 0, 6, 2, 0, 0, 0, 5, 0],
#
#              [0, 0, 0, 0, 0, 1, 0, 4, 9],
#              [0, 0, 0, 6, 7, 2, 5, 0, 0],
#              [0, 1, 0, 0, 0, 9, 8, 0, 7],
#
#              [0, 7, 0, 0, 1, 5, 0, 0, 0],
#              [0, 0, 9, 0, 6, 0, 1, 0, 5],
#              [0, 0, 0, 9, 0, 0, 3, 0, 0]]

test_sudo = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# test_sudo = [[0, 0, 1, 2, 0, 0, 8, 7, 0],
#              [0, 0, 6, 0, 8, 0, 0, 2, 4],
#              [0, 8, 0, 0, 7, 3, 0, 0, 5],
#              [6, 2, 0, 1, 3, 0, 0, 8, 0],
#              [8, 0, 0, 9, 4, 0, 0, 5, 2],
#              [5, 9, 4, 0, 0, 8, 3, 0, 6],
#              [3, 0, 9, 0, 0, 0, 5, 4, 0],
#              [1, 0, 0, 0, 9, 0, 2, 0, 8],
#              [0, 0, 0, 0, 5, 7, 0, 0, 0]]

# test_sudo = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#              [5, 2, 0, 0, 0, 0, 0, 0, 0],
#              [0, 8, 7, 0, 0, 0, 0, 3, 1],
#              [0, 0, 3, 0, 1, 0, 0, 8, 0],
#              [9, 0, 0, 8, 6, 3, 0, 0, 5],
#              [0, 5, 0, 0, 9, 0, 6, 0, 0],
#              [1, 3, 0, 0, 0, 0, 2, 5, 0],
#              [0, 0, 0, 0, 0, 0, 0, 7, 4],
#              [0, 0, 5, 2, 0, 6, 3, 0, 0]]


import sys

# test_sudo = [[4, 5, 1, 2, 6, 9, 8, 7, 0],
#              [0, 0, 6, 0, 8, 0, 0, 2, 4],
#              [0, 8, 0, 0, 7, 3, 0, 0, 5],
#              [6, 2, 0, 1, 3, 0, 0, 8, 0],
#              [8, 0, 0, 9, 4, 0, 0, 5, 2],
#              [5, 9, 4, 0, 0, 8, 3, 0, 6],
#              [3, 0, 9, 0, 0, 0, 5, 4, 0],
#              [1, 0, 0, 0, 9, 0, 2, 0, 8],
#              [0, 0, 0, 0, 5, 7, 0, 0, 0]]
# new_sudo = test_sudo.copy()
solved = []
solved_status = False


# print(id(test_sudo))
# print(id(new_sudo))

def get_line_vert(matrix, idx):
    lines_vert = []
    for i in range(9):
        line = []
        for j in range(9):
            line.append(matrix[j][i])
        lines_vert.append(line)
    return lines_vert[idx]


# def get_boxes(matrix):
#     boxes = [[] for i in range(9)]
#     comb = [[0, [0]], [1, [1, 3]], [3, [5, 7]], [2, [2, 4, 6]], [4, [8]]]
#     done = []
#     for i in range(0, 9):
#         for j in range(0, 7, 3):
#             row = matrix[i][j:j + 3]
#             box_para = (i // 3) + (j // 3)
#             box_idx = ""
#             for x in comb:
#                 if x[0] == box_para:
#                     for y in x[1]:
#                         if y not in done:
#                             box_idx = y
#
#             for k in row:
#                 boxes[box_idx].append(k)
#             if len(boxes[box_idx]) == 9:
#                 done.append(box_idx)
#     return boxes

def get_boxes(matrix, idx):
    boxes = [[] for _ in range(9)]
    comb = [[0, [0]], [1, [3, 1]], [3, [7, 5]], [2, [6, 4, 2]], [4, [8]]]
    done = []
    box_num = None
    for i in range(0, 9):
        flag1 = False

        if (idx[1] // 3) * 3 <= i <= ((idx[1] // 3) * 3 + 2):
            flag1 = True
        for j in range(0, 7, 3):
            flag2 = False
            if (idx[0] // 3) * 3 <= j <= ((idx[0] // 3) * 3 + 2):
                flag2 = True

            row = matrix[i][j:j + 3]
            box_para = (i // 3) + (j // 3)
            box_idx = ""
            for x in comb:
                if x[0] == box_para:
                    for y in x[1]:
                        if y not in done:
                            box_idx = y

            for k in row:
                boxes[box_idx].append(k)
            if len(boxes[box_idx]) == 9:
                done.append(box_idx)

            if flag1 == True and flag2 == True:
                box_num = box_idx
    return boxes[box_num]


def get_poss_nums(idx, matrix):
    # idx [1] - line number
    # idx [0] - column number
    possible = []
    box = get_boxes(matrix, idx)
    vert_lines = get_line_vert(matrix, idx[0])
    hor_line = matrix[idx[1]]
    # print("box",box)
    # print("vertical",vert_lines)
    # print("horizontal",hor_line)
    for i in range(1, 10):
        if i not in box and i not in vert_lines and i not in hor_line:
            possible.append(i)

    return possible


# print(get_poss_nums([6, 0], test_sudo))

def get_zero_idx(matrix):
    zero_idx = []
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                zero_idx.append([j, i])
    return zero_idx


# print(get_zero_idx(test_sudo))

def ans_disp(matrix):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, END)
            entries[i][j].insert(END, matrix[j][i])


def reset_boxes():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, END)
            entries[i][j].insert(END, '')


def solver(new_matrix):
    global solved, solved_status
    # print("hi")
    zero_idx = get_zero_idx(new_matrix)
    if solved_status == False:
        if zero_idx == []:
            solved_status = True
            solved = new_matrix
            for i in solved:
                print(i)
            ans_disp(solved)
            # sys.exit()

        # for idx in zero_idx:
        else:
            poss = get_poss_nums(zero_idx[0], new_matrix)
            # print(poss)
            if poss == []:
                pass
            else:
                for i in poss:
                    new_matrix[zero_idx[0][1]][zero_idx[0][0]] = i
                    # print("enter solver")
                    # for x in new_matrix:
                    #     print(x)
                    solver(new_matrix)
                    # if solved_status == False:
                    new_matrix[zero_idx[0][1]][zero_idx[0][0]] = 0
                    # print("exit solver")
                    # for x in new_matrix:
                    #     print(x)


# print(get_boxes(test_sudo,[8,0]))
def open_media():
    global Top_img, root2, frame4, img_lab

    route = filedialog.askopenfilename(initialdir="C:/", title="Select a file", filetypes=(
        ("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))

    img_temp = Image.open(route)
    ratiox, ratioy = img_temp.width / 500, img_temp.height / 500
    if (ratiox > 1 or ratioy > 1):
        ratio = max(ratiox, ratioy)
        img_temp = img_temp.resize((int(img_temp.width / ratio), int(img_temp.height / ratio)))

    route = "upload.png"
    img_temp.save(route, format="png")

    # img = ImageTk.PhotoImage(Image.open(route))
    img2 = ImageTk.PhotoImage(Image.open("upload.png"))
    print(route)

    # Label(frame4, text = "HELLO").place(x=0, y=60)
    img_lab.configure(image=img2)
    img_lab.image = img2
    # path = .filename


def get_photo():
    global Top_img
    Top_img = Toplevel()
    Top_img.geometry("600x600")
    Top_img.configure(bg="white")
    global frame4
    frame4 = Frame(Top_img, bg="PaleTurquoise1", width=530, height=530)
    frame4.place(x=30, y=30)
    Button(Top_img, text="add/change photo", command=lambda: open_media()).place(x=250, y=0)
    # Button(Top_img, text="add photo", command = lambda:open_media()).place(x=10,y=30)
    global img_lab
    img_lab = Label(frame4, bg="PaleTurquoise1")
    img_lab.place(x=10, y=10)
    # open_media()
    Top_img.mainloop()


def get_val():
    print("ola")
    values = []
    flag = True
    for i in range(9):
        x = []
        for j in range(9):
            val = entries[j][i].get()
            try:
                val = int(val)
                if 1 <= val <= 9:
                    pass
                else:
                    flag = False
            except:
                # print("in except")
                if val == '':
                    # print("in if cond 1")
                    val = 0
                else:
                    messagebox.showerror("Error",
                                         "Invalid number in the board matrix.Please reenter the invalid number")
                    break
            # print(val)
            x.append(val)
        values.append(x)
    if flag == False:
        messagebox.showerror("Error",
                             "Invalid number in the board matrix.Please reenter the invalid number")
    else:
        # print(values)
        solver(values)


image = ""


def select_file():
    global image, test_sudo, entries
    filetypes = (
        ('png files', '*.png'),
        ('jpg files', '*.jpg'),
        ('All files', '*.*')
    )

    picName = filedialog.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)

    image = Image.open(picName)
    image = image.convert("L")

    numR = numberReader(image)
    numR.run()

    test_sudo = numR.getNumbs()

    for i in range(9):
        for j in range(9):
            ins = test_sudo[j][i]
            if ins == 0:
                entries[i][j].insert(END, '')
            else:
                entries[i][j].insert(END, ins)


# open button


root = Tk()
root.geometry("325x450")
# root.configure(bg="lemon chiffon")
root.configure(bg="PaleTurquoise1")

root.title("Sudoku Solver")
entries = [[Entry(root, highlightthickness=2, font=("Comic Sans MS", 10, "bold"), justify='center') for _ in range(9)]
           for k
           in range(9)]
# a.place(x=10,y=10)
for i in range(9):
    for j in range(9):
        col_para = i // 3 + j // 3
        if col_para % 2 == 0:
            # colour = "PaleTurquoise1"
            colour = "MediumPurple1"
            # colour = "SlateBlue1"
        else:
            # colour ="SteelBlue1"
            # colour = "PaleGreen1"
            colour = "thistle1"
        pos_x = 10 + i * 32
        pos_y = 10 + j * 32
        entries[i][j].config(highlightbackground="black", highlightcolor="black", bg=colour)
        entries[i][j].place(x=pos_x, y=pos_y, width=30, height=30)
        ins = test_sudo[j][i]
        if ins == 0:
            entries[i][j].insert(END, '')
        else:
            entries[i][j].insert(END, ins)

Button(root, text="Solve", command=lambda: get_val(), bg="lawn green", font=("Comic Sans MS", 12, "bold")).place(x=250,
                                                                                                                 y=400)

Button(root, text="Reset", command=lambda: reset_boxes(), bg="lawn green", font=("Comic Sans MS", 12, "bold")).place(
    x=180,
    y=400)
cam = ImageTk.PhotoImage(Image.open("camera.png"))
Label(root, text="Number detection by uploading pic takes time.\nPlease wait until it processes",
      background="azure").place(x=5, y=320)
Button(root, image=cam, borderwidth=0, bg="yellow", command=lambda: select_file()).place(x=50, y=400)

root.mainloop()
