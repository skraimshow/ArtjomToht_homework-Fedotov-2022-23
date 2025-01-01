from tkinter import *
from tkinter import ttk
import time

place = Tk()
draw = Canvas(place, width=290, height=400)

# draw.create_text(85, 35, text="Авто", font="sans-serif 20 bold")
# draw.create_text(200, 35, text="Пешеход", font="sans-serif 20 bold")

draw.create_rectangle(50, 50, 120, 240, fill="black")


draw.create_oval(60, 60, 110, 110, fill="#800000")  # red - on   #800000 - off
draw.create_oval(60, 120, 110, 170, fill="#666600")  # yellow - on   #666600 - off
draw.create_oval(60, 180, 110, 230, fill="#006600")  # 00e600 - on   #006600 - off

draw.create_rectangle(160, 50, 230, 240, fill="black")

draw.create_oval(170, 60, 220, 110, fill="#800000")  # red - on   #800000 - off
draw.create_oval(170, 120, 220, 170, fill="#666600")  # yellow - on   #666600 - off
draw.create_oval(170, 180, 220, 230, fill="#006600")  # 00e600 - on   #006600 - off

#draw.create_oval(60, 60, 110, 110, fill="red")  # red - on   #800000 - off
#draw.create_oval(60, 120, 110, 170, fill="yellow")  # yellow - on   #666600 - off
#draw.create_oval(60, 180, 110, 230, fill="#00e600")  # 00e600 - on   #006600 - off
#command=
def btnclick():
    draw.create_oval(60, 60, 110, 110, fill="red")
    #time.sleep(3)
    draw.create_oval(60, 120, 110, 170, fill="yellow")
    draw.create_oval(60, 180, 110, 230, fill="#00e600")

B1 = Button(draw, text = "Кнопка перехода", command=btnclick)
B1.place(x = 90,y = 300)

        

draw.pack()
place.mainloop()