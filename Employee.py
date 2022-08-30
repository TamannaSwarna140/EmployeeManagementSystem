from tkinter import*
from tkinter import ttk, messagebox
import tkinter as tk
import mysql.connector

def GetValue(event):
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    ent1.insert(0, select['Employee ID'])
    ent2.insert(0, select['Employee Name'])
    ent3.insert(0, select['Salary'])
    ent4.insert(0, select['Branch ID'])


def Add():
    empID = var1.get()
    Name = var2.get()
    salary = var3.get()
    branchID = var4.get()

    mydb = mysql.connector.connect(host='localhost',user="root",password="mypass",database="DBMSLAB")
    mycursor = mydb.cursor()

    try:
        sql = "INSERT INTO  Employee (empID,Name,Salary,branchID) VALUES (%s, %s, %s, %s)"
        val = (empID,Name,salary,branchID)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Employee Information Inserted successfully...")
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
        ent1.focus_set()
    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


def update():
    empID = var1.get()
    name = var2.get()
    salary = var3.get()
    branchID = var4.get()

    mydb = mysql.connector.connect(host='localhost', user="root", password="mypass", database="DBMSLAB")
    mycursor = mydb.cursor()

    try:
        sql = "Update  Employee set Name= %s,Salary= %s,branchID= %s where empID= %s"
        val = (name,salary,branchID,empID)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Record Updated successfully...")

        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
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
        sql = "DELETE FROM Employee WHERE empID = %s"
        val = (empID,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Record Deleted successfully...")

        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
        ent1.focus_set()

    except Exception as e:

        print(e)
        mydb.rollback()
        mydb.close()


def show():
    mydb = mysql.connector.connect(host='localhost', user="root", password="mypass", database="DBMSLAB")
    mycursor = mydb.cursor()
    sql = "SELECT empID,Name,Salary,branchID FROM Employee"
    mycursor.execute(sql)
    records = mycursor.fetchall()
    print(records)

    for i, (empID, Name, Salary, branchID) in enumerate(records, start=1):
        listBox.insert("", "end", values=(empID,Name,Salary,branchID))
        mydb.close()

def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent1.focus_set()


win = Tk()
win.title("Employee")
win.maxsize(width=800, height=500)
win.minsize(width=800, height=500)
my_label = Label(win, bg = "#C8C5C1")
my_label.place(x=0, y=0, relwidth=1, relheight=1)

global var1
global var2
global var3
global var4

tk.Label(win, text="Employee Information", fg="green", font=("Times New Roman", 30,"bold")).place(x=400, y=35)

# Employee ID
lbl1 = tk.Label(win, text="Employee ID", bg="navy blue", fg="white", width=15, height=1, font=("Arial", 10, "bold"))
lbl1.place(x=40, y=18)

var1 = StringVar()
ent1 = Entry(win, bg='white', fg='black', bd=3, textvariable=var1, width=30)
ent1.place(x=170, y=18)

# Employee Name
lbl2 = Label(win, text="Employee Name", bg="navy blue", fg="white", width=15, height=1, font=("Arial", 10, "bold"))
lbl2.place(x=40, y= 48)

var2 = StringVar()
ent2 = Entry(win, bg='White', fg='black', bd=2, textvariable=var2, width=30)
ent2.place(x=170, y= 48)

# Salary
lbl3 = Label(win, text="Salary", bg="navy blue", fg="white", width=15, height=1, font=("Arial", 10, "bold"))
lbl3.place(x=40, y= 78)

var3 = StringVar()
ent3 = Entry(win, bg='White', fg='black', bd=2, textvariable=var3, width=30)
ent3.place(x=170, y= 78)

# Branch ID

lbl4 = Label(win, text="Branch ID", bg="navy blue", fg="white", width=15, height=1, font=("Arial", 10, "bold"))
lbl4.place(x=40, y=108)

var4 = StringVar()
ent4 = Entry(win, bg='White', fg='black', bd=2, textvariable=var4, width=30)
ent4.place(x=170, y=108)



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

cols = ('Employee ID', 'Employee Name', 'Salary', 'Branch ID')
listBox = ttk.Treeview(win, columns=cols, show='headings')
listBox.column("Employee ID",width=190,)
listBox.column("Employee Name",width=190)
listBox.column("Salary",width=190)
listBox.column("Branch ID",width=190)

s = ttk.Style(win)
s.theme_use("clam")

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=20, y=250)


listBox.bind('<Double-Button-1>', GetValue)

win.mainloop()