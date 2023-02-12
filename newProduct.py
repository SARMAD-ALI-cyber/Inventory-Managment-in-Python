import pandas as pd
from tkinter import*
from tkinter import ttk,messagebox
import productMenu
class NewProductClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #==================title=====================================
        title=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",font=("times new roman",40, "bold"),bg="lightblue",fg="white").place(x=0, y=10,relwidth=1,height=70)
        btn_back=Button(self.root,text="BACK",font=("times new roman",15, "bold"),bg="#2196f3",fg="white",command=lambda: productMenu.ProductMenuClass(root)).place(x=10, y=20,height=50,width=100)
        
        #==================Product Menu==============================
        MainFrame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
        MainFrame.place(x=330,y=110,width=750,height=550)
            
        pTitle=Label(MainFrame,text="ADD NEW PRODUCT", font=("goudy old style", 20, "bold"),bg="lightblue",fg="white").pack(side=TOP,fill=X)

        self.var_PId=StringVar()
        self.var_PName=StringVar()
        self.var_PPrice=StringVar()
        self.var_PCategory=StringVar()
        self.var_PSupplier=StringVar()
        self.var_PStock=StringVar()

        lbl_PId = Label(MainFrame, text="Product ID ", font=("times new roman", 18, "bold"), bg="lightgray").place(x=220, y=100)
        txt_PId = Entry(MainFrame, textvariable=self.var_PId, font=("times new roman", 18), bg="white").place(x=370, y=100, width=180)
        lbl_PName = Label(MainFrame, text="Name ", font=("times new roman", 18, "bold"), bg="lightgray").place(x=220, y=150)
        txt_PName = Entry(MainFrame, textvariable=self.var_PName, font=("times new roman", 18), bg="white").place(x=370, y=150, width=180)
        lbl_PPrice = Label(MainFrame, text="Price ", font=("times new roman", 18, "bold"), bg="lightgray").place(x=220, y=200)
        txt_PPrice = Entry(MainFrame, textvariable=self.var_PPrice, font=("times new roman", 18), bg="white").place(x=370, y=200, width=180)
        lbl_PCategory = Label(MainFrame, text="Category ", font=("times new roman", 18, "bold"), bg="lightgray").place(x=220, y=250)
        txt_PCategory = Entry(MainFrame, textvariable=self.var_PCategory, font=("times new roman", 18), bg="white").place(x=370, y=250, width=180)
        lbl_PSupplier = Label(MainFrame, text="Supplier ", font=("times new roman", 18, "bold"), bg="lightgray").place(x=220, y=300)
        txt_Supplier = Entry(MainFrame, textvariable=self.var_PSupplier, font=("times new roman", 18), bg="white").place(x=370, y=300, width=180)
        lbl_PStock = Label(MainFrame, text="Stock ", font=("times new roman", 18, "bold"), bg="lightgray").place(x=220, y=350)
        txt_PStock = Entry(MainFrame, textvariable=self.var_PStock, font=("times new roman", 18), bg="white").place(x=370, y=350, width=180)

        btn_search = Button(MainFrame, text="Save Product",font=("goudy old style", 18, "bold"),command=self.add_product,bg="#2196f3",fg="white",cursor="hand2").place(x=55,y=450,width=300,height=50)

    def add_product(self):
        if self.var_PId.get()=="" or self.var_PId.get()=="" or self.var_PPrice.get()=="" or self.var_PCategory.get()=="" or self.var_PSupplier.get()=="" or self.var_PStock.get()=="":
            messagebox.showerror("Error","Fill all required blanks",parent=self.root)
        else:
            product = {'ID': [self.var_PId.get()], 'Name': [self.var_PName.get()], 'Price': [self.var_PPrice.get()], 'Stock': [self.var_PCategory.get()], 'Category': [self.var_PSupplier.get()],
                    'Supplier': [self.var_PStock.get()]}
            df = pd.DataFrame(product)
            df.to_csv("Product.csv", mode='a', index=False, header=False)
            messagebox.showinfo("Saved","New product added successfully",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=NewProductClass(root)
    root.mainloop()