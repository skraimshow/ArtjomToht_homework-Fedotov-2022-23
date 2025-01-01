from tkinter import *

root = Tk()
canvas = Canvas(root, width=700, height=320, background="grey")


def f1(letter) -> None:
    if letter == "C":
        colors = ['blue', 'white', 'red', 'white', 'blue']
    if letter == 'D':
        colors = ['yellow', 'blue', 'blue', 'yellow']
    if letter == 'E':
        colors = ['blue', 'blue', 'red', 'red']
    if letter == 'J':
        colors = ['blue', 'white', 'blue']
    if letter == 'Q':
        colors = ['yellow', 'yellow', 'yellow', 'yellow']

    i = 0
    k = 20
    while i < len(colors):
        points = [
            30, 30 + k,
            150, 30 + k,
            150, 50 + k,
            30, 50 + k
        ]
        canvas.create_polygon(points, fill=colors[i])
        i += 1
        k += 20


def f2(letter):
    if letter == 'G':
        colors = ['yellow', 'blue', 'yellow', 'blue', 'yellow', 'blue']
    if letter == 'H':
        colors = ['white', 'white', 'white', 'red', 'red', 'red']
    if letter == 'K':
        colors = ['yellow', 'yellow', 'yellow', 'blue', 'blue', 'blue']
    if letter == 'T':
        colors = ['red', 'red', 'white', 'white', 'blue', 'blue']
    i = 0
    k = 20
    while i < len(colors):
        points = [
            180 + k, 50,
            190 + k, 50,
            190 + k, 110,
            180 + k, 110
        ]
        canvas.create_polygon(points, fill=colors[i])
        i += 1
        k += 10


def f3(letter):
    if letter == 'L':
        colors = ['black', 'yellow']
        count = 2
    if letter == 'N':
        colors = ['blue', 'white']
        count = 4
    if letter == 'U':
        colors = ['red', 'white']
        count = 2
    width = 100
    height = 100
    height_one_segment = height/count
    width_one_segment = width/count

    offset_height = 300
    offset_width = 100

    # Loop over the rows
    running_height = 0
    for i in range(count):
        running_width = 0
        # Loop over the columns
        for j in range(count):
            canvas.create_rectangle(offset_height + running_height, offset_width + running_width,
                                    offset_height + running_height + height_one_segment,  offset_width + running_width + width_one_segment,
                                    fill=colors[(i+j) % len(colors)])
            running_width += width_one_segment
        running_height += height_one_segment


# f1(['blue', 'white', 'red', 'white', 'blue'])
# f2(['yellow', 'blue', 'yellow', 'blue', 'yellow', 'blue'])
# f3(['blue', 'red'], 4



f1('C')
f2('T')
f3('U')


canvas.pack()
root.mainloop()
