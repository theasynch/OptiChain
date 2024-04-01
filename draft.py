import tkinter
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt




def record_revenue():
    revenue_window = tkinter.Toplevel(window)
    revenue_window.title("Record Revenue")
    revenue_frame = tkinter.Frame(revenue_window)
    revenue_frame.pack()
    desc_frame = tkinter.LabelFrame(revenue_frame,text= "Description")
    desc_frame.grid(row= 0, column=0, padx=20, pady=10)

    description  = f"""
    Record total revenue income for today.
    Date : {datetime.today().date()}
    Time : {datetime.now().time()}
    """
    label_description = tkinter.Label(desc_frame, text=description, padx=10, pady=20, justify="left")
    label_description.pack()
    
    app_frame = tkinter.LabelFrame(revenue_frame, text = "Add data")
    app_frame.grid(row = 1, column= 0, padx=20, pady=10)

    income_label = tkinter.Label(app_frame, text="Revenue (₹)")
    income_spinbox = tkinter.Spinbox(app_frame, from_=1, to='infinity')
    income_label.grid(row=2, column=0, padx= 10, pady=5)
    income_spinbox.grid(row=2, column=1, padx= 10, pady=5)

    button = tkinter.Button(revenue_frame, text="Enter data")
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)






def inventory_window():
    inventory_window = tkinter.Toplevel(window)
    inventory_window.title("Manage Inventory")
    inventory_frame = tkinter.Frame(inventory_window)
    inventory_frame.pack()
    desc_frame = tkinter.LabelFrame(inventory_frame,text= "Description")
    desc_frame.grid(row= 0, column=0, padx=20, pady=10)

    description  = "Manage iventory for the below SKU units.\nUse the spinboxes to edit the quantity numbers of each SKUs"
    label_description = tkinter.Label(desc_frame, text=description, padx=20, pady=20, justify="left")
    label_description.pack()    


def sales_pitch_window():
    sales_window = tkinter.Toplevel(window)
    sales_window.title("View Sales Pitch")
    sales_frame = tkinter.Frame(sales_window)
    sales_frame.pack()
    desc_frame = tkinter.LabelFrame(sales_frame, text = "Description")
    desc_frame.grid(row=0, column=0, padx=20, pady=10)

    
    description = "View the sales graph over time.\nFor each SKU unit indivisually or the sales graph of the entire firm at once."
    label_description = tkinter.Label(desc_frame, text=description, padx=20, pady=20, justify="left")
    label_description.pack()


def logistics_info(): 
    log_window = tkinter.Toplevel(window)
    log_window.title("Logistics Information")
    log_frame  = tkinter.Frame(log_window)
    log_frame.pack()
    log_frame = tkinter.LabelFrame(log_frame, text= "Dictionary of all suppliers")
    log_frame.grid(row=0, column=0, padx=20, pady=10)
    
    



window = tkinter.Tk()
window.title("OptiChain")

frame = tkinter.Frame(window)
frame.pack()




user_info_frame =tkinter.LabelFrame(frame, text="Welcome")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

welcome_message = """
Welcome to OptiChain!

OptiChain is your all-in-one supply chain management solution. 
With OptiChain, you can track revenue, manage inventory, 
analyze sales growth, and optimize logistics to drive business success.

Get started by selecting options from the menu or exploring the analytics features.

                                                                                       - theasynch
"""

label_welcome = tkinter.Label(user_info_frame, text=welcome_message, padx=20, pady=20, justify="left")
label_welcome.pack()

features_frame = tkinter.LabelFrame(frame, text = "Apps")
features_frame.grid(row= 1, column=0, padx=20, pady=10)
button_revenue = tkinter.Button(features_frame, text="Record Revenue", command= record_revenue)
button_revenue.grid(row=0, column=0, sticky="news", padx=20, pady=10)
button_inventory = tkinter.Button(features_frame, text="Inventory", command= inventory_window)
button_inventory.grid(row=0, column=1, sticky="news", padx=20, pady=10)
button_sales = tkinter.Button(features_frame, text="Sales Pitch", command= sales_pitch_window)
button_sales.grid(row=1, column=0, sticky="news", padx=20, pady=10)
button_logistics = tkinter.Button(features_frame, text="Logistics Info", command= logistics_info)
button_logistics.grid(row=1, column=1, sticky="news", padx=20, pady=10)



window.mainloop()