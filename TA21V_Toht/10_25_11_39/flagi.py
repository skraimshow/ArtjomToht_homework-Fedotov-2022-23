import tkinter as tk
window = tk.Tk()

# Функция для вывода флагов C, D, E, J и Q из международного свода сигналов
def flags1(colors):
    if set(colors).issubset(set(["white", "blue", "red", "yellow", "black"])):
        # код для вывода изображений флагов C, D, E, J и Q
        pass
    else:
        print("Некорректный массив цветов для этой функции")
        
# Функция для вывода флагов G, H, K, T и Q из международного свода сигналов
def flags2(colors):
    if set(colors).issubset(set(["white", "blue", "red", "yellow", "black"])):
        # код для вывода изображений флагов G, H, K, T и Q
        pass
    else:
        print("Некорректный массив цветов для этой функции")

# Функция для вывода флагов с указанным количеством секций и двумя цветами
def flags3(num_sections, color1, color2):
    if set([color1, color2]).issubset(set(["white", "blue", "red", "yellow", "black"])):
        if num_sections == 1:
            # код для вывода прямоугольного флага
            pass
        elif num_sections > 1:
            # код для вывода флага из двух перекрещивающихся полосок
            pass
    else:
        print("Некорректные цвета для этой функции")


window.mainloop()
