import pandas as pd
from tkinter import*
import searchProduct
import newProduct
import deletproduct
import MainMenu
from tkinter import ttk,messagebox
class ProductMenuClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #==================title=====================================
        title=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",font=("times new roman",40, "bold"),bg="lightblue",fg="white").place(x=0, y=10,relwidth=1,height=70)

        #==================logout====================================
        btn_back=Button(self.root,text="BACK",font=("times new roman",15, "bold"),bg="#2196f3",fg="white",command=lambda: MainMenu.MainMenuClass()).place(x=10, y=20,height=50,width=100)

        #==================Product Menu=================================
        MainFrame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
        MainFrame.place(x=330,y=110,width=750,height=550)

        pTitle=Label(MainFrame,text="PRODUCT MENU", font=("goudy old style", 20, "bold"),bg="lightblue",fg="white").pack(side=TOP,fill=X)

        btn_search = Button(MainFrame, text="Search/Show Product",font=("goudy old style", 15),bg="#2196f3",fg="white",cursor="hand2", command=lambda: searchProduct.SearchProductClass(self.root)).place(x=220,y=160,height=50,width=300)
        btn_add_product = Button(MainFrame, text="Add New Product",font=("goudy old style", 15),bg="#2196f3",fg="white",cursor="hand2", command=lambda: newProduct.NewProductClass(self.root)).place(x=220,y=260,height=50,width=300)
        btn_del_product = Button(MainFrame, text="Delete Product",font=("goudy old style", 15),command=lambda: deletproduct.DeleteProductClass(self.root),bg="#2196f3",fg="white",cursor="hand2").place(x=220,y=360,height=50,width=300)


if __name__=="__main__":
    root=Tk()
    obj=ProductMenuClass(root)
    root.mainloop()