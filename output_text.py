import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from loguru import logger


logger.add("register_output.log", format="{time} | {level} | {message}", rotation="100MB") # Adds a file where all logs are stored


window = tk.Tk()
window.title("3 Завдання")

connection = mysql.connector.connect(host='localhost',
                                database='tkintermysql',
                                user='root',
                                password='') # Connect to the database 

cursor = connection.cursor() 

def button_three():
    cursor.execute('SELECT * FROM user') # Takes everything from the table
    data = cursor.fetchall() # Makes the text from what we took from the database
    text1.insert(tk.END, data) # Insert into the text what we took from the database
    logger.info("The function(button_three) worked") # Makes a log that says everything is fine


text1 = tk.Text(width = 141, height = 50) # Makes a text
text1.pack()

button1 = tk.Button(text="Вивести все", height=50, command=button_three) # Make a button that displays everything from the database
button1.place(x=1,y=1)

button2 = tk.Button(text="Вивести все", height=50, command=button_three) # Make a button that displays everything from the database
button2.place(x=1210,y=1)


window.mainloop()

cursor.close()
connection.close()