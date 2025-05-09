from tkinter import *

root = Tk()
canvas = Canvas(root, width=700, height=320, background="grey")

# Функция для рисования прямоугольников
def draw_rectangle(canvas, x1, y1, x2, y2, color):
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

# Функция для рисования треугольников
def draw_triangle(canvas, points, color):
    canvas.create_polygon(points, fill=color)

# Функция F1 для флагов C, D, E, J, Q
def f1(letter):
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
        draw_rectangle(canvas, 30, 30 + k, 150, 50 + k, colors[i])
        i += 1
        k += 20

# Функция F2 для флагов G, H, K, T
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
        draw_rectangle(canvas, 180 + k, 50, 190 + k, 110, colors[i])
        i += 1
        k += 10

# Функция F3 для флагов L, N, U (количество секций и цвета)
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
    height_one_segment = height // count
    width_one_segment = width // count

    offset_height = 300
    offset_width = 100

    # Логика для разделения флагов на секции
    running_height = 0
    for i in range(count):
        running_width = 0
        for j in range(count):
            draw_rectangle(canvas,
                           offset_height + running_height, 
                           offset_width + running_width,
                           offset_height + running_height + height_one_segment,  
                           offset_width + running_width + width_one_segment,
                           colors[(i + j) % len(colors)])
            running_width += width_one_segment
        running_height += height_one_segment

# Пример вызовов функций
f1('C')
f2('T')
f3('U')

canvas.pack()
root.mainloop()
