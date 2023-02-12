import pandas as pd
from tkinter import*
import productMenu
from tkinter import ttk,messagebox
import suppliers
import login
import employee
class MainMenuClass:
    def __init__(self):
        self.root=Toplevel()
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #==================title=====================================
        title=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",font=("times new roman",40, "bold"),bg="lightblue",fg="white").place(x=0, y=10,relwidth=1,height=70)

        #==================logout====================================
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15, "bold"),command=lambda: login.Loginform(window=self.root),bg="#2196f3",fg="white").place(x=1200, y=20,height=50,width=100)

        #==================Product Menu=================================
        MainFrame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
        MainFrame.place(x=500,y=110,width=410,height=550)

        pTitle=Label(MainFrame,text="Main Menu", font=("goudy old style", 20, "bold"),bg="lightblue",fg="white").pack(side=TOP,fill=X)

        btn_employee = Button(MainFrame, text="EMPLOYEE",font=("goudy old style", 15),command=lambda: employee.EmployeeClass(),bg="#2196f3",fg="white",cursor="hand2").place(x=50,y=160,height=50,width=300)
        btn_product = Button(MainFrame, text="PRODUCT",font=("goudy old style", 15),bg="#2196f3",fg="white",cursor="hand2", command=lambda: productMenu.ProductMenuClass(self.root)).place(x=50,y=260,height=50,width=300)
        btn_suppliers= Button(MainFrame, text="SUPPLIERS",font=("goudy old style", 15),bg="#2196f3",fg="white",cursor="hand2",command=lambda: suppliers.sup_run()).place(x=50,y=360,height=50,width=300)
def run1():
    if __name__=="__main__":
        root=Tk()
        obj=MainMenuClass()
        
        root.mainloop()
run1()

