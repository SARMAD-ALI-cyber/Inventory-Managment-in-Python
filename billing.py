import pandas as pd
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import random
import time
import os
import tempfile
import login
class BillClass:
    def __init__(self):
        self.root=Toplevel()
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.cart_list=[]

        #==================================title===================================
        title=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",font=("times new roman",40, "bold"),bg="lightblue",fg="white").place(x=0, y=10,relwidth=1,height=70)
        #==================================logout==================================
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15, "bold"),command=lambda: login.Loginform(window=self.root),bg="#2196f3",fg="white").place(x=1200, y=20,height=50,width=100)

        #product frame
        df = pd.read_csv("C:\\Users\\hasee\\ICT project\\product.csv")
        matrix = df.to_numpy()
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Products", font=("goudy old style", 20, "bold"),bg="lightblue",fg="white").pack(side=TOP,fill=X)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Product Search Frame$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        self.var_search=StringVar()
        ProductFrame2 = Frame(ProductFrame1, bd=2, relief=RIDGE, bg="white")
        ProductFrame2.place(x=2, y=42, width=398, height=90)

        lbl_search=Label(ProductFrame2, text="Search Product | By Name",font=("times new roman",15, "bold"),bg="white",fg="green").place(x=2, y=5)

        lbl_search = Label(ProductFrame2,text="Product Name",font=("times new roman",15, "bold"),fg="green",bg="white").place(x=2, y=45)
        txt_search = Entry(ProductFrame2, textvariable=self.var_search,font=("times new roman", 15), bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search = Button(ProductFrame2, text="Search",font=("goudy old style", 15),command=self.search,bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=47,width=100,height=22)
        btn_show_all = Button(ProductFrame2, text="Show All", font=("goudy old style", 15),command=self.show_all_products, bg="#2196f3", fg="white",cursor="hand2").place(x=285, y=10, width=100, height=22)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Product details Frame$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        ProductFrame3 = Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("ID", "name", "price", "stock"))
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("ID",text="ID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("stock", text="stock")
        self.product_Table["show"] = "headings"
        self.product_Table.column("ID", width=80)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("stock", width=80)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(ProductFrame1,text="Note: Enter 0 Quantity to remove product from cart", font=("goudy old style", 12),anchor='w',bg="white", fg="red").pack(side=BOTTOM,fill=X)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$CUSTOMER FRAME$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        self.var_customer_name=StringVar()
        self.var_contact=StringVar()
        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=420, y=110, width=530, height=70)

        cTitle = Label(CustomerFrame, text="Customer Details", font=("goudy old style", 15, "bold"), bg="lightblue",fg="white").pack(side=TOP, fill=X)
        lbl_naem = Label(CustomerFrame, text="Name", font=("times new roman", 15, "bold"), bg="white",fg="green").place(x=5, y=35)
        txt_name = Entry(CustomerFrame, textvariable=self.var_customer_name, font=("times new roman", 15), bg="lightyellow").place(x=80, y=35, width=180)

        lbl_contact = Label(CustomerFrame, text="Contact No.", font=("times new roman", 15, "bold"), bg="white",fg="green").place(x=270, y=35)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("times new roman", 15),bg="lightyellow").place(x=380, y=35, width=140)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Calculator and Cart Frame$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        Cal_Cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=420, y=190, width=530, height=360)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Calculator Frame$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        self.var_cal_input=StringVar()

        Cal_Frame = Frame(Cal_Cart_Frame, bd=9, relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=10, width=268, height=340)

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial', 15, 'bold'), width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7 = Button(Cal_Frame,text='7',font=('arial', 15, 'bold'),command=lambda :self.get_input(7),bd=5,width=4,pady=10,cursor='hand2').grid(row=1,column=0)
        btn_8 = Button(Cal_Frame, text='8', font=('arial', 15, 'bold'),command=lambda :self.get_input(8), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=1)
        btn_9 = Button(Cal_Frame, text='9', font=('arial', 15, 'bold'),command=lambda :self.get_input(8), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=2)
        btn_sum = Button(Cal_Frame, text='+', font=('arial', 15, 'bold'),command=lambda :self.get_input('+'), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=3)

        btn_4 = Button(Cal_Frame, text='4', font=('arial', 15, 'bold'),command=lambda :self.get_input(4), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=0)
        btn_5 = Button(Cal_Frame, text='5', font=('arial', 15, 'bold'),command=lambda :self.get_input(5), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=1)
        btn_6 = Button(Cal_Frame, text='6', font=('arial', 15, 'bold'),command=lambda :self.get_input(6), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=2)
        btn_sub = Button(Cal_Frame, text='-', font=('arial', 15, 'bold'),command=lambda :self.get_input('-'), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=3)

        btn_1 = Button(Cal_Frame, text='1', font=('arial', 15, 'bold'),command=lambda :self.get_input(1), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=0)
        btn_2 = Button(Cal_Frame, text='2', font=('arial', 15, 'bold'),command=lambda :self.get_input(2), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=1)
        btn_3 = Button(Cal_Frame, text='3', font=('arial', 15, 'bold'),command=lambda :self.get_input(3), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=2)
        btn_mul = Button(Cal_Frame, text='*', font=('arial', 15, 'bold'),command=lambda :self.get_input('*'), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=3)

        btn_0 = Button(Cal_Frame, text='0', font=('arial', 15, 'bold'),command=lambda :self.get_input(0), bd=5, width=4, pady=15, cursor='hand2').grid(row=4, column=0)
        btn_c = Button(Cal_Frame, text='C', font=('arial', 15, 'bold'),command=self.clear_cal, bd=5, width=4, pady=15, cursor='hand2').grid(row=4, column=1)
        btn_equal = Button(Cal_Frame, text='=', font=('arial', 15, 'bold'),command=self.perform_cal, bd=5, width=4, pady=15, cursor='hand2').grid(row=4, column=2)
        btn_div = Button(Cal_Frame, text='/', font=('arial', 15, 'bold'),command=lambda :self.get_input("/"), bd=5, width=4, pady=15, cursor='hand2').grid(row=4, column=3)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Cart Frame$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        cart_Frame = Frame(Cal_Cart_Frame, bd=3, relief=RIDGE)
        cart_Frame.place(x=280, y=8, width=245, height=342)
        cartTitle = Label(cart_Frame, text="Cart", font=("goudy old style", 15), bg="lightgray").pack(side=TOP, fill=X)

        scrolly = Scrollbar(cart_Frame, orient=VERTICAL)

        self.CartTable = ttk.Treeview(cart_Frame, columns=("name", "price", "qty"))
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("name", text="Name")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("qty", text="Qty")
        self.CartTable["show"] = "headings"
        self.CartTable.column("name", width=100)
        self.CartTable.column("price", width=80)
        self.CartTable.column("qty", width=40)
        self.CartTable.pack(fill=BOTH, expand=1)
        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Add cart Widgets Frame$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()
        Add_CartWidgetsFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Add_CartWidgetsFrame.place(x=420, y=550, width=530, height=110)

        label_p_name=Label(Add_CartWidgetsFrame,text="Product Name", font=("times new roman", 15),bg="white").place(x=5, y=5)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_pname, font=("times new roman", 15), bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        label_p_price = Label(Add_CartWidgetsFrame, text="Price Per Qty", font=("times new roman", 15), bg="white").place(x=230, y=5)
        txt_p_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_price, font=("times new roman", 15),bg="lightyellow", state='readonly').place(x=230, y=35, width=150, height=22)

        label_p_qty = Label(Add_CartWidgetsFrame, text="Quantity", font=("times new roman", 15), bg="white").place(x=390, y=5)
        txt_p_qty = Entry(Add_CartWidgetsFrame, textvariable=self.var_qty, font=("times new roman", 15),bg="lightyellow").place(x=390, y=35, width=120, height=22)

        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",font=("times new roman", 15, "bold"),command=self.clear_cart, bg="lightgray", cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart = Button(Add_CartWidgetsFrame, text="Add | Update Cart", font=("times new roman", 15, "bold"),command=self.add_update_cart,bg="orange", cursor="hand2").place(x=340, y=70, width=180, height=30)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Billing Area$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=410,height=410)

        bTitle = Label(billFrame, text="Customer Bill Area", font=("goudy old style", 20, "bold"), bg="#f44336",fg="white").pack(side=TOP, fill=X)
        scrolly = Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #$$$$$$$$$$$$$$$$Billing buttons$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        billMenuFrame.place(x=953, y=520, width=410, height=140)

        self.lbl_net_pay = Label(billMenuFrame, text="Total Bill\n[0]", font=("goudy old style", 15, "bold"),bg="#607db8", fg="white")
        self.lbl_net_pay.place(x=2, y=5, width=390, height=70)

        btn_clear_all = Button(billMenuFrame, text="Clear All", font=("goudy old style", 15, "bold"),command=self.clear_all, cursor="hand2",bg="gray", fg="white")
        btn_clear_all.place(x=2, y=80, width=195, height=50)

        btn_generate = Button(billMenuFrame, text="Generate/Save Bill", font=("goudy old style", 15, "bold"),command=self.generate_bill, cursor="hand2", bg="#009688",fg="white")
        btn_generate.place(x=200, y=80, width=190, height=50)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$footer$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        footer=Label(self.root,text="IMS-Inventory Management System", font=("times new roman", 11),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.var_TotalBill = StringVar()


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&&&$$$$$$$$$All Function&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    def get_input(self,num):
        xnum = self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show_all_products(self):
        df = pd.read_csv("C:\\Users\\hasee\\ICT project\\product.csv")
        matrix = df.to_numpy()
        self.product_Table.delete(*self.product_Table.get_children())
        for record in matrix:
            self.product_Table.insert(parent='', index='end', text='',values=(record[0], record[1], record[2], record[3]))

    def search(self):
        df = pd.read_csv("C:\\Users\\hasee\\ICT project\\product.csv")
        matrix = df.to_numpy()
        if self.var_search.get()=="":
            messagebox.showerror("Error", "Search input should be required",parent=self.root)
        else:
            self.product_Table.delete(*self.product_Table.get_children())
            for record in matrix:
                if self.var_search.get() in record[1]:
                    self.product_Table.insert(parent='', index='end', text='',values=(record[0], record[1], record[2], record[3]))
    
    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_stock.set(row[3])
        
    def add_update_cart(self):
        if self.var_qty.get()=="":
            messagebox.showerror('Error',"Quantity is required",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror('Error', "Insufficient stock available")
        else:
            price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
            cart_data=[self.var_pname.get(),price_cal,self.var_qty.get()]
            #$$$$$$$$update cart $$$$$$$$$$$$$$
            present=False
            index=0
            for row in self.cart_list:
                if row[0]==self.var_pname.get():
                    present=True
                    break;
                index+=1
            if present:
                op=messagebox.askyesno('confirm',"Product already present\nDo you want to update| Remove from the Cart List",parent=self.root)
                if op==True:
                    if self.var_qty.get()=='0':
                        self.cart_list.pop(index)
                    else:
                        self.cart_list[index][1]=price_cal#price
                        self.cart_list[index][2]=self.var_qty.get()#qty
                    self.show_cart()
            else:
                self.cart_list.append(cart_data)
                self.show_cart()
            self.bill_updates()
    
    def bill_updates(self):
        bill_amount=0
        for row in self.cart_list:
            bill_amount+=row[1]
        self.lbl_net_pay.config(text=f'Bill Amount(Rs.)\n{str(bill_amount)}')
        self.var_TotalBill = bill_amount
        
    def show_cart(self):
        self.CartTable.delete(*self.CartTable.get_children())
        for record in self.cart_list:
            self.CartTable.insert(parent='', index='end', text='',values=(record[0], record[1], self.var_qty.get()))

    def generate_bill(self):
        if self.var_customer_name.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","Customer details are required",parent=self.root)
        elif (self.cart_list)==0:
            messagebox.showerror("Error","No prduct in Cart",parent=self.root)
        else:
            #$$$$$$$$$$$$$$$$$$$BILL Header$$$$$$$$$$$$$$$$$$
            self.bill_top()
            #$$$$$$$$$$$$$$$$$$$BILL Main$$$$$$$$$$$$$$$$$$$$
            self.bill_middle()
            #$$$$$$$$$$$$$$$$$$$BILL Footer$$$$$$$$$$$$$$$$$$
            self.bill_bottom()

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showerror("Saved","Bill has been generated and saved",parent=self.root)

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tInventory Managment System

{str("="*47)}
 Customer Name: {self.var_customer_name.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
 Total Bill:\t\t\t\tRs.{self.var_TotalBill}
{str("="*47)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
        
    def bill_middle(self):
        for row in self.cart_list:
        # pid,name,price,qty,stock
            name=row[0]
            qty=row[2]
            price=float(row[1])*int(row[2])
            price=str(price)
            self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+qty+"\tRs."+price)
        
    def clear_cart(self):
        self.var_pname.set('')
        self.var_price.set('')
        self.var_stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_customer_name.set('')
        self.var_contact.set("")
        self.txt_bill_area.delete('1.0',END)
        self.var_search.set('')
        self.clear_cart()
        self.show_cart()

def run():
    if __name__=="__main__":
        root=Tk()
        obj=BillClass()
        root.mainloop()
run()