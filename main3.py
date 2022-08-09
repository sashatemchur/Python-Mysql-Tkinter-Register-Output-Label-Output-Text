import pymysql
import tkinter as tk
from tkinter import *
from tkinter import messagebox


window = tk.Tk()
window.title("3 Завдання")

connection = pymysql.connect(
                                host='localhost',
                                database='tkintermysql',
                                user='root',
                                password='',
                                cursorclass=pymysql.cursors.DictCursor
                            )

cursor = connection.cursor()

def button3():
    cursor.execute('SELECT * FROM user')
    data = cursor.fetchall()
    text1.insert(tk.END, data)


 


text1 = tk.Text(width = 141, height = 50)
text1.pack()

button1 = tk.Button(text="Вивести все", height=50, command=button3)
button1.place(x=1,y=1)

button2 = tk.Button(text="Вивести все", height=50, command=button3)
button2.place(x=1210,y=1)


window.mainloop()

connection.close()