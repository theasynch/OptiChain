import tkinter
from tkinter import PhotoImage
import sqlite3
from datetime import datetime
import tkinter.messagebox
import matplotlib.pyplot as plt


date = datetime.today().date()



def record_revenue():

    conn = sqlite3.connect("data.db")
    table_create_query = '''CREATE TABLE IF NOT EXISTS Revenue_Sheet 
                    (date STR, revenue INT)
            '''
    conn.execute(table_create_query)
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Revenue_Sheet")
    rows = cursor.fetchall()
    
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
    

    for row in rows:
        date, revenue = row
        if date == datetime.today().date():
            today_revenue = revenue

            app_frame = tkinter.LabelFrame(revenue_frame, text = "Add data")
            app_frame.grid(row = 1, column= 0, padx=20, pady=10)

            income_label = tkinter.Label(app_frame, text="Revenue (₹)")
            income_spinbox = tkinter.Spinbox(app_frame, from_=f"{today_revenue}", to='infinity')
            income_label.grid(row=2, column=0, padx= 10, pady=5)
            income_spinbox.grid(row=2, column=1, padx= 10, pady=5)
            data_insert_query = '''UPDATE Revenue_Sheet SET date = ?, revenue=?'''
            data_insert_tuple = (date, revenue)

        else:
            app_frame = tkinter.LabelFrame(revenue_frame, text = "Add data")
            app_frame.grid(row = 1, column= 0, padx=20, pady=10)

            income_label = tkinter.Label(app_frame, text="Revenue (₹)")
            income_spinbox = tkinter.Spinbox(app_frame, from_=1, to='infinity')
            income_label.grid(row=2, column=0, padx= 10, pady=5)
            income_spinbox.grid(row=2, column=1, padx= 10, pady=5)  
            data_insert_query = '''INSERT INTO Revenue_Sheet (date, revenue) VALUES (?, ?)'''
            data_insert_tuple = (date, revenue)

    def enter_revenue():
        revenue  = income_spinbox.get()
        print(type(revenue))
        if revenue=="69420":
            tkinter.messagebox.showinfo("Nice", "Nice.")
        else:
            pass
        conn = sqlite3.connect('data.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Revenue_Sheet 
                        (date TEXT, revenue INT)
                '''
        conn.execute(table_create_query)
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()

    button = tkinter.Button(revenue_frame, text="Enter data", command = enter_revenue)
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

    app_frame = tkinter.LabelFrame(inventory_frame, text = "Add data")
    app_frame.grid(row = 1, column= 0, padx=20, pady=10)

    conn = sqlite3.connect('data.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS SKU_Sheet 
                    (SKU87423 INT, SKU53982 INT, SKU21675 INT, SKU70148 INT, SKU38291 INT, SKU96574 INT)
            '''
    conn.execute(table_create_query)
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM SKU_Sheet")
    row = cursor.fetchone()

    
    SKU87423, SKU53982, SKU21675, SKU70148, SKU38291, SKU96574 = row
     

    inv_label = tkinter.Label(app_frame, text="SKU87423")
    inv_label.grid(row=0, column=0, padx= 10, pady=5)
    income_spinbox0 = tkinter.Spinbox(app_frame, from_=f"{SKU87423}", to='infinity')
    income_spinbox0.grid(row=1, column=0, padx= 10, pady=5)

    inv_label = tkinter.Label(app_frame, text="SKU53982")
    inv_label.grid(row=2, column=0, padx= 10, pady=5)
    income_spinbox1 = tkinter.Spinbox(app_frame, from_=f"{SKU53982}", to='infinity')
    income_spinbox1.grid(row=3, column=0, padx= 10, pady=5)

    inv_label = tkinter.Label(app_frame, text="SKU21675")
    inv_label.grid(row=4, column=0, padx= 10, pady=5)
    income_spinbox2 = tkinter.Spinbox(app_frame, from_=f"{SKU21675}", to='infinity')
    income_spinbox2.grid(row=5, column=0, padx= 10, pady=5)

    inv_label = tkinter.Label(app_frame, text="SKU70148")
    inv_label.grid(row=0, column=1, padx= 10, pady=5)
    income_spinbox3 = tkinter.Spinbox(app_frame, from_=f"{SKU70148}", to='infinity')
    income_spinbox3.grid(row=1, column=1, padx= 10, pady=5)

    inv_label = tkinter.Label(app_frame, text="SKU38291")
    inv_label.grid(row=2, column=1, padx= 10, pady=5)
    income_spinbox4 = tkinter.Spinbox(app_frame, from_=f"{SKU38291}", to='infinity')
    income_spinbox4.grid(row=3, column=1, padx= 10, pady=5)

    inv_label = tkinter.Label(app_frame, text="SKU96574")
    inv_label.grid(row=4, column=1, padx= 10, pady=5)
    income_spinbox5 = tkinter.Spinbox(app_frame, from_=f"{SKU96574}", to='infinity')
    income_spinbox5.grid(row=5, column=1, padx= 10, pady=5)

    def enter_inventory():
        revenue0  = income_spinbox0.get()
        revenue1  = income_spinbox1.get()
        revenue2  = income_spinbox2.get()
        revenue3  = income_spinbox3.get()
        revenue4  = income_spinbox4.get()
        revenue5  = income_spinbox5.get()
        
        # Insert Data
        data_insert_query = '''UPDATE SKU_Sheet SET SKU87423 = ?, SKU53982 = ?, SKU21675 = ?, SKU70148 = ?, SKU38291 = ?, SKU96574 = ?'''
        data_insert_tuple = (revenue0, revenue1, revenue2, revenue3, revenue4, revenue5)
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()
    button = tkinter.Button(inventory_frame, text="Enter data", command = enter_inventory)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


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


    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT date, revenue FROM Revenue_Sheet ORDER BY date DESC LIMIT 20")
    rows = cursor.fetchall()
    
    dates, revenues = zip(*rows)

    cursor.close()
    conn.close()
    dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

    plt.plot(dates, revenues, marker='o', linestyle='-')

    # Customize the plot
    plt.title('Date vs Revenue')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()

def logistics_info(): 
    log_window = tkinter.Toplevel(window)
    log_window.title("Logistics Information")
    log_frame  = tkinter.Frame(log_window)
    log_frame.pack()
    log_frame2 = tkinter.LabelFrame(log_frame, text= "Dictionary of all suppliers")
    log_frame2.grid(row=0, column=0, padx=20, pady=10)
    desc = "View all the current logisctics partners for your firm."
    log_frame2desc = tkinter.Label(log_frame2, text = desc, padx=20, pady=20, justify="left")
    log_frame2desc.pack()

    

def add_logistics():
        
    add_window = tkinter.Toplevel(window)
    add_window.title("Add New Supplier")
    add_frame = tkinter.Frame(add_window)
    add_frame.pack()
    add_frame2 = tkinter.LabelFrame(add_frame, text = "Description")
    add_frame2.grid(row=0, column=0, padx=20, pady=10)
    add_frame2desc = tkinter.Label(add_frame2, text = "Add a new contact entry in your database.\nFill in all the details and hit the Button!", padx=20, pady=20, justify="left")
    add_frame2desc.pack() 

    add_frame3 = tkinter.LabelFrame(add_frame, text="New Contact Form")
    add_frame3.grid(row=1, column=0, padx=20, pady=20)

    retail_label = tkinter.Label(add_frame3, text="Retailer Name")
    retail_entry = tkinter.Entry(add_frame3)
    retail_label.grid(row=0, column=0, padx= 10, pady=5)
    retail_entry.grid(row=0, column=1, padx= 10, pady=5)

    manager_label = tkinter.Label(add_frame3, text="Manager Name")
    manager_entry = tkinter.Entry(add_frame3)
    manager_label.grid(row=1, column=0, padx= 10, pady=5)
    manager_entry.grid(row=1, column=1, padx= 10, pady=5)
    
    contact_label = tkinter.Label(add_frame3, text="Contact Number")
    contact_entry = tkinter.Entry(add_frame3)
    contact_label.grid(row=2, column=0, padx= 10, pady=5)
    contact_entry.grid(row=2, column=1, padx= 10, pady=5)

    def addtodb():
        try:
            retailer = retail_entry.get()
            manager = manager_entry.get()
            contact = int(contact_entry.get())

            #ValueError(int):
            #    tkinter.messagebox.showwarning("Notice", "Contact number must be a 10 digit sequence")
            

            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Logistics 
                            (firm_name STR, manager STR, contact int)
                    '''
            conn.execute(table_create_query)
            
            # Insert Data
            data_insert_query = '''INSERT INTO Logistics (firm_name, manager, contact) VALUES (?, ?, ?)'''
            data_insert_tuple = (retailer, manager, contact)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
        except ValueError:
            tkinter.messagebox.showwarning("Notice", "Contact number must be a 10 digit sequence.")    


    button = tkinter.Button(add_frame, text="Add Contact", command = addtodb)
    button.grid(row=2, column=0, sticky="news", padx=20, pady=10)
    



window = tkinter.Tk()
window.title("OptiChain")

frame = tkinter.Frame(window)
frame.pack()




welcome_frame =tkinter.LabelFrame(frame, text="Welcome")
welcome_frame.grid(row= 1, column=0, padx=20, pady=10)

welcome_message = """
Welcome to OptiChain!

OptiChain is your all-in-one 
supply chain management solution. 
With OptiChain, you can 
track revenue, manage inventory, 
analyze sales growth, and 
optimize logistics to drive business success.

Get started by selecting options from the menu 
or exploring the analytics features.
"""

label_welcome = tkinter.Label(welcome_frame, text=welcome_message, padx=20, pady=20, justify="left")
label_welcome.pack()

features_frame = tkinter.LabelFrame(frame, text = "Apps",)
features_frame.grid(row= 2, column=0, padx=5, pady=20)
button_revenue = tkinter.Button(features_frame, text="Record Revenue", command= record_revenue)
button_revenue.grid(row=0, column=0, sticky="news", padx=30, pady=10)
button_inventory = tkinter.Button(features_frame, text="Inventory", command= inventory_window)
button_inventory.grid(row=0, column=1, sticky="news", padx=30, pady=10)
button_sales = tkinter.Button(features_frame, text="Growth Analysis", command= sales_pitch_window)
button_sales.grid(row=1, column=0, sticky="news", padx=30, pady=10)
button_logistics = tkinter.Button(features_frame, text="Logistics Info", command= logistics_info)
button_logistics.grid(row=1, column=1, sticky="news", padx=30, pady=10)
button = tkinter.Button(features_frame, text="Add Contact", command = add_logistics)
button.grid(row=2, column=0, sticky="news", padx=20, pady=10)


image_path = "OptiChain Res.png" 
image = PhotoImage(file=image_path)


image_label = tkinter.Label(frame, image=image, padx=70, pady=10)
image_label.grid(row  = 0, column= 0)


icon = "Icon.ico"
window.iconbitmap(False, icon)
window.mainloop()