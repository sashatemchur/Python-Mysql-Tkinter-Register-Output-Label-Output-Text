import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from loguru import logger


logger.add("register_output.log", format="{time} | {level} | {message}", rotation="100MB") # Adds a file where all logs are stored

window = tk.Tk()
window.title("2 Завдання")

def button_two():
    id = int(e4.get()) # Assigns changes to the input value
    cursor.execute("SELECT name, password, phone FROM user where id = {}".format(id)) # Takes everything from the table according to the specified id
    data = cursor.fetchall() # Outputs with bd text
    l3.config(text="{}".format(data)) # Inserts into the label what we took from the database
    logger.info("The function(button_two) worked") # Makes a log that says everything is fine


connection = mysql.connector.connect(host='localhost',
                                database='tkintermysql',
                                user='root',
                                password='') # Connect to the database  

cursor = connection.cursor() 

frame1 = tk.Frame(master=window, bg="Red", width=450, height=200) # Makes a blue window
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame2 = tk.Frame(master=window, bg="black", width=450, height=200) # Makes a blue window
frame2.pack(fill=tk.BOTH, side=tk.BOTTOM,  expand=True)

e4 = tk.Entry(master=frame1, width=100) # Text field for entering ID
e4.pack(padx=15, pady=15)

l3 = tk.Label(master=frame1, text="") # A text field where information from the database is inserted
l3.pack()

button1 = tk.Button(master=frame2, relief=tk.FLAT, text="Вивести", width=50, height=15, bg="black", fg="white", command=button_two) # Make a button that displays everything from the database according to the specified id
button1.place(x=450,y=100)

window.mainloop()

cursor.close()
connection.close()