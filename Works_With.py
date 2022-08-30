from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector



def GetValue(event):
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    ent1.insert(0, select['Employee ID'])
    ent2.insert(0, select['Client ID'])
    ent3.insert(0, select['Total Sales'])


def Add():
    empID = var1.get()
    clientID = var2.get()
    totalSales = var3.get()

    mydb = mysql.connector.connect(host='localhost',user="root",password="mypass",database="DBMSLAB")
    mycursor = mydb.cursor()

    try:
        sql = "INSERT INTO  Works_With (empID,clientID,totalSales) VALUES (%s, %s, %s)"
        val = (empID,clientID,totalSales)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Works With Table Information Inserted successfully...")
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent1.focus_set()
    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def update():
    empID = var1.get()
    clientID = var2.get()
    totalSales = var3.get()

    mydb = mysql.connector.connect(host='localhost', user="root", password="mypass", database="DBMSLAB")
    mycursor = mydb.cursor()

    try:
        sql = "Update  Works_With set clientID = %s,totalSales = %s where empID= %s"
        val = (clientID,totalSales,empID)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Information Updated successfully...")

        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent1.focus_set()

    except Exception as e:

        print(e)
        mydb.rollback()
        mydb.close()


def delete():
    empID = var1.get()

    mydb = mysql.connector.connect(host='localhost', user="root", password="mypass", database="DBMSLAB")
    mycursor = mydb.cursor()

    try:
        sql = "DELETE FROM Works_With WHERE empID = %s"
        val = (empID,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Information Deleted successfully...")

        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent1.focus_set()

    except Exception as e:

        print(e)
        mydb.rollback()
        mydb.close()


def show():
    mydb = mysql.connector.connect(host='localhost', user="root", password="mypass", database="DBMSLAB")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM Works_With"
    mycursor.execute(sql)
    records = mycursor.fetchall()
    print(records)

    for i, (empID, clientID, totalSales) in enumerate(records, start=1):
        listBox.insert("", "end", values=(empID,clientID,totalSales))
        mydb.close()

def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent1.focus_set()


win = Tk()
win.title("Works_With")
win.maxsize(width=800, height=500)
win.minsize(width=800, height=500)
my_label = Label(win, bg = "#C8C5C1")
my_label.place(x=0, y=0, relwidth=1, relheight=1)

global var1
global var2
global var3

tk.Label(win, text="WorksWith Information", fg="green", font=("Times New Roman",30,"bold")).place(x=370, y=40)

# employee ID
lbl1 = tk.Label(win, text="Employee ID", bg="navy blue", fg="white", width=12, height=1, font=("Arial", 10, "bold"))
lbl1.place(x=50, y=40)

var1 = StringVar()
ent1 = Entry(win, bg='white', fg='black', bd=3, textvariable=var1, width=30)
ent1.place(x=170, y=40)

# Client ID
lbl2 = Label(win, text="Client ID", bg="navy blue", fg="white", width=12, height=1, font=("Arial", 10, "bold"))
lbl2.place(x=50, y= 70)

var2 = StringVar()
ent2 = Entry(win, bg='White', fg='black', bd=2, textvariable=var2, width=30)
ent2.place(x=170, y= 70)

# Total Sales
lbl3 = Label(win, text="Total Sales", bg="navy blue", fg="white", width=12, height=1, font=("Arial", 10, "bold"))
lbl3.place(x=50, y= 100)

var3 = StringVar()
ent3 = Entry(win, bg='White', fg='black', bd=2, textvariable=var3, width=30)
ent3.place(x=170, y= 100)


#  Add button
btn = Button(win, text="ADD",command = Add, bg="navy blue", width=8, height=2, fg="white", font=("Arial", 16, "bold"))
btn.place(x=120, y=145)

# UPDATE button
btn = Button(win, text="UPDATE",command=update, bg="navy blue", width=8, height=2, fg="white", font=("Arial", 16, "bold"))
btn.place(x=290, y=145)

# DELETE button
btn = Button(win, text="DELETE",command=delete, bg="navy blue", width=8, height=2, fg="white", font=("Arial", 16, "bold"))
btn.place(x=460, y=145)

# show button
btn = Button(win, text="Show All",command=show, bg="navy blue", width=8, height=1, fg="white", font=("Arial", 12, "bold"))
btn.place(x= 650, y=145)

# Clear button
btn = Button(win, text="Clear", command=clear, bg="navy blue", width=8, height=1, fg="white", font=("Arial", 12, "bold"))
btn.place(x= 650, y=180)

cols = ('Employee ID', 'Client ID', 'Total Sales')
listBox = ttk.Treeview(win, columns=cols, show='headings')
listBox.column("Employee ID",width=240,)
listBox.column("Client ID",width=240)
listBox.column("Total Sales",width=240)

s = ttk.Style(win)
s.theme_use("clam")

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=40, y=250)


listBox.bind('<Double-Button-1>', GetValue)

win.mainloop()