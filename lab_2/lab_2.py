from tkinter import *

def click_btn_start():
    pass

def click_btn_move():
    pass

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

root.mainloop()
