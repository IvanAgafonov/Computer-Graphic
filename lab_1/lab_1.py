from tkinter import *
from tkinter import messagebox
import tkinter.ttk as tkk
from random import random
import math

import time

def update_mass():
    children = tabl_1.get_children()
    for i in range(len(children)):
        tabl_1.delete(children[i])

    children = tabl_2.get_children()
    for i in range(len(children)):
        tabl_2.delete(children[i])

    for i in range(len(mas_1)):
        tabl_1.insert("", i, text=i+1, values=(mas_1[i][0], mas_1[i][1]))
    for i in range(len(mas_2)):
        tabl_2.insert("", i, text=i+1, values=(mas_2[i][0], mas_2[i][1]))

def click_btn_add():
    line = message_entr_add.get().split(",")
    if len(line) != 3:
        print("Error Input. Need 3 argument (x, y, number_mas)")
        messagebox.showerror("Error", "Error Input. Need 3 argument (x, y, number_mas)")
    else:
        try:
            if int(line[2]) == 1:
                mas_1.append([int(line[0]),int(line[1])])
            elif int(line[2]) == 2:
                mas_2.append([int(line[0]),int(line[1])])
            else:
                messagebox.showerror("Error", "Error Input. number_mas must be 1 or 2")
                print("Error Input. number_mas must be 1 or 2")
        except:
            messagebox.showerror("Error", "Error input. x,y must me integer")
            print("Error input. y must me integer")

        update_mass()


def click_btn_del():
    line = message_entr_del.get().split(",")
    if len(line) != 2:
        print("Error Input. Need 2 argument (number_point, number_mas)")
        messagebox.showerror("Error", "Error Input. Need 2 argument (number_point, number_mas)")
    elif int(line[0])<=0:
        print("1<=number_point<=len(mas)")
        messagebox.showerror("Error", "1<=number_point<=len(mas)")
    else:
        try:
            if int(line[1]) == 1:
                del mas_1[int(line[0])-1]
            elif int(line[1]) == 2:
                del mas_2[int(line[0])-1]
            else:
                print("Error Input. number_mas must be 1 or 2")
                messagebox.showerror("Error", "Error Input. number_mas must be 1 or 2")
        except:
            messagebox.showerror("Error", "Error input. number_point(N) must me integer and 1<=N<=len(mas)")
            print("Error input. number_point(N) must me integer and 1<=N<=len(mas)")

        update_mass()

def click_btn_red():
    line = message_entr_red.get().split(",")
    if len(line) != 4:
        print("Error Input. Need 4 argument (x, y, number_point, number_mas)")
        messagebox.showerror("Error", "Error Input. Need 4 argument (x, y, number_point, number_mas)")
    else:
        try:
            if int(line[3]) == 1:
                mas_1[int(line[2])-1] = [int(line[0]),int(line[1])]
            elif int(line[3]) == 2:
                mas_2[int(line[2])-1] = [int(line[0]),int(line[1])]
            else:
                messagebox.showerror("Error", "Error Input. number_mas must be 1 or 2")
                print("Error Input. number_mas must be 1 or 2")
        except:
            messagebox.showerror("Error", "Error input. x,y must me integer and number_point(N) must me integer and 1<N<len(mas)")
            print("Error input. x,y must me integer and number_point(N) must me integer and 1<N<len(mas)")

        update_mass()

def click_btn_run():

    mas_okr_1 = get_mas_okr(mas_1)
    mas_okr_2 = get_mas_okr(mas_2)

    mas_okr = mas_okr_1 + mas_okr_2

    if len(mas_okr) <= 1:
        messagebox.showerror("Error", "Error Input. At these points, zero or one circle can be constructed.")
        return

    for i in mas_okr:
        print(i)

    print("------")

    mas_points_centr = get_mas_points_centr(mas_okr)

    for i in mas_points_centr:
        print(i)
    print("------")

    mas_angle = get_mas_angle(mas_points_centr)

    for i in mas_angle:
        print(i)
    print("------")

    min_angle_i = mas_angle[0][0]
    min_angle_g = mas_angle[0][1]
    min_angle = mas_angle[0][2]

    for k in range(len(mas_angle)):

        i = mas_angle[k][0]
        g = mas_angle[k][1]
        angle = mas_angle[k][2]

        if angle < min_angle:
            min_angle_i = i
            min_angle_g = g
            min_angle = angle


    print(min_angle)
    print(min_angle_g)
    print(min_angle_i)


    # Определение точек найденных окружжностей
    x0_i = mas_points_centr[min_angle_i][0][0]
    y0_i = mas_points_centr[min_angle_i][0][1]
    r_i = mas_points_centr[min_angle_i][1]

    x0_g = mas_points_centr[min_angle_g][0][0]
    y0_g = mas_points_centr[min_angle_g][0][1]
    r_g = mas_points_centr[min_angle_g][1]

    print(x0_i,y0_i,r_i,x0_g,y0_g,r_g)


    # Расчет коэфа масштабирования
    KXmax = window_x - 4
    KYmax = window_y - 4

    KXmin = 0
    KYmin = 0

    if x0_i + r_i >= x0_g + r_g:
        Xmax = x0_i + r_i

    else:
        Xmax = x0_g + r_g

    if x0_i - r_i >= x0_g - r_g:
        Xmin = x0_g - r_g
    else:
        Xmin = x0_i - r_i

    if y0_i + r_i >= y0_g + r_g:
        Ymax = y0_i + r_i

    else:
        Ymax = y0_g + r_g

    if y0_i - r_i >= y0_g - r_g:
        Ymin = y0_g - r_g
    else:
        Ymin = y0_i - r_i

    Kx = (KXmax - KXmin)/(Xmax - Xmin)
    Ky = (KYmax - KYmin)/(Ymax - Ymin)

    scale = min(Kx,Ky)
    print(Xmax)
    print(Xmin)
    print(Ymax)
    print(Ymin)
    print(Kx,Ky)
    print("sds",scale)

    print(len(mas_okr_1))
    print(len(mas_okr_2))
    print(len(mas_points_centr))
    print(len(mas_angle))

    print(y0_i)
    print(y0_g)

    canv.delete('all')

    if r_i > r_g:
        canv.create_oval((x0_i - r_i - Xmin + 0.5) * scale, ((y0_i + r_i - Ymin + 0.5) * scale),
                         (x0_i + r_i - Xmin + 0.5) * scale, ((y0_i - r_i - Ymin + 0.5) * scale),
                         fill='#FFF0F5')
        canv.create_oval((x0_g - r_g - Xmin + 0.5) * scale, ((y0_g + r_g - Ymin + 0.5) * scale),
                         (x0_g + r_g - Xmin + 0.5) * scale, ((y0_g - r_g - Ymin + 0.5) * scale),
                         fill='#E6E6FA')

    else:
        canv.create_oval((x0_g - r_g - Xmin + 0.5) * scale, ((y0_g + r_g - Ymin + 0.5) * scale),
                         (x0_g + r_g - Xmin + 0.5) * scale, ((y0_g - r_g - Ymin + 0.5) * scale),
                         fill='#E6E6FA')
        canv.create_oval((x0_i - r_i - Xmin + 0.5) * scale, ((y0_i + r_i - Ymin + 0.5) * scale),
                         (x0_i + r_i - Xmin + 0.5) * scale, ((y0_i - r_i - Ymin + 0.5) * scale),
                         fill='#FFF0F5')



    if y0_i >= y0_g:
        canv.create_line(0, (y0_i - Ymin + 0.5) * scale, window_x, (y0_i - Ymin + 0.5) * scale, fill='#006400')
    else:
        canv.create_line(0, (y0_g - Ymin + 0.5) * scale, window_x, (y0_g - Ymin + 0.5) * scale, fill='#006400')

    canv.create_line((x0_i - Xmin + 0.5) * scale, (y0_i - Ymin + 0.5) * scale, (x0_g - Xmin + 0.5) * scale, (y0_g - Ymin + 0.5)  * scale, fill='#FF0000')

    offset = 2

    canv.create_oval((x0_i - Xmin + 0.5) * scale - offset, (y0_i - Ymin + 0.5) * scale - offset, (x0_i - Xmin + 0.5) * scale + offset, (y0_i - Ymin + 0.5) * scale + offset, fill="#00FF7F")
    canv.create_oval((x0_g - Xmin + 0.5) * scale - offset, (y0_g - Ymin + 0.5) * scale - offset, (x0_g - Xmin + 0.5) * scale + offset, (y0_g - Ymin + 0.5) * scale + offset, fill="#00FF7F")



    # Перевод из радиан в градусы
    min_angle = min_angle * 180/math.pi
    print(min_angle)

    tx.delete('1.0', END)
    tx.insert(1.0, "Окружности найдены. \n"
                   "Окружность 1: ее радиус {0:.2f}, координаты центра ({1:.2f}, {2:.2f}) \n"
                   "Окружность 2: ее радиус {3:.2f}, координаты центра ({4:.2f}, {5:.2f}) \n"
                   "Угол с осью абцис {6:.2f}".format(r_i, x0_i, y0_i,
                                                                  r_g, x0_g, y0_g,
                                                                  min_angle))

def get_mas_angle(mas):

    mas_angle = []

    for i in range(len(mas)-1):
        for g in range(i+1,len(mas)):

            x1 = mas[i][0][0]
            y1 = mas[i][0][1]

            x2 = mas[g][0][0]
            y2 = mas[g][0][1]

            # A*X+B*Y+C=0

            A1 = y1-y2
            B1 = x2-x1
            C1 = (x1-x2)*y1 + (y2-y1)*x1

            A2 = 0
            B2 = 1
            C2 = 0

            try:
                angle = math.fabs(math.atan((A1*B2 - A2*B1)/(A1*A2 - B1*B2)))
            except:
                angle = 0

            mas_angle.append([i,g,angle])

    return mas_angle

def get_mas_points_centr(mas):

    mas_points_centr = []

    for i in range(len(mas)):
        x1 = mas[i][0]
        y1 = mas[i][1]

        x2 = mas[i][2]
        y2 = mas[i][3]

        x3 = mas[i][4]
        y3 = mas[i][5]

        # A*Xo+B*Yo=C
        # D*Xo+E*Yo=F

        A = 2*(x2-x1)
        B = 2*(y2-y1)
        C = x2**2 - x1**2 + y2**2 - y1**2
        D = 2*(x3-x2)
        E = 2*(y3-y2)
        F = x3**2 - x2**2 + y3**2 - y2**2

        # (X1-Xo)^2 + (Y1-Yo)^2 = R^2
        # (X2-Xo)^2 + (Y2-Yo)^2 = R^2
        # (X3-Xo)^2 + (Y3-Yo)^2 = R^2

        x0 = (C*E - B*F)/(A*E - D*B)
        y0 = (A*F - D*C)/(A*E - D*B)

        rad = distance_between_points([x0,y0],[x1,y1])

        mas_points_centr.append([[x0,y0], rad])

    return mas_points_centr

def distance_between_points(xy1, xy2):
    x_1 = xy1[0]
    x_2 = xy2[0]
    y_1 = xy1[1]
    y_2 = xy2[1]
    dis = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    return dis


def get_mas_okr(mas):

    mas_okr = []

    for i in range(len(mas)-2):
        for g in range(i+1, len(mas)-1):
            for k in range(g+1, len(mas)):
                x1 = mas[i][0]
                y1 = mas[i][1]

                x2 = mas[g][0]
                y2 = mas[g][1]

                x3 = mas[k][0]
                y3 = mas[k][1]

                if (y2-y1) * (x3-x1) != (y3-y1) * (x2-x1):
                    mas_okr.append([x1,y1,x2,y2,x3,y3])

    return mas_okr

def click_btn_add_from_file():

    line = message_entr_run.get()
    try:
        f = open(line,"r")
        data = f.read()
        data = data.split("\n")
    except:
        pass

    for i in range(len(data)):
        data[i] = data[i].split("|")


    print(data)
    for i in range(len(data)-1):
        #print(data[i][1][3:])
        mas_1.append([int(data[i][0].split(" ")[0]),int(data[i][0].split(" ")[1])])
        mas_2.append([int(data[i][1][3:].split(" ")[0]),int(data[i][1][3:].split(" ")[1])])

    update_mass()



# Массивы точек
mas_1 = [[100,100], [28,100], [50,20]]
mas_2 = [[120,55], [160,84], [190,41]]

# Основная сцена
root=Tk()
root.title('Лабораторная работа №1')
root.geometry('1280x768+400+10') # ширина=1024, высота=768, смещение x=600, смещение y=200

btn_bg_color = "#CACACA"
padx = 10
pady = 5

# Кнопки
btn_add_from_file = Button(text="Загрузить данные из файла\n(name_file)", bg=btn_bg_color, command=click_btn_add_from_file)
btn_add = Button(root, text="Добавить точку\n(x, y, number_mas)", bg=btn_bg_color, command=click_btn_add)
btn_del = Button(text="Удалить точку\n(number_point, number_mas)", bg=btn_bg_color, command=click_btn_del)
btn_red = Button(text="Отредактировать точку\n(x, y, number_point, number_mas)", bg=btn_bg_color, command=click_btn_red)
btn_run = Button(text="Запустить", bg=btn_bg_color, command=click_btn_run)

# Размещение кнопок
btn_add_from_file.grid(row=0, column=0, padx=padx, pady=pady)
btn_add.grid(row=1, column=0, padx=padx, pady=pady)
btn_del.grid(row=2, column=0, padx=padx, pady=pady)
btn_red.grid(row=3, column=0, padx=padx, pady=pady)
btn_run.grid(row=4, column=0, padx=padx, pady=pady)

# Строки внутри полей
message_entr_add = StringVar()
message_entr_del = StringVar()
message_entr_red = StringVar()
message_entr_run = StringVar()

# Поля для ввода
entr_add = Entry(textvariable=message_entr_add)
entr_del = Entry(textvariable=message_entr_del)
entr_red = Entry(textvariable=message_entr_red)
entr_run = Entry(textvariable=message_entr_run)

# Размещение полей
entr_add.grid(row=1, column=1, padx=padx, pady=pady)
entr_del.grid(row=2, column=1, padx=padx, pady=pady)
entr_red.grid(row=3, column=1, padx=padx, pady=pady)
entr_run.grid(row=0, column=1, padx=padx, pady=pady)

# Таблица точек 1-ого массива
width_column = 70

tabl_1 = tkk.Treeview(root, height=20)
tabl_1["columns"] = ("x_1", "y_1")

tabl_1.column("#0", width=width_column-30)
tabl_1.column("x_1", width=width_column)
tabl_1.column("y_1", width=width_column)

tabl_1.heading("x_1", text="x_1")
tabl_1.heading("y_1", text="y_1")

tabl_1.place(x = 10, y = 300)

# Скролбар для 1-ой таблицы
vsb_1 = Scrollbar(root, orient="vertical", command=tabl_1.yview)
vsb_1.place(x=10, y=300, height=428)

tabl_1.configure(yscrollcommand=vsb_1.set)

# Таблица точек 2-ого массива
tabl_2 = tkk.Treeview(root, height=20)
tabl_2["columns"] = ("x_2", "y_2")

tabl_2.column("#0", width=width_column-30)
tabl_2.column("x_2", width=width_column)
tabl_2.column("y_2", width=width_column)

tabl_2.heading("x_2", text="x_2")
tabl_2.heading("y_2", text="y_2")

tabl_2.place(x = 190, y = 300)

# Скролбар для 2-ой таблицы
vsb_2 = Scrollbar(root, orient="vertical", command=tabl_2.yview)
vsb_2.place(x=190, y=300, height=428)

tabl_2.configure(yscrollcommand=vsb_2.set)

# Первичное заполнение таблиц
for i in range(len(mas_1)):
    tabl_1.insert("", i, text=i+1, values=(mas_1[i][0], mas_1[i][1]))
for i in range(len(mas_2)):
    tabl_2.insert("", i, text=i+1, values=(mas_2[i][0], mas_2[i][1]))

# Текст для результата
tx = Text(root, width=100, height=4, font='Times 12')
tx.place(x = 450, y = 644)

    
window_x = 800
window_y = 600


canv = Canvas(width = window_x, height = window_y, bg = "black", cursor = "pencil")
canv.place(x = 450, y = 44)


#https://docs.python.org/3/library/tkinter.ttk.html#treeview

root.mainloop()
