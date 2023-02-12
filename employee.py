from tabulate import tabulate
import pandas as pd
import MainMenu

column = ['EMPID','Name', 'Gender', 'Contact', 'User Type', 'Password', 'DOB', 'DOJ', 'Email', 'Salary']

exit = False
count = 0


def read(column, self):
    df = pd.read_csv("Book10.csv")
    matrix = df.to_numpy()

    self.employee_Table.delete(*self.employee_Table.get_children())
    for record in matrix:
        self.employee_Table.insert(parent='', index='end', text='', values=(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],
            record[9],
            record[10]))


def add(column, var_EMPID,
        var_customer_name, var_Username,
        var_customer_gender
        , var_contact
        , var_usertype
        , var_Password
        , var_DOB
        , var_DOJ
        , var_Email, var_Salary):
    employee_details = {'EMPID': [var_EMPID.get()], 'Name': [var_customer_name.get()], 'Username': [var_Username.get()],
                        'Gender': [var_customer_gender.get()], 'Contact': [var_contact.get()],
                        'User Type': [var_usertype.get()], 'Password': [var_Password.get()], 'DOB': [var_DOB.get()],
                        'DOJ': [var_DOJ.get()], 'Email': [var_Email.get()], 'Salary': [var_Salary.get()]}
    df = pd.DataFrame(employee_details)

    df.to_csv("Book10.csv", mode='a', header=False, index=False)


def delete(column, txt_delete_search):
    df = pd.read_csv("Book10.csv")
    empid = txt_delete_search.get()
    empid = int(empid)
    if empid in df['EMPID'].unique():
        df.set_index('EMPID', inplace=True)
        df = df.drop(empid)
        df.to_csv("Book10.csv")

from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class EmployeeClass:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        title=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",font=("times new roman",40, "bold"),bg="lightblue",fg="white").place(x=0, y=10,relwidth=1,height=70)
        btn_back=Button(self.root,text="BACK",font=("times new roman",15, "bold"),bg="#2196f3",fg="white",command=lambda: MainMenu.MainMenuClass()).place(x=10, y=20,height=50,width=100)
        # employee frame
        self.var_search = StringVar()
        self.var_delete = StringVar()

        EmployeeFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        EmployeeFrame1.place(x=150, y=90, width=1000, height=350)

        pTitle = Label(EmployeeFrame1, text="EMPLOYEE INFO", font=("goudy old style", 20, "bold"), bg="light blue",
                       fg="white").pack(side=TOP, fill=X)

        # employee Search Frame
        EmployeeFrame2 = Frame(EmployeeFrame1, bd=2, relief=RIDGE, bg="white")
        EmployeeFrame2.place(x=2, y=42, width=1500, height=90)

        lbl_search = Label(EmployeeFrame2, text="Search Employee | By EMP ID", font=("times new roman", 15, "bold"),
                           bg="white", fg="green").place(x=2, y=5)

        lbl_search = Label(EmployeeFrame2, text="EMP ID", font=("times new roman", 15, "bold"), bg="white").place(x=2,
                                                                                                                 y=45)
        txt_search = Entry(EmployeeFrame2, textvariable=self.var_search, font=("times new roman", 15),
                           bg="lightyellow").place(x=128, y=47, width=150, height=22)
        btn_search = Button(EmployeeFrame2, text="Search", font=("goudy old style", 15), command=self.search,
                            bg="#2196f3", fg="white", cursor="hand2").place(x=285, y=47, width=100, height=22)

        # function for deletng employees

        lbl_Delete = Label(EmployeeFrame2, text="Delete Employee | By EMP ID", font=("times new roman", 15, "bold"),
                           bg="white").place(x=500, y=5)
        txt_delete_search = Entry(EmployeeFrame2, textvariable=self.var_delete, font=("times new roman", 15),
                                  bg="lightyellow").place(x=760, y=5, width=150, height=22)
        btn_delete = Button(EmployeeFrame2, text="Delete", font=("goudy old style", 15), bg="#2196f3", fg="white",
                            command=lambda: delete(column, self.var_delete),
                            cursor="hand2").place(x=760, y=40, width=100, height=22)

        # Employee details Frame
        EmployeeFrame3 = Frame(EmployeeFrame1, bd=3, relief=RIDGE)
        EmployeeFrame3.place(x=2, y=140, width=1000, height=200)

        scrolly = Scrollbar(EmployeeFrame3, orient=VERTICAL)
        self.employee_Table = ttk.Treeview(EmployeeFrame3, columns=(
            'EMPID', 'Name', 'User Name', 'Gender', 'Contact', 'User Type', 'Password', 'DOB', 'DOJ', 'Email',
            'Salary'))
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.employee_Table.yview)

        self.product_Table = ttk.Treeview(EmployeeFrame3, columns=(
            'EMPID', 'Name', 'User Name', 'Gender', 'Contact', 'User Type', 'Password', 'DOB', 'DOJ', 'Email',
            'Salary'))

        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.employee_Table.yview)
        btn_show_all = Button(EmployeeFrame2, text="Show All", command=lambda: read(column, self),
                              font=("goudy old style", 15), bg="#083531", fg="white", cursor="hand2").place(x=285, y=10,
                                                                                                            width=100,
                                                                                                            height=22)
        self.employee_Table.heading("EMPID", text="EMPID")
        self.employee_Table.heading("Name", text="Name")
        self.employee_Table.heading("User Name", text="User Name")
        self.employee_Table.heading("Gender", text="Gender")
        self.employee_Table.heading("Contact", text="Contact")
        self.employee_Table.heading("User Type", text="User Type")
        self.employee_Table.heading("Password", text="Password")
        self.employee_Table.heading("DOB", text="DOB")
        self.employee_Table.heading("DOJ", text="DOJ")
        self.employee_Table.heading("Email", text="Email")
        self.employee_Table.heading("Salary", text="Salary")
        self.employee_Table["show"] = "headings"
        self.employee_Table.column("EMPID", width=80)
        self.employee_Table.column("Name", width=80)
        self.employee_Table.column("User Name", width=80)
        self.employee_Table.column("Gender", width=80)
        self.employee_Table.column("Contact", width=80)
        self.employee_Table.column("User Type", width=80)
        self.employee_Table.column("Password", width=80)
        self.employee_Table.column("DOB", width=80)
        self.employee_Table.column("DOJ", width=80)
        self.employee_Table.column("Email", width=80)
        self.employee_Table.column("Salary", width=80)

        self.employee_Table.pack(fill=BOTH, expand=1)

        # Employee Data Entry
        self.var_customer_name = StringVar()
        self.var_contact = StringVar()
        self.var_customer_gender = StringVar()
        self.var_usertype = StringVar()
        self.var_DOB = StringVar()
        self.var_DOJ = StringVar()
        self.var_EMPID = StringVar()
        self.var_Email = StringVar()
        self.var_Salary = StringVar()
        self.var_Password = StringVar()
        self.var_Username = StringVar()
        EmployeeFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        EmployeeFrame.place(x=10, y=430, width=1350, height=70)

        cTitle = Label(EmployeeFrame, text="ADD NEW EMPLOYEE", font=("goudy old style", 15,"bold"), bg="lightblue", fg="white").pack(
            side=TOP, fill=X)

        employee = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        employee.place(x=10, y=500, width=1500, height=200)
        lbl_naem = Label(employee, text="Name", font=("times new roman", 15, "bold"), bg="white").place(x=5, y=35)
        txt_name = Entry(employee, textvariable=self.var_customer_name, font=("times new roman", 15),
                         bg="lightyellow").place(x=150, y=35, width=100)

        lbl_contact = Label(employee, text="Contact No.", font=("times new roman", 15, "bold"), bg="white").place(
            x=270, y=35)
        txt_contact = Entry(employee, textvariable=self.var_contact, font=("times new roman", 15),
                            bg="lightyellow").place(x=380, y=35, width=140)
        lbl_gender = Label(employee, text="Gender", font=("times new roman", 15, "bold"), bg="white").place(
            x=270, y=70)
        txt_gender = Entry(employee, textvariable=self.var_customer_gender, font=("times new roman", 15),
                           bg="lightyellow").place(x=380, y=70, width=140)
        lbl_Usertype = Label(employee, text="User Type", font=("times new roman", 15, "bold"), bg="white").place(
            x=540, y=35)
        txt_Usertype = Entry(employee, textvariable=self.var_usertype, font=("times new roman", 15),
                             bg="lightyellow").place(x=640, y=35, width=120)
        lbl_DOB = Label(employee, text="DOB dd/mm/yy", font=("times new roman", 15, "bold"), bg="white").place(x=5,
                                                                                                               y=70)
        txt_DOB = Entry(employee, textvariable=self.var_DOB, font=("times new roman", 15),
                        bg="lightyellow").place(x=150, y=70, width=100)
        lbl_DOJ = Label(employee, text="DOJ dd/mm/yy", font=("times new roman", 15, "bold"), bg="white").place(
            x=5, y=105)
        txt_DOJ = Entry(employee, textvariable=self.var_DOJ, font=("times new roman", 15),
                        bg="lightyellow").place(x=150, y=105, width=100)
        lbl_EMPID = Label(employee, text="EMPID", font=("times new roman", 15, "bold"), bg="white").place(
            x=770, y=35)
        txt_EMPID = Entry(employee, textvariable=self.var_EMPID, font=("times new roman", 15),
                          bg="lightyellow").place(x=850, y=35, width=140)
        lbl_Email = Label(employee, text="Email", font=("times new roman", 15, "bold"), bg="white").place(
            x=1000, y=35)
        txt_Email = Entry(employee, textvariable=self.var_Email, font=("times new roman", 15),
                          bg="lightyellow").place(x=1100, y=35, width=140)
        lbl_Salary = Label(employee, text="Salary", font=("times new roman", 15, "bold"), bg="white").place(
            x=770, y=70)
        txt_Salary = Entry(employee, textvariable=self.var_Salary, font=("times new roman", 15),
                           bg="lightyellow").place(x=850, y=70, width=140)
        lbl_Password = Label(employee, text="password", font=("times new roman", 15, "bold"), bg="white").place(
            x=1000, y=70)
        txt_Password = Entry(employee, textvariable=self.var_Password, font=("times new roman", 15),
                             bg="lightyellow").place(x=1100, y=70, width=140)
        lbl_Username = Label(employee, text="Username", font=("times new roman", 15, "bold"), bg="white").place(
            x=270, y=105)
        txt_Username = Entry(employee, textvariable=self.var_Username, font=("times new roman", 15),
                             bg="lightyellow").place(x=380, y=105, width=140)

        button_Add = Button(employee, command=lambda: add(column, self.var_EMPID, self.var_customer_name,self.var_Username,
                                                          self.var_customer_gender, self.var_contact, self.var_usertype,
                                                          self.var_Password, self.var_DOB, self.var_DOJ, self.var_Email,
                                                          self.var_Salary), text="Add",
                            font=("goudy old style", 15), bg="#2196f3", fg="white",
                            cursor="hand2").place(x=1200, y=130, width=100, height=22)

    def search(self):

        df = pd.read_csv("Book10.csv")
        # df = pd.DataFrame(df, columns=column)

        # s= df[df['EMPID']==[emp_id]]
        matrix = df.to_numpy()
        EmpID =self.var_search.get()
        if self.var_search.get() == "":
            messagebox.showerror("Error", "Search input should be required", parent=self.root)
        else:
            self.employee_Table.delete(*self.employee_Table.get_children())
            for record in matrix:
                print(EmpID, record[0])
                if str(EmpID) == str(record[0]):
                    print("found")
                    self.employee_Table.insert(parent='', index='end', text='',
                                               values=(
                                                   record[0], record[1], record[2], record[3], record[4], record[5],
                                                   record[6],
                                                   record[7], record[8], record[9], record[10]))


if __name__ == "__main__":
    root = Tk()
    obj = EmployeeClass()
    root.mainloop()
