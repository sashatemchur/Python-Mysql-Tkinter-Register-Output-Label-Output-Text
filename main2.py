import pymysql
import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.title("2 Завдання")

def button2():
    id = int(e4.get())
    cursor.execute("SELECT name, password, phone FROM user where id = {}".format(id))
    data=cursor.fetchall()
    l3.config(text="{}".format(data))



connection = pymysql.connect(
                                host='localhost',
                                database='tkintermysql',
                                user='root',
                                password='',
                                cursorclass=pymysql.cursors.DictCursor
                            )
cursor = connection.cursor()

frame1 = tk.Frame(master=window, bg="Red", width=450, height=200)
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame2 = tk.Frame(master=window, bg="black", width=450, height=200)
frame2.pack(fill=tk.BOTH, side=tk.BOTTOM,  expand=True)

e4 = tk.Entry(master=frame1, width=100)
e4.pack(padx=15, pady=15)

l3 = tk.Label(master=frame1, text="")
l3.pack()

button1 = tk.Button(master=frame2, relief=tk.FLAT, text="Вивести", width=50, height=15, bg="black", fg="white", command=button2)
button1.place(x=450,y=100)

window.mainloop()

cursor.close()