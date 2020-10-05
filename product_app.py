import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
import mysql.connector

set_dpi_awareness()

Colour_primary = "#2e3f4f"

class ProductRegister(tk.Tk):
    #Creating GUI for data form 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self['background'] = Colour_primary

        self.title('New Product')
        self.geometry('300x300')
        self.resizable(False, False)

        order_number = tk.StringVar()
        item_number = tk.StringVar()
        employee_id = tk.StringVar()
        pieces = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        input_frame = ttk.Frame(self, style='Timer.TFrame')
        input_frame.grid(row=0, column=0, sticky='NSEW', padx=10, pady=(10,0))
    
        info_label = ttk.Label(input_frame, text="Please to register your product:")
        info_label.grid(row=0, column=0, columnspan=2, sticky='EW', padx=10, pady=(10,10))    

        order_label = ttk.Label(input_frame, text="Order Number: ")
        order_label.grid(row=1, column=0, sticky='W', padx=10, pady=(10,10))
        order_entry = ttk.Entry(input_frame, width=25, textvariable=order_number)
        order_entry.grid(row=1, column=1, sticky='W', padx=10,pady=(10,10))

        item_label = ttk.Label(input_frame, text="Item Number: ")
        item_label.grid(row=2, column=0, sticky='W', padx=10, pady=10)
        item_entry = ttk.Entry(input_frame, width=25, textvariable=item_number)
        item_entry.grid(row=2, column=1, sticky='W', padx=10, pady=10)

        employee_label = ttk.Label(input_frame, text="Employee ID: ")
        employee_label.grid(row=3, column=0, sticky='W', padx=10, pady=10)
        employee_entry = ttk.Entry(input_frame, width=25, textvariable=employee_id)
        employee_entry.grid(row=3, column=1, sticky='E', padx=10, pady=10)

        pieces_label = ttk.Label(input_frame, text="Quantity: ")
        pieces_label.grid(row=4, column=0, sticky='W', padx=10, pady=10)
        pieces_entry = ttk.Entry(input_frame, width=25, textvariable=pieces)
        pieces_entry.grid(row=4, column=1, sticky='E', padx=10, pady=10)

        button_frame = ttk.Frame(self, style='Timer.TFrame')
        button_frame.grid(row=1, column=0, sticky='EW', padx=10, pady=(0,10))
        button_frame.columnconfigure((0,1), weight=1)

        register_button = ttk.Button(button_frame, 
                                    text="Register",
                                    command= lambda : self.add_recorrd(order_number, item_number, employee_id, pieces)
                                    )
        register_button.grid(row=0, column=0, sticky='EW', padx=10, pady=10)
        cancel_button = ttk.Button(button_frame, text="Cancel", command=self.destroy)
        cancel_button.grid(row=0, column=1, sticky='EW', padx=10, pady=10)

    #This fucnction create conection between app and MySQL database and insert values from form to tabel. 
    def add_recorrd(self, orde, it, emp, pie):
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'mypass',
            database = 'test-schema'
            )
 
        my_cursor = mydb.cursor()
    
        my_cursor.execute("INSERT INTO products(order_num, item, employee_id, pieces) VALUES(%s,%s,%s,%s)", 
                         (str(orde.get()), str(it.get()), str(emp.get()), str(pie.get())))
        mydb.commit()
        my_cursor.close()
        mydb.close()
        self.destroy()

app = ProductRegister()
app.mainloop()