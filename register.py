import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from loguru import logger


logger.add("register_output.log", format="{time} | {level} | {message}", rotation="100MB") # Adds a file where all logs are stored

window = tk.Tk()
window.title("1 Завдання")

def button_one():
    if entry1.get() != '' and entry2.get() != '' and entry3.get() != '': # It says the condition that if the line is not empty, then we execute the code
        cursor.execute('INSERT INTO user (name, password, phone) VALUES ("{}", "{}", "{}")'.format(entry1.get(), entry2.get(), entry3.get())) # Writes the name, phone number and password in the table
        connection.commit()
    else:
        messagebox.showwarning('Information', 'The line is empty.') # Returns an error that the line is empty
    logger.info("Registration is successful") # Makes a log that says everything is fine
    
    
connection = mysql.connector.connect(host='localhost',
                                database='tkintermysql',
                                user='root',
                                password='') # Connect to the database 

cursor = connection.cursor() 


frame1 = tk.Frame(master=window, bg="Blue", width=450, height=200) # Makes a blue window
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame2 = tk.Frame(master=window, bg="Yellow", width=450, height=200) # Makes a yellow window
frame2.pack(fill=tk.BOTH, side=tk.BOTTOM,  expand=True)

entry1 = tk.Entry(master=frame1, width=100) # Creates an input field
entry1.pack(padx=15, pady=15)

entry2 = tk.Entry(master=frame1, width=100) # Creates an input field
entry2.pack(padx=15, pady=15)

entry3 = tk.Entry(master=frame1, width=100) # Creates an input field
entry3.pack(padx=15, pady=15)

b1 = tk.Button(master=frame2, text="Зберегти", width=50, height=15, command=button_one) # Creates a button that stores data in a table
b1.place(x=450,y=100)

window.mainloop()

cursor.close()
connection.close()