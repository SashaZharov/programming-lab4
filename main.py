import copy
from tkinter import *
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import module as m
import recovery as r
import smoothing as s

tickers = ["YNDX", "GAZP", "TATN", "SBER", "VTBR", "ALRS", "AFLT", "HYDR"]
recovery = ["Винзорирование", "Линейная аппроксимация"]
smoothing = ["Взвешенный метод скользящего среднего", "Метод скользящего среднего со скользящим окном наблюдения"]

# Функции для обработки введенных данных
def Select():
    ticker = cmb1.get()
    start = date_start.get()
    end = date_end.get()
    print(start, end)
    quot = m.getData(ticker, start, end)
    rst = copy.copy(quot)
    #Восстановление
    if cmb2.get() == "Винзорирование":
        print("Винзорирование")
        rst = r.venz(rst)

    elif cmb2.get() == "Линейная аппроксимация":
        print("Линейная аппроксимация")
        rst = r.aprokRest(rst)

     #Сглажевание
    smt = copy.copy(rst)
    if cmb3.get() == "Взвешенный метод скользящего среднего":
        print("Взвешенный метод скользящего среднего")
        smt = s.smt1(smt, float(ntr1.get()))
    elif cmb3.get() == "Метод скользящего среднего со скользящим окном наблюдения":
        print("Метод скользящего среднего со скользящим окном наблюдения")
        smt = s.smt2(smt, float(ntr2.get()))

    Generate(quot, rst, smt)


def Generate(quot, rst, smt):
    global conv
    if conv:
        conv.get_tk_widget().destroy()

    figure2 = plt.Figure(figsize=(16, 9), dpi=100)
    ax2 = figure2.add_subplot(111)
    conv = FigureCanvasTkAgg(figure2, str8)
    conv.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax2.plot(rst)
    ax2.plot(quot)
    ax2.plot(smt)
    ax2.set_title(cmb1.get())
    return conv


def Close():
    global conv
    if conv:
        conv.get_tk_widget().destroy()
        return conv

# Структура окна
window = Tk()
window.geometry("900x700")
window.title("Аналитика акций")

conv = None

str1 = Frame(window)
str2 = Frame(window)
str3 = Frame(window)
str4 = Frame(window)
str5 = Frame(window)
str6 = Frame(window)
str7 = Frame(window)
str8 = Frame(window)

str1.pack()
str2.pack()
str3.pack()
str4.pack()
str5.pack()
str6.pack()
str7.pack()
str8.pack()

lb1 = Label(str1, text="Введите тикер:", padx=5, pady=5)
lb1.pack(side=LEFT)

lb2 = Label(str2, text="Введите временной отрезок:", padx=5, pady=5)
lb2.pack(side=LEFT)

cmb1 = ttk.Combobox(str1, values=tickers , state="readonly")
cmb1.pack(side=LEFT)

date_start = Entry(str2, width=15)
date_end = Entry(str2, width=15)
date_start.pack(side=LEFT)
date_end.pack(side=LEFT)

lb3 = Label(str4, text="Выберите способ восстановления:", padx=5, pady=5)
lb3.pack(side=LEFT)

cmb2 = ttk.Combobox(str4, values=recovery, state="readonly")
cmb2.pack(side=LEFT)

lb3 = Label(str5, text="Выберите способ сглаживания:", padx=5, pady=5)
lb3.pack(side=LEFT)

cmb3 = ttk.Combobox(str5, values=smoothing, state="readonly")
cmb3.pack(side=LEFT)

lb4 = Label(str6, text="Размер окна:", padx=5, pady=5)
lb4.pack(side=LEFT)

ntr1 = Entry(str6, width=15)
ntr1.pack(side=LEFT)

lb5 = Label(str6, text="Коэффициент:", padx=5, pady=5)
lb5.pack(side=LEFT)

ntr2 = Entry(str6, width=15)
ntr2.pack(side=LEFT)

btn1 = Button(str7, text="Построить график", command=Select, padx=5, pady=5)
btn1.pack(side=LEFT)

button = Button(str7, text="Отчистить", command=Close, padx=5, pady=5)
button.pack(side=LEFT)

window.mainloop()
