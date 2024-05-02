from tkinter import *

class Object:
    def __init__(self):
        self.master = Tk()
        self.master.config(bg='peach puff')
        self.zagol = Label(self.master, text="Калькулятор квадратных уравнений", font='calibri, 18', bg='peach puff', fg='rosybrown4')
        #self.zagol.grid(row=0, column=2)
        self.zagol.pack()
        self.text = Label(self.master, text='Лень считать дискриминант? Не выучил теорему Виета? Используй мой '
                                            'шедеврокалькулятор для решения квадратных уравнений!!!', font='calibri, 13', bg='peach puff', fg='burlywood4')
        #self.text.grid(row=1, column=1)
        self.text.pack()
        self.text2 = Label(self.master, text='С его помощью ты получишь детальное решение примера, которое позволит '
                                             'быстро и эффективно решать сложные уравнения.', font='calibri, 13', bg='peach puff', fg='burlywood4')
        self.text2.pack()
        self.textnew = Label(self.master, text='Введи коэффициенты ниже:', font='calibri, 17', bg='peach puff', fg='rosybrown4')
        self.textnew.pack()
        #self.text2.grid(row=4, column=1)
        self.text3 = Label(self.master, text='Внимание! Если твое уравнение линейное (коэффициент а = 0),\n '
                                             'то калькулятор не будет работать!', font='calibri, 11', bg='peach puff', fg='burlywood4')
        self.text3.pack()
        self.texte = Label(self.master, text='\n', font='calibri, 13', bg='peach puff')
        self.texte.pack()
        self.text4 = Label(self.master, text='ax²+bx+c=0', font='calibri, 25', bg='oldlace', fg='burlywood4')
        self.text4.pack()

        self.a = Label(self.master, text='a:', font='calibri, 18', bg='peach puff', fg='burlywood4')
        self.a.pack()
        self.entry = Entry(self.master)
        self.entry.pack()
        self.master.mainloop()
Object()
