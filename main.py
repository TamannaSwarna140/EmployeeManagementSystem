from tkinter import*
from tkinter import ttk, messagebox
import tkinter as tk
import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' ,user= "root" ,password = "mypass" ,database = "DBMSLAB"
)

mycursor = mydb.cursor()

"""
# Creating Database:
sql="CREATE DATABASE DBMSLAB"
mycursor.execute(sql)

# Creating Table Employee:
sql1 = "CREATE TABLE Employee(empID int(20) PRIMARY KEY,Name varchar(30),salary INT(30),branchID int(10))"
mycursor.execute(sql1)

# Creating Table Branch:
sql2 = "CREATE TABLE Branch(branchID int(20) PRIMARY KEY,branchName varchar(30),mngrID INT(30),mngr_st_date Date)"
mycursor.execute(sql2)

# Creating Table Client
sql3 = "CREATE TABLE Client(clientID int(20) PRIMARY KEY,clientName varchar(30),branchID int(10))"
mycursor.execute(sql3)

# Creating Works With table:
sql4 = "CREATE TABLE Works_With(empID int(20),clientID int(20),totalSales int (30))"
mycursor.execute(sql4)

# Update Table with photo and resume:
sql5 = "UPDATE Employee SET Photo = %s, Res = %s WHERE empID = %s"
val5 = (convertPic,convertfile,100)

sql6 = "UPDATE Employee SET Photo = %s, Res = %s WHERE empID = %s"
val6 = (convertPic,convertfile,101)

sql7 = "UPDATE Employee SET Photo = %s, Res = %s WHERE empID = %s"
val7 = (convertPic,convertfile,102)

mycursor.execute(sql7,val7)

sql = "UPDATE Employee SET Photo = %s, Res = %s WHERE empID = %s"
val = (convertPic,convertfile,104)

sql = "UPDATE Employee SET Photo = %s, Res = %s WHERE empID = %s"
val = (convertPic,convertfile,105)

sql = "UPDATE Employee SET Photo = %s, Res = %s WHERE empID = %s"
val = (convertPic,convertfile,106)
sql = "UPDATE Employee SET Photo = %s, Res = %s WHERE empID = %s"
val = (convertPic,convertfile,107)
"""
def convertToBinary(filename):
    with open(filename,'rb') as file:
        binarydata = file.read()

    return binarydata

def convertBinaryToFile(binarydata,filename):
    with open(filename,'wb') as file:
        file.write(binarydata)


ctoBiPhoto= convertToBinary('D:\dbmsphoto/16.webp')
ctOBiFile= convertToBinary("D:\dbmsphoto/14.png")

#sql = "UPDATE Employee SET Photo = %s, Res = %s WHERE empID = %s"
#val = (convertPic,convertfile,107)

#mycursor.execute(sql,val)
#sql = "SELECT Photo , Res FROM Employee WHERE empID=107"
#mydb.commit()
#for x in mycursor:
#    print(x)
#mydb.commit()
convertPhoto = "D:\phototest/test.webp"
convertFile = "D:\phototest/test71.png"
sql = "SELECT * FROM Employee WHERE empID=%s"
val = (107,)
mycursor.execute(sql,val)
records = mycursor.fetchall()
#print(records)

for i in records:
    print("empID",i[0],"Name",i[1])
    pic = convertBinaryToFile(i[4],convertPhoto)
    resume = convertBinaryToFile(i[5],convertFile)
    mydb.close()


