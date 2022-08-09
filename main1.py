import pymysql
import tkinter as tk
from tkinter import *
from tkinter import messagebox


window = tk.Tk()
window.title("1 Завдання")

def button1():
    if entry1.get() != '' and entry2.get() != '' and entry3.get() != '':
        cursor.execute('INSERT INTO user (name, password, phone) VALUES ("{}", "{}", "{}")'.format(entry1.get(), entry2.get(), entry3.get()))
        connection.commit()
    else:
        messagebox.showwarning('Information', 'The line is empty.')

connection = pymysql.connect(
                                host='localhost',
                                database='tkintermysql',
                                user='root',
                                password='',
                                cursorclass=pymysql.cursors.DictCursor
                            )
cursor = connection.cursor() 


frame1 = tk.Frame(master=window, bg="Blue", width=450, height=200)
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame2 = tk.Frame(master=window, bg="Yellow", width=450, height=200)
frame2.pack(fill=tk.BOTH, side=tk.BOTTOM,  expand=True)

entry1 = tk.Entry(master=frame1, width=100)
entry1.pack(padx=15, pady=15)

entry2 = tk.Entry(master=frame1, width=100)
entry2.pack(padx=15, pady=15)

entry3 = tk.Entry(master=frame1, width=100)
entry3.pack(padx=15, pady=15)

b1 = tk.Button(master=frame2, text="Зберегти", width=50, height=15, command=button1)
b1.place(x=450,y=100)

window.mainloop()

cursor.close()