import tkinter
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        skunumber = skunumber_entry.get()
        date = date_calender.get_date()
        category = category_entry.get()
        
        if skunumber and category:
            category = category_entry .get()
            quantity = quantity_spinbox.get()
            price = price_combobox.get()
            
            # Course info
            registration_status = reg_status_var.get()
            numsemesters = date_calender.get_date()
            
            print("First name: ", skunumber, "Last name: ", category)
            print("Category: ", category, "Quantity ", quantity, "Price per unit ", price)
            print("Date", date)
            print("------------------------------------------")
            
            # Create Table
            conn = sqlite3.connect('data1.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (date TEXT, skunumber TEXT, category TEXT, quantity INT,  price INT, 
                    registration_status TEXT)
            '''
            conn.execute(table_create_query)
            
            # Insert Data
            data_insert_query = '''INSERT INTO Student_Data (date, skunumber, category, quantity, 
            price, registration_status) VALUES 
            (?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (date, skunumber, category, quantity, price, registration_status)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

            
                
        else:
            tkinter.messagebox.showwarning(title="Error", message="SKU Number and last name are required.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Revenue Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="Product Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

skunumber_label = tkinter.Label(user_info_frame, text="SKU Number")
skunumber_label.grid(row=0, column=0)

category_label =tkinter.Label(user_info_frame, text = "Category")
category_label.grid(row = 0, column = 1)

skunumber_entry = tkinter.Entry(user_info_frame)
category_entry = ttk.Combobox(user_info_frame, values=["", "Beverages", "Snacks", "Lavatories"])
skunumber_entry.grid(row=1, column=0)
category_entry.grid(row=1, column=1)

quantity_label = tkinter.Label(user_info_frame, text="Quantity")
quantity_spinbox = tkinter.Spinbox(user_info_frame, from_=1, to='infinity')
quantity_label.grid(row=2, column=0)
quantity_spinbox.grid(row=3, column=0)

price_label = tkinter.Label(user_info_frame, text="Price Per Unit (₹)")
price_combobox = tkinter.Spinbox(user_info_frame, from_ = 1, to= 3000)
price_label.grid(row=2, column=1)
price_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)


date_label = tkinter.Label(courses_frame, text="# Semesters")
date_calender = Calendar(courses_frame, selectmode="day", date_pattern="yyyy-mm-dd")
date_label.grid(row=0, column=2)
date_calender.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()