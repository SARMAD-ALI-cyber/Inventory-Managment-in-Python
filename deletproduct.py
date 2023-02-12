import pandas as pd
from tkinter import*
from tkinter import ttk,messagebox
import productMenu
class DeleteProductClass:
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
            
        pTitle=Label(MainFrame,text="DELETE PRODUCT", font=("goudy old style", 20, "bold"),bg="lightblue",fg="white").pack(side=TOP,fill=X)

        self.var_PId=StringVar()
        self.var_PName=StringVar()

        lbl_PId = Label(MainFrame, text="Product ID ", font=("times new roman", 30, "bold"), bg="lightgray").place(x=150, y=200)
        txt_PId = Entry(MainFrame, textvariable=self.var_PId, font=("times new roman", 30), bg="white").place(x=370, y=200, width=180)

        btn_search = Button(MainFrame, text="Delete Product",font=("goudy old style", 30, "bold"),command=self.delete_product,bg="#2196f3",fg="white",cursor="hand2").place(x=220,y=350,width=300,height=50)

    def delete_product(self):
        ID = int(self.var_PId.get())
        data = pd.read_csv("Product.csv", index_col=False)
        if ID in data['ID'].unique():
            data.set_index('ID', inplace=True)
            data = data.drop(ID)
            data.to_csv("Product.csv")
            messagebox.showinfo("Delete","Product Deleted successfully",parent=self.root)
        else:
            messagebox.showinfo("Delete","Product not in database",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=DeleteProductClass(root)
    root.mainloop()