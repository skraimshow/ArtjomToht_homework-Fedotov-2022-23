from tkinter import *

# Создаем основное окно
place = Tk()
place.title("Светофор")
draw = Canvas(place, width=290, height=400)

# Создаем первый светофор для автомобилей
draw.create_rectangle(50, 50, 120, 240, fill="black")
car_red = draw.create_oval(60, 60, 110, 110, fill="#800000")  # Красный выключен
car_yellow = draw.create_oval(60, 120, 110, 170, fill="#666600")  # Желтый выключен
car_green = draw.create_oval(60, 180, 110, 230, fill="#006600")  # Зеленый выключен

# Создаем второй светофор для пешеходов
draw.create_rectangle(160, 50, 230, 240, fill="black")
ped_red = draw.create_oval(170, 60, 220, 110, fill="#800000")  # Красный выключен
ped_yellow = draw.create_oval(170, 120, 220, 170, fill="#666600")  # Желтый выключен
ped_green = draw.create_oval(170, 180, 220, 230, fill="#006600")  # Зеленый выключен

# Функция для смены цветов
def switch_lights():
    # Сначала автомобили едут, пешеходы стоят
    draw.itemconfig(car_red, fill="#800000")  # Красный для авто выключен
    draw.itemconfig(car_green, fill="#00e600")  # Зеленый для авто включен
    draw.itemconfig(car_yellow, fill="#666600")  # Желтый для авто выключен
    draw.itemconfig(ped_red, fill="red")  # Красный для пешеходов включен
    draw.itemconfig(ped_green, fill="#006600")  # Зеленый для пешеходов выключен
    draw.itemconfig(ped_yellow, fill="#666600")  # Желтый для пешеходов выключен
    
    # Через 5 секунд желтый для авто
    place.after(5000, car_yellow_light)

def car_yellow_light():
    draw.itemconfig(car_green, fill="#006600")  # Зеленый для авто выключен
    draw.itemconfig(car_yellow, fill="yellow")  # Желтый для авто включен
    
    # Через 2 секунды красный для авто и зеленый для пешеходов
    place.after(2000, pedestrian_green)

def pedestrian_green():
    draw.itemconfig(car_yellow, fill="#666600")  # Желтый для авто выключен
    draw.itemconfig(car_red, fill="red")  # Красный для авто включен
    draw.itemconfig(ped_red, fill="#800000")  # Красный для пешеходов выключен
    draw.itemconfig(ped_green, fill="#00e600")  # Зеленый для пешеходов включен
    draw.itemconfig(ped_yellow, fill="#666600")  # Желтый для пешеходов выключен
    
    # Через 7 секунд пешеходный желтый и возвращаемся
    place.after(7000, pedestrian_yellow)

def pedestrian_yellow():
    draw.itemconfig(ped_green, fill="#006600")  # Зеленый для пешеходов выключен
    draw.itemconfig(ped_yellow, fill="yellow")  # Желтый для пешеходов включен
    
    # Через 2 секунды цикл начинается заново
    place.after(2000, switch_lights)

# Кнопка для начала работы светофора
B1 = Button(place, text="Кнопка перехода", command=switch_lights)
B1.pack(pady=20)

draw.pack()
place.mainloop()
