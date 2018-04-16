from tkinter import *
from tkinter import messagebox
import numpy as np

def paint():
    # Очистка холста
    canv.delete('all')

    # Основа дома
    canv.create_polygon(mas[0],mas[1],mas[2],mas[3], outline="#FFFFFF")
    canv.create_polygon(mas[3],mas[4],mas[2], outline="#FFFFFF")

    #Окна
    canv.create_polygon(mas[5],mas[6],mas[7],mas[8], outline="#FFFFFF")
    canv.create_polygon(mas[9],mas[10],mas[11],mas[12], outline="#FFFFFF")

    # Ромб в окне
    canv.create_polygon(mas[13],mas[14],mas[15],mas[16], outline="#FFFFFF")

    # Решетка окна
    canv.create_line(mas[17],mas[18], fill="#FFFFFF")
    canv.create_line(mas[19],mas[20], fill="#FFFFFF")

    #Круглое окно
    canv.create_oval(mas[25],mas[26], outline="#FFFFFF")

    #Дуга окна
    canv.create_arc(mas[27],mas[28], start=0, extent=180, outline="#FFFFFF")

    # Решетка для круглого окна
    canv.create_line(mas[21],mas[22], fill="#FFFFFF")
    canv.create_line(mas[23],mas[24], fill="#FFFFFF")

def click_btn_start():
    pass

def click_btn_move():
    global mas

    line = message_entr_move.get().split(",")
    if len(line) != 2:
        print("Error Input. Need 2 argument (dx, dy)")
        messagebox.showerror("Error", "Error Input. Need 2 argument (dx, dy)")


    for i in mas:
        i += [1]

    print(mas)
    mas = np.array(mas)

    M = np.array([[1,0,0], [0,1,0], [int(line[0]),int(line[1]),1]])

    for i in range(len(mas)):
        print(mas[i])
        mas[i] = np.dot(mas[i],M)




    mas = list(map(list, mas))
    for i in range(len(mas)):
        mas[i] = mas[i][:2]

    print(mas)
    paint()

def click_btn_rotate():
    pass

def click_btn_scale():
    pass

def click_btn_return():
    pass


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
btn_rotate = Button(root, text="Масшатбирование(x,y,dx,dy)", bg=btn_bg_color, command=click_btn_rotate)
btn_scale = Button(text="Вращение(x,y,angle)", bg=btn_bg_color, command=click_btn_scale)
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
window_y = 600

canv = Canvas(width = window_x, height = window_y, bg = "black", cursor = "pencil")
canv.place(x = 450, y = 44)

val = 20

mas = [[0,0], [8*val,0], [8*val,4*val], [0, 4*val], [4*val, 8*val], [1*val,1*val], [1*val, 3*val], [3*val, 3*val],
       [3*val, 1*val], [5*val, 1*val], [5*val, 3*val], [7*val, 3*val], [7*val, 1*val], [5*val, 2*val], [6*val, 3*val], [7*val, 2*val],
       [6*val, 1*val], [1*val, 2*val], [3*val, 2*val], [2*val, 2*val], [2*val, 1*val], [3*val, 6*val], [5*val, 6*val], [4*val, 7*val],
       [4*val, 5*val], [3*val, 7*val], [5*val, 5*val], [1*val, 3.5*val], [3*val, 2.5*val]]

# Инверсия по Y и центрирование
for i in mas:
    i[0] += window_x/2 - 4*val
    i[1] += window_y/2 - 4*val

    i[1] = window_y - i[1]

paint()




root.mainloop()
