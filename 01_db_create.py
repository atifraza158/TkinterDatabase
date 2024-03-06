import tkinter as tk
import customtkinter as ctk
import sqlite3
from ttkbootstrap.toast import ToastNotification


def show_data(name, email):
    # global name_value
    # global email_value

    print(f"Name: {name}")
    print(f"Email: {email}")


def create_db():
    global name_value
    global email_value
    # Create a new database
    if name_value and email_value:
        conn = sqlite3.connect("data.db")

    # table creation query
        table_create = '''CREATE TABLE IF NOT EXISTS students_data (
        name TEXT,
        email TEXT
        ) '''

        # Create a new table
        conn.execute(table_create)

        # data insertion
        data_insert_query = '''INSERT INTO students_data (name, email) VALUES (?, ?)'''
        data_insert_tuple = (name_value.get(), email_value.get())

        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()

        # toast = ToastNotification(
        #     title="DB Data Message",
        #     message="Data inserted successfully",
        #     duration=3000,
        # )
        # toast.show_toast()



window = ctk.CTk()
window._set_appearance_mode('light')
window.title("Database Creation")
window.geometry('800x500')
 
main_frame = ctk.CTkFrame(window)
main_frame.place(relx = 0.5, rely = 0.5, anchor ='center', relwidth = 0.7, relheight = 0.7)

# Variables for value holding
name_value = tk.StringVar()
email_value = tk.StringVar()

# Widgets
name_label = ctk.CTkLabel(main_frame, text="Name")
name_entry = ctk.CTkEntry(main_frame, textvariable=name_value)
email_label = ctk.CTkLabel(main_frame, text="Email Address")
email_entry = ctk.CTkEntry(main_frame, textvariable=email_value)

# Buttons
login_btn = ctk.CTkButton(main_frame, text="Login", command=create_db)

# Layout
name_label.pack(pady = 4,)
name_entry.pack(pady = 4,)
email_label.pack(pady = 4,)
email_entry.pack(pady = 4,)

login_btn.pack(pady = 4, fill = 'x', padx = 90)

window.mainloop()