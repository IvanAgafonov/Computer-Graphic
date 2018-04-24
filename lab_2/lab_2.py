from tkinter import *
from tkinter import messagebox
import numpy as np
import copy
import math

def paint():
    global mas, val, window_x, window_y
    # Очистка холста
    canv.delete('all')

    # Инверсия по Y
    mas_1 = copy.deepcopy(mas)
    print("--")
    for i in mas_1:

        i[1] = window_y - i[1]

    print(mas_1)
    print(mas)

    # Основа дома
    canv.create_polygon(mas_1[0],mas_1[1],mas_1[2],mas_1[3], outline="#FFFFFF")
    canv.create_polygon(mas_1[3],mas_1[4],mas_1[2], outline="#FFFFFF")

    #Окна
    canv.create_polygon(mas_1[5],mas_1[6],mas_1[7],mas_1[8], outline="#FFFFFF")
    canv.create_polygon(mas_1[9],mas_1[10],mas_1[11],mas_1[12], outline="#FFFFFF")

    # Ромб в окне
    canv.create_polygon(mas_1[13],mas_1[14],mas_1[15],mas_1[16], outline="#FFFFFF")

    # Решетка окна
    canv.create_line(mas_1[17],mas_1[18], fill="#FFFFFF")
    canv.create_line(mas_1[19],mas_1[20], fill="#FFFFFF")

    print([mas_1[25][0]+math.sqrt((val*2)**2*2)*math.cos(angle),mas_1[25][1]+math.sqrt((val*2)**2*2)*math.sin(angle)])
    print(math.cos(angle))
    #Круглое окно
    #canv.create_polygon(mas_1[25],mas_1[29],mas_1[26],mas_1[30], outline="#FFFFFF")
    canv.create_oval(mas_1[29][0] - math.sqrt(rad_x**2*2)*math.cos(angle), mas_1[29][1]  + math.sqrt(rad_y**2*2)*math.sin(angle),
                     mas_1[29][0] + math.sqrt(rad_x**2*2)*math.cos(angle), mas_1[29][1] - math.sqrt(rad_y**2*2)*math.sin(angle), outline="#FFFFFF")
    canv.create_line(mas_1[29][0] - math.sqrt(rad_x**2*2)*math.cos(angle), mas_1[29][1]  + math.sqrt(rad_y**2*2)*math.sin(angle),
                     mas_1[29][0] + math.sqrt(rad_x**2*2)*math.cos(angle), mas_1[29][1] - math.sqrt(rad_y**2*2)*math.sin(angle), fill="#FFFFFF")

    for t in np.arange(0, 2 * math.pi, 0.001):
        x = mas_1[30][0] + 20 * math.cos(t)
        y = mas_1[30][1] + 10 * math.sin(t)
        canv.create_line(x, y, x + 0.1, y + 0.1, fill="#FFFFFF", width=1)


    #Дуга окна
    #canv.create_arc(mas_1[27],mas_1[28], start=0, extent=180, outline="#FFFFFF")
    #print(angle_3, "a")
    #canv.create_arc(mas_1[30][0] - math.sqrt(rad_x**2*2)*math.cos(angle_2 - ((angle_3 * math.pi/540) % 30)), mas_1[30][1] - math.sqrt(rad_y**2*2)*math.sin(angle_2 - ((angle_3 * math.pi/540) % 30)),
    #                mas_1[30][0] + math.sqrt(rad_x**2*2)*math.cos(angle_2 + ((angle_3 * math.pi/540) % 30)), mas_1[30][1] + math.sqrt(rad_y**2*2)*math.sin(angle_2 + ((angle_3 * math.pi/540) % 30)), start=0, extent=350, outline="#FFFFFF")

    # canv.create_line(mas_1[30][0] - math.sqrt(rad_x_1**2 + rad_y_1**2)*math.cos(angle_2 + angle_3/3 * math.pi/180), mas_1[30][1] - math.sqrt(rad_x_1**2 + rad_y_1**2)*math.sin(angle_2 + angle_3/3 * math.pi/180),
    #                  mas_1[30][0] + math.sqrt(rad_x_1**2 + rad_y_1**2)*math.cos(angle_2 + angle_3/3 * math.pi/180), mas_1[30][1] + math.sqrt(rad_x_1**2 + rad_y_1**2)*math.sin(angle_2 + angle_3/3 * math.pi/180), fill="#FFFFFF")
    #
    # canv.create_line(mas_1[31][0] - val + math.sqrt((val/2)**2-(0.25*val)**2), mas_1[31][1] - val*0.5, mas_1[29], fill="#FFFFFF")
    # canv.create_line(mas_1[32][0] + val - math.sqrt((val/2)**2-(0.25*val)**2), mas_1[31][1] + val*0.5, mas_1[29], fill="#FFFFFF")

    canv.create_line(mas_1[30][0] - math.sqrt(rad_x_1**2 + rad_y_1**2)*math.cos(angle_2 + ((angle_3 * math.pi/540) % 30)), mas_1[30][1] - math.sqrt(rad_x_1**2 + rad_y_1**2)*math.sin(angle_2 + ((angle_3 * math.pi/540) % 30)),
                     mas_1[30][0] + math.sqrt(rad_x_1**2 + rad_y_1**2)*math.cos(angle_2 + ((angle_3 * math.pi/540) % 30)), mas_1[30][1] + math.sqrt(rad_x_1**2 + rad_y_1**2)*math.sin(angle_2 + ((angle_3 * math.pi/540) % 30)),fill="#FFFFFF")


    #print(angle_3/3)

    # Решетка для круглого окнаmas_1
    canv.create_line(mas_1[21],mas_1[22], fill="#FFFFFF")
    canv.create_line(mas_1[23],mas_1[24], fill="#FFFFFF")




def click_btn_start():
    global mas, rad_x, rad_y, rad_x_1, rad_y_1, angle, angle_2, angle_3, val, mas_2

    angle   = 45 * math.pi/180
    angle_2 = math.asin(1/math.sqrt(5))
    angle_3 = 0
    val = 20
    rad_x = val
    rad_y = val
    rad_x_1 = val
    rad_y_1 = val*0.5

    mas = [[0,0], [8*val,0], [8*val,4*val], [0, 4*val], [4*val, 8*val], [1*val,1*val], [1*val, 3*val], [3*val, 3*val],
           [3*val, 1*val], [5*val, 1*val], [5*val, 3*val], [7*val, 3*val], [7*val, 1*val], [5*val, 2*val], [6*val, 3*val], [7*val, 2*val],
           [6*val, 1*val], [1*val, 2*val], [3*val, 2*val], [2*val, 2*val], [2*val, 1*val], [3*val, 6*val], [5*val, 6*val], [4*val, 7*val],
           [4*val, 5*val], [3*val, 7*val], [5*val, 5*val], [1*val, 3.5*val], [3*val, 2.5*val], [4*val, 6*val], [2*val, 3*val], [1*val,3.5*val], [3*val,2.5*val]]


    # Центрирование
    for i in mas:
        i[0] += window_x/2 - 4*val
        i[1] += window_y/2 - 4*val

    mas_2 = copy.deepcopy(mas)


    paint()

def click_btn_move():
    global mas, mas_2
    mas_2 = copy.deepcopy(mas)

    line = message_entr_move.get().split(",")
    if len(line) != 2:
        print("Error Input. Need 2 argument (dx, dy)")
        messagebox.showerror("Error", "Error Input. Need 2 argument (dx, dy)")
        return 0

    for i in mas:
        i += [1]

    print(mas)
    mas = np.array(mas)

    M = np.array([[1,0,0], [0,1,0], [int(line[0]),int(line[1]),1]])

    for i in range(len(mas)):
        mas[i] = np.dot(mas[i],M)




    mas = list(map(list, mas))
    for i in range(len(mas)):
        mas[i] = mas[i][:2]


    paint()

def click_btn_rotate():
    global mas, angle, angle_2, angle_3, mas_2
    mas_2 = copy.deepcopy(mas)

    line = message_entr_rotate.get().split(",")
    if len(line) != 3:
        print("Error Input. Need 3 argument (x0, y0, angle)")
        messagebox.showerror("Error", "Error Input. Need 3 argument (x0, y0, angle)")
        return 0

    x0 = float(line[0])
    y0 = float(line[1])
    angle_1 = float(line[2]) * math.pi/180
    #angle_2 += float(line[2])
    angle_3 += float(line[2])

    print(angle_2,"angle")

    print("---")
    print(mas)
    for i in mas:
        i += [1]
        i[0] -= x0
        i[1] -= y0
    print(mas)

    print(mas)
    mas = np.array(mas)

    M = np.array([[math.cos(angle_1), -math.sin(angle_1),0], [math.sin(angle_1),math.cos(angle_1),0], [0,0,1]])

    for i in range(len(mas)):
        mas[i] = np.dot(mas[i],M)




    mas = list(map(list, mas))
    for i in range(len(mas)):
        mas[i] = mas[i][:2]
        mas[i][0] += x0
        mas[i][1] += y0

    print(1)
    paint()

def click_btn_scale():
    global mas, rad_x, rad_y, rad_x_1, rad_y_1, mas_2
    mas_2 = copy.deepcopy(mas)

    line = message_entr_scale.get().split(",")
    if len(line) != 4:
        print("Error Input. Need 4 argument (x0, y0, kx, ky)")
        messagebox.showerror("Error", "Error Input. Need 4 argument (x0, y0, kx, ky)")
        return 0

    x0 = float(line[0])
    y0 = float(line[1])

    kx = float(line[2])
    ky = float(line[3])

    print("-")
    print(mas)
    for i in mas:
        i += [1]
        i[0] -= x0
        i[1] -= y0


    mas = np.array(mas)

    rad_x *= kx
    rad_y *= ky
    rad_x_1 *= kx
    rad_y_1 *= ky
    M = np.array([[kx,0,0], [0,ky,0], [0,0,1]])

    for i in range(len(mas)):
        mas[i] = np.dot(mas[i],M)




    mas = list(map(list, mas))
    for i in range(len(mas)):
        mas[i] = mas[i][:2]
        mas[i][0] += x0
        mas[i][1] += y0

    print(1)
    paint()

def click_btn_return():
    global mas
    mas = copy.deepcopy(mas_2)
    paint()


# Основная сцена
root=Tk()
root.title('Лабораторная работа №1')
root.geometry('1280x768+400+10') # ширина=1024, высота=768, смещение x=600, смещение y=200

btn_bg_color = "#CACACA"
padx = 10
pady = 5

# Кнопки
btn_start = Button(text="Вывод исходного изображения", bg=btn_bg_color, command=click_btn_start)
btn_move = Button(text="Перемещение(dx,dy)", bg=btn_bg_color, command=click_btn_move)
btn_scale = Button(root, text="Масшатбирование(x0, y0, kx, ky)", bg=btn_bg_color, command=click_btn_scale)
btn_rotate = Button(text="Вращение(x,y,angle)", bg=btn_bg_color, command=click_btn_rotate)
btn_return = Button(text="Возврат на одно действие", bg=btn_bg_color, command=click_btn_return)

# Размещение кнопок
btn_start.grid (row=0, column=0, padx=padx, pady=pady)
btn_move.grid  (row=1, column=0, padx=padx, pady=pady)
btn_rotate.grid(row=2, column=0, padx=padx, pady=pady)
btn_scale.grid (row=3, column=0, padx=padx, pady=pady)
btn_return.grid(row=4, column=0, padx=padx, pady=pady)

# Строки внутри полей
message_entr_move = StringVar()
message_entr_rotate = StringVar()
message_entr_scale = StringVar()

# Поля для ввода
entr_move = Entry(textvariable=message_entr_move)
entr_rotate = Entry(textvariable=message_entr_rotate)
entr_scale = Entry(textvariable=message_entr_scale)

# Размещение полей
entr_move.grid(row=1, column=1, padx=padx, pady=pady)
entr_rotate.grid(row=2, column=1, padx=padx, pady=pady)
entr_scale.grid(row=3, column=1, padx=padx, pady=pady)


# Холст изображения
window_x = 800
window_y = 700

canv = Canvas(width = window_x, height = window_y, bg = "black", cursor = "pencil")
canv.place(x = 450, y = 34)

click_btn_start()






root.mainloop()
