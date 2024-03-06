import tkinter as tk
# import customtkinter as ctk
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import sqlite3

# Inserting data into database
def save_data():
    name = name_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    connextion = sqlite3.connect("users.db")
    cursor = connextion.cursor()

    command = '''CREATE TABLE IF NOT EXISTS user_data(
    name TEXT,
    email TEXT,
    password TEXT
    )'''

    insert_data = '''INSERT INTO user_data (
    name,
    email,
    password) 
    VALUES (?, ?, ?)'''

    insert_data_tuple = (name, email, password)

    cursor.execute(insert_data, insert_data_tuple)

    cursor.execute(command)
    connextion.commit()
    cursor.close()

    toast = ToastNotification(
    title="SQLITE Message",
    message="Data inserted successfully",
    duration=3000,
    )
    toast.show_toast()
    fetch_data()

# Fetching data from database
def fetch_data():
    connextion = sqlite3.connect("users.db")
    cursor = connextion.cursor()

    cursor.execute('SELECT * FROM user_data')
    results = cursor.fetchall()
    print(results)


# Main Window
window = ttk.Window(themename='solar')
window.title("Students")
window.geometry('900x600')

main_frame = ttk.Frame(window)
menu_frame = ttk.Frame(window)

label1 = ttk.Label(main_frame, background='lightgreen')
label1.pack(expand = True, fill = 'both')

# label1 = ctk.CTkLabel(menu_frame, bg_color='pink')
# label1.pack(expand = True, fill = 'both')

main_frame.place(relx=0.4, y = 0, relwidth=0.7, relheight=1,)
menu_frame.place(x = 0, y = 0, relwidth = 0.4, relheight = 1)


name_label = ttk.Label(menu_frame, text="Name: ")
name_entry = ttk.Entry(menu_frame)
email_label = ttk.Label(menu_frame, text="Email: ")
email_entry = ttk.Entry(menu_frame)
pass_label = ttk.Label(menu_frame, text="Password: ")
pass_entry = ttk.Entry(menu_frame)

save_button = ttk.Button(menu_frame, text="Save", command=save_data)


name_label.pack(padx = 4, pady = 3)
name_entry.pack(padx = 4, pady = 3)
email_label.pack(padx = 4, pady = 3)
email_entry.pack(padx = 4, pady = 3)
pass_label.pack(padx = 4, pady = 3)
pass_entry.pack(padx = 4, pady = 3)
save_button.pack(pady = 20, padx = 4)



window.mainloop()