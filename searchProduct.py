import pandas as pd
from tkinter import*
from tkinter import ttk,messagebox
import productMenu
class SearchProductClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        #==================title=====================================
        title=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",font=("times new roman",40, "bold"),bg="lightblue",fg="white").place(x=0, y=10,relwidth=1,height=70)
        btn_back=Button(self.root,text="BACK",font=("times new roman",15, "bold"),bg="#2196f3",fg="white",command=lambda: productMenu.ProductMenuClass(root)).place(x=10, y=20,height=50,width=100)
        #==================Product Menu=================================
        #product frame
        df = pd.read_csv("Product.csv")
        matrix = df.to_numpy()
        MainFrame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
        MainFrame.place(x=330,y=110,width=750,height=550)

        pTitle=Label(MainFrame,text="Products", font=("goudy old style", 20, "bold"),bg="lightblue",fg="white").pack(side=TOP,fill=X)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Product Search Frame$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        self.var_search=StringVar()
        ProductFrame2 = Frame(MainFrame, bd=2, relief=RIDGE, bg="white")
        ProductFrame2.place(x=2, y=42, width=740, height=90)

        lbl_search=Label(ProductFrame2, text="Search Product | By Name",font=("times new roman",15, "bold"),bg="white",fg="green").place(x=2, y=5)

        lbl_search = Label(ProductFrame2,text="Product Name",font=("times new roman",15, "bold"),fg="green",bg="white").place(x=2, y=45)
        txt_search = Entry(ProductFrame2, textvariable=self.var_search,font=("times new roman", 15), bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search = Button(ProductFrame2, text="Search",font=("goudy old style", 15),command=self.search,bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=47,width=100,height=22)
        btn_show_all = Button(ProductFrame2, text="Show All", font=("goudy old style", 15),command=self.show_all_products, bg="#2196f3", fg="white",cursor="hand2").place(x=285, y=10, width=100, height=22)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Product details Frame$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        self.var_PID = StringVar()
        self.var_PName = StringVar()
        self.var_PPrice = StringVar()
        self.var_PStock = StringVar()
        self.var_PCategoryame = StringVar()
        self.var_PSupplier = StringVar()

        ProductFrame3 = Frame(MainFrame,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=740,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("ID", "name", "price", "stock", "category", "supplier"))
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("ID",text="ID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("stock", text="stock")
        self.product_Table.heading("category", text="Category")
        self.product_Table.heading("supplier", text="Supplier")
        self.product_Table["show"] = "headings"
        self.product_Table.column("ID", width=80)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("stock", width=80)
        self.product_Table.column("category", width=80)
        self.product_Table.column("supplier", width=100)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)

    def show_all_products(self):
        df = pd.read_csv("Product.csv")
        matrix = df.to_numpy()
        self.product_Table.delete(*self.product_Table.get_children())
        for record in matrix:
            self.product_Table.insert(parent='', index='end', text='',values=(record[0], record[1], record[2], record[3], record[4], record[5]))

    def search(self):
        df = pd.read_csv("Product.csv")
        matrix = df.to_numpy()
        if self.var_search.get()=="":
            messagebox.showerror("Error", "Search input should be required",parent=self.root)
        else:
            self.product_Table.delete(*self.product_Table.get_children())
            for record in matrix:
                if self.var_search.get() in record[1]:
                    self.product_Table.insert(parent='', index='end', text='',values=(record[0], record[1], record[2], record[3], record[4], record[5]))

    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_PID.set(row[3])
        self.var_PName.set(row[1])
        self.var_PPrice.set(row[2])
        self.var_PStock.set(row[3])
        self.var_PCategoryame.set(row[4])
        self.var_PSupplier.set(row[5])

if __name__=="__main__":
    root=Tk()
    obj=SearchProductClass(root)
    root.mainloop()