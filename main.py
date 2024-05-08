import tkinter
from tkinter import PhotoImage
import sqlite3
from datetime import datetime
import tkinter.messagebox
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

def record_revenue():
    """
    Function to record revenue in a database table.
    """
    conn = sqlite3.connect("data.db")
    table_create_query = """CREATE TABLE IF NOT EXISTS Revenue_Sheet 
                    (date STR, revenue INT)
            """
    conn.execute(table_create_query)

    cursor = conn.cursor()

    # Check if there is an entry for today's date
    cursor.execute("SELECT * FROM Revenue_Sheet WHERE date = ?", (datetime.today().date(),))
    existing_row = cursor.fetchone()

    revenue_window = tkinter.Toplevel(window)
    revenue_window.title("Record Revenue")
    revenue_frame = tkinter.Frame(revenue_window)
    revenue_frame.pack()
    desc_frame = tkinter.LabelFrame(revenue_frame, text="Description")
    desc_frame.grid(row=0, column=0, padx=20, pady=10)

    description = f"""
    Record total revenue income for today.
    Date : {datetime.today().date()}
    Time : {datetime.now().time()}
    """
    label_description = tkinter.Label(
        desc_frame, text=description, padx=10, pady=20, justify="left"
    )
    label_description.pack()

    
    app_frame = tkinter.LabelFrame(revenue_frame, text="Add data")
    app_frame.grid(row=1, column=0, padx=20, pady=10)

    income_label = tkinter.Label(app_frame, text="Revenue (₹)")
    income_spinbox = tkinter.Spinbox(app_frame, from_=1, to="infinity")
    income_label.grid(row=2, column=0, padx=10, pady=5)
    income_spinbox.grid(row=2, column=1, padx=10, pady=5)
    data_insert_query = (
        """INSERT INTO Revenue_Sheet (date, revenue) VALUES (?, ?)"""
    )
    data_insert_tuple = (datetime.today().date(), income_spinbox.get())

    def enter_revenue():
        """
        Function to enter revenue data into the database.
        """
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()
        # Close the revenue window after data is entered
        revenue_window.destroy()

    button = tkinter.Button(revenue_frame, text="Enter data", command=enter_revenue)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

def inventory_window():
    """
    Opens a new window to manage inventory and update SKU quantities.
    """
    inventory_window = tkinter.Toplevel(window)
    inventory_window.title("Manage Inventory")
    inventory_frame = tkinter.Frame(inventory_window)
    inventory_frame.pack()
    
    desc_frame = tkinter.LabelFrame(inventory_frame, text="Description")
    desc_frame.grid(row=0, column=0, padx=20, pady=10)

    description = "Manage inventory for the below SKU units.\nUse the spinboxes to edit the quantity numbers\nof each SKUs"
    label_description = tkinter.Label(
        desc_frame, text=description, padx=27, pady=20, justify="left"
    )
    label_description.pack()

    app_frame = tkinter.LabelFrame(inventory_frame, text="Add data")
    app_frame.grid(row=1, column=0, padx=20, pady=10) 

    conn = sqlite3.connect("data.db")
    table_create_query = """CREATE TABLE IF NOT EXISTS SKU_Sheet 
                    (SKU87423 INT, SKU53982 INT, SKU21675 INT, SKU70148 INT, SKU38291 INT, SKU96574 INT)
            """
    conn.execute(table_create_query)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM SKU_Sheet")
    row = cursor.fetchone()

    SKU87423, SKU53982, SKU21675, SKU70148, SKU38291, SKU96574 = row

    inv_label = tkinter.Label(app_frame, text="SKU87423")
    inv_label.grid(row=0, column=0, padx=10, pady=5)
    income_spinbox0 = tkinter.Spinbox(app_frame, from_=f"{SKU87423}", to="infinity")
    income_spinbox0.grid(row=1, column=0, padx=10, pady=5)

    inv_label = tkinter.Label(app_frame, text="SKU53982")
    inv_label.grid(row=2, column=0, padx=10, pady=5)
    income_spinbox1 = tkinter.Spinbox(app_frame, from_=f"{SKU53982}", to="infinity")
    income_spinbox1.grid(row=3, column=0, padx=10, pady=5)

    inv_label = tkinter.Label(app_frame, text="SKU21675")
    inv_label.grid(row=4, column=0, padx=10, pady=5)
    income_spinbox2 = tkinter.Spinbox(app_frame, from_=f"{SKU21675}", to="infinity")
    income_spinbox2.grid(row=5, column=0, padx=10, pady=5)

    inv_label = tkinter.Label(app_frame, text="SKU70148")
    inv_label.grid(row=0, column=1, padx=10, pady=5)
    income_spinbox3 = tkinter.Spinbox(app_frame, from_=f"{SKU70148}", to="infinity")
    income_spinbox3.grid(row=1, column=1, padx=10, pady=5)

    inv_label = tkinter.Label(app_frame, text="SKU38291")
    inv_label.grid(row=2, column=1, padx=10, pady=5)
    income_spinbox4 = tkinter.Spinbox(app_frame, from_=f"{SKU38291}", to="infinity")
    income_spinbox4.grid(row=3, column=1, padx=10, pady=5)

    inv_label = tkinter.Label(app_frame, text="SKU96574")
    inv_label.grid(row=4, column=1, padx=10, pady=5)
    income_spinbox5 = tkinter.Spinbox(app_frame, from_=f"{SKU96574}", to="infinity")
    income_spinbox5.grid(row=5, column=1, padx=10, pady=5)

    def enter_inventory():
        """
        Updates the SKU quantities in the database based on the values entered in the spinboxes.
        """
        revenue0 = income_spinbox0.get()
        revenue1 = income_spinbox1.get()
        revenue2 = income_spinbox2.get()
        revenue3 = income_spinbox3.get()
        revenue4 = income_spinbox4.get()
        revenue5 = income_spinbox5.get()

        # Insert Data
        data_insert_query = """UPDATE SKU_Sheet SET SKU87423 = ?, SKU53982 = ?, SKU21675 = ?, SKU70148 = ?, SKU38291 = ?, SKU96574 = ?"""
        data_insert_tuple = (revenue0, revenue1, revenue2, revenue3, revenue4, revenue5)
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()

    button = tkinter.Button(inventory_frame, text="Enter data", command=enter_inventory)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


def sales_pitch_window():
    """
    Opens a new window to display the sales pitch graph.

    Retrieves the last 20 revenue entries from the database and plots them on a graph.

    Args:
        None

    Returns:
        None
    """
    # Create a new window
    sales_window = tkinter.Toplevel(window)
    sales_window.title("View Sales Pitch")

    # Create a frame for the sales window
    sales_frame = tkinter.Frame(sales_window)
    sales_frame.pack()

    # Create a label frame for the description
    desc_frame = tkinter.LabelFrame(sales_frame, text="Description")
    desc_frame.grid(row=0, column=0, padx=20, pady=10)

    # Set the description text
    description = "View the sales graph over time.\nNOTE: The graph shows data only for the last 20 revenue entries"
    label_description = tkinter.Label(
        desc_frame, text=description, padx=20, pady=20, justify="left"
    )
    label_description.pack()

    # Connect to the database
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    # Retrieve the last 20 revenue entries from the database
    cursor.execute(
        "SELECT date, revenue FROM Revenue_Sheet ORDER BY date DESC LIMIT 20"
    )
    rows = cursor.fetchall()

    # Separate the dates and revenues into separate lists
    dates, revenues = zip(*rows)

    # Close the database connection
    cursor.close()
    conn.close()

    # Convert the dates to datetime objects
    dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]

    # Plot the dates and revenues on a graph
    plt.plot(dates, revenues, marker="o", linestyle="-")

    # Customize the plot
    plt.title("Date vs Revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()


def logistics_info():
    """
    Retrieves and displays logistics information from the database.
    """
    conn = sqlite3.connect("data.db")  # Connect to the database

    # Create the Logistics table if it doesn't exist
    table_create_query = """CREATE TABLE IF NOT EXISTS Logistics 
                    (firm_name STR, manager STR, contact int)
            """
    conn.execute(table_create_query)

    log_window = tkinter.Toplevel(window)  # Create a new window for displaying logistics information
    log_window.title("Logistics Information")

    log_frame = tkinter.Frame(log_window)  # Create a frame within the window
    log_frame.pack()

    log_frame2 = tkinter.LabelFrame(log_frame, text="Dictionary of all suppliers")  # Create a labeled frame within the main frame
    log_frame2.grid(row=0, column=0, padx=20, pady=10)

    desc = "View all the current logistics partners for your firm."
    log_frame2desc = tkinter.Label(
        log_frame2, text=desc, padx=20, pady=20, justify="left"
    )
    log_frame2desc.pack()  # Display the description within the labeled frame

    conn = sqlite3.connect("data.db")  # Connect to the database again
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Logistics")  # Retrieve all rows from the Logistics table
    rows = cursor.fetchall()

    if len(rows) == 0:  # If there are no rows in the table
        app_frame = tkinter.LabelFrame(log_frame)
        app_frame.grid(row=1, column=0, padx=20, pady=10)

        manager_label = tkinter.Label(app_frame, text="Hmmm, looks like there are no stored contacts.\nGo back to the home page and use the 'Add Contact'\napp to add a new contact.", padx=20, pady=20, justify="left")
        manager_label.pack()  # Display a message indicating no stored contacts

    else:  # If there are rows in the table
        for i, row in enumerate(rows, start=1):  # Iterate over each row
            retailer, manager, contact = row

            app_frame = tkinter.LabelFrame(log_frame, text=f"{retailer}")  # Create a labeled frame for each retailer
            app_frame.grid(row=i, column=0, padx=20, pady=10)

            manager_label = tkinter.Label(app_frame, text=f"Manager Name: {manager}")
            contact_label = tkinter.Label(
                app_frame, text=f"Contact: {str(contact)}"
            )
            manager_label.grid(row=0, column=0, padx=13, pady=5)
            contact_label.grid(row=0, column=1, padx=13, pady=5)  # Display the manager name and contact within the labeled frame
        


def add_logistics():
    """
    Function to add logistics information to the database.
    """
    add_window = tkinter.Toplevel(window)
    add_window.title("Add New Supplier")
    add_frame = tkinter.Frame(add_window)
    add_frame.pack()
    
    add_frame2 = tkinter.LabelFrame(add_frame, text="Description")
    add_frame2.grid(row=0, column=0, padx=20, pady=10)
    add_frame2desc = tkinter.Label(
        add_frame2,
        text="Add a new contact entry in your database.\nFill in all the details and hit the Button!",
        padx=20,
        pady=20,
        justify="left",
    )
    add_frame2desc.pack()

    add_frame3 = tkinter.LabelFrame(add_frame, text="New Contact Form")
    add_frame3.grid(row=1, column=0, padx=20, pady=20)

    retail_label = tkinter.Label(add_frame3, text="Retailer Name")
    retail_entry = tkinter.Entry(add_frame3)
    retail_label.grid(row=0, column=0, padx=10, pady=5)
    retail_entry.grid(row=0, column=1, padx=10, pady=5)

    manager_label = tkinter.Label(add_frame3, text="Manager Name")
    manager_entry = tkinter.Entry(add_frame3)
    manager_label.grid(row=1, column=0, padx=10, pady=5)
    manager_entry.grid(row=1, column=1, padx=10, pady=5)

    contact_label = tkinter.Label(add_frame3, text="Contact Number")
    contact_entry = tkinter.Entry(add_frame3)
    contact_label.grid(row=2, column=0, padx=10, pady=5)
    contact_entry.grid(row=2, column=1, padx=10, pady=5)

    def addtodb():
        """
        Function to add the entered logistics information to the database.
        """
        try:
            retailer = retail_entry.get()
            manager = manager_entry.get()
            contact = int(contact_entry.get())

            conn = sqlite3.connect("data.db")
            table_create_query = """CREATE TABLE IF NOT EXISTS Logistics 
                            (firm_name STR, manager STR, contact STR)
                    """
            conn.execute(table_create_query)

            # Insert Data
            data_insert_query = """INSERT INTO Logistics (firm_name, manager, contact) VALUES (?, ?, ?)"""
            data_insert_tuple = (retailer, manager, str(contact))
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
        except ValueError:
            tkinter.messagebox.showwarning(
                "Notice", "Contact number must be a 10 digit sequence."
            )

    button = tkinter.Button(add_frame, text="Add Contact", command=addtodb)
    button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

def export():
    """
    Export data from SQLite database to an Excel file.
    """

    # Connect to the SQLite database
    conn = sqlite3.connect("data.db")

    # Create an Excel writer object
    excel_writer = pd.ExcelWriter("data.xlsx", engine="openpyxl")

    # Create a dictionary to store the dataframes for each table
    dataframes = {}

    # List of tables to export
    tables = ["Revenue_Sheet", "SKU_Sheet", "Logistics"]

    # Iterate over each table and retrieve the data as a dataframe
    for table in tables:
        dataframes[table] = pd.read_sql_query(f"SELECT * FROM {table}", conn)

    # Write each dataframe to a separate sheet in the Excel file
    for table, df in dataframes.items():
        df.to_excel(excel_writer, sheet_name=table, index=False)

    # Close the Excel writer and the database connection
    excel_writer.close()
    conn.close()

    # Open the exported Excel file
    subprocess.Popen("data.xlsx", shell=True)

    # Show a message box indicating the export is completed
    tkinter.messagebox.showinfo("Action Completed", "Your data has been exported successfully as 'data.xlsx'")

window = tkinter.Tk()
window.title("OptiChain")

frame = tkinter.Frame(window)
frame.pack()


welcome_frame = tkinter.LabelFrame(frame, text="Welcome")
welcome_frame.grid(row=1, column=0, padx=20, pady=10)

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

label_welcome = tkinter.Label(
    welcome_frame, text=welcome_message, padx=20, pady=20, justify="left"
)
label_welcome.pack()

features_frame = tkinter.LabelFrame(
    frame,
    text="Apps",
)
features_frame.grid(row=2, column=0, padx=5, pady=20)
button_revenue = tkinter.Button(
    features_frame, text="Record Revenue", command=record_revenue
)
button_revenue.grid(row=0, column=0, sticky="news", padx=30, pady=10)
button_inventory = tkinter.Button(
    features_frame, text="Inventory", command=inventory_window
)
button_inventory.grid(row=0, column=1, sticky="news", padx=30, pady=10)
button_sales = tkinter.Button(
    features_frame, text="Growth Analysis", command=sales_pitch_window
)
button_sales.grid(row=1, column=0, sticky="news", padx=30, pady=10)
button_logistics = tkinter.Button(
    features_frame, text="Logistics Info", command=logistics_info
)
button_logistics.grid(row=2, column=0, sticky="news", padx=30, pady=10)
button = tkinter.Button(features_frame, text="Add Contact", command=add_logistics)
button.grid(row=2, column=1, sticky="news", padx=20, pady=10)


button = tkinter.Button(features_frame, text="Export Data", command=export)
button.grid(row=1, column=1, sticky="news", padx=20, pady=10)


image_path = "OptiChain Res.png"
image = PhotoImage(file=image_path)


image_label = tkinter.Label(frame, image=image, padx=70, pady=10)
image_label.grid(row=0, column=0)


icon = "Icon.ico"
window.iconbitmap(False, icon)
window.mainloop()