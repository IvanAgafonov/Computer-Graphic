from tkinter import *
from tkinter import messagebox
import tkinter.ttk as tkk
from random import random

import time

def update_mass():

    text_1 = '           x1       y1\n'
    for i in mas_1:
        text_1 += '{:10d} {:10d}\n'.format(i[0], i[1])
    data_1['text'] = text_1


    text_2 = '          x2       y2\n'
    for i in mas_2:
        text_2 += '{:10d} {:10d}\n'.format(i[0], i[1])
    data_2['text'] = text_2



    text_number = ''
    for i in range(max(len(mas_1),len(mas_2))):
        text_number += str(i+1) + "\n"
    data_number['text'] = text_number

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
            messagebox.showerror("Error", "Error input. number_point(N) must me integer and 1<N<len(mas)")
            print("Error input. number_point(N) must me integer and 1<N<len(mas)")

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

    # for i in range(len(mas_1)):
    #     print(1)
    #     for
    #     for
    # for i in range
    pass


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
mas_1 = [[10,23],[43,21],[53,25]]
mas_2 = [[45,21]]

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

# Таблицы точек
text_1 = '           x1       y1\n'
for i in mas_1:
    text_1 += '{0:10} {0:10}\n'.format(i[0],i[1])
data_1 = Label(text=text_1)
data_1.place(x = 10, y = 250)

text_2 = '          x2       y2\n'
for i in mas_2:
    text_2 += '{0:10d}{0:10d}'.format(i[0],i[1]) + "\n"
data_2 = Label(text=text_2)
data_2.place(x = 100, y = 250)

text_number = ''
for i in range(max(len(mas_1),len(mas_2))):
    text_number += str(i+1) + "\n"
data_number = Label(text=text_number)
data_number.place(x = 0, y = 265)

# Таблицы точек
lb_header = ['x_1', 'y_1','x_2','y_2']
tabl = tkk.Treeview(root)
tabl_1 = tkk.Treeview(root)
tabl["columns"] = ("x_1","y_1","x_2","y_2")

width_column = 100

tabl.column("#0",  width=width_column)
tabl.column("x_1", width=width_column)
tabl.column("y_1", width=width_column)
tabl.column("x_2", width=width_column)
tabl.column("y_2", width=width_column)




tabl.heading("x_1", text="x_1")
tabl.heading("y_1", text="y_1")
tabl.heading("x_2", text="x_2")
tabl.heading("y_2", text="y_2")

for i in range(len(mas_1)):
    tabl.insert("", i, text=i, values=(mas_1[i][0],mas_1[i][1]))


tabl.place(x = 10, y = 250)
    

#canv = Canvas(width = 800, height = 600, bg = "black", cursor = "pencil")
#canv.place(x = 450, y = 44)


#https://docs.python.org/3/library/tkinter.ttk.html#treeview

root.mainloop()