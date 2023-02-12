import tkinter as tk
import customtkinter as ctk
import pandas as pd

def sup_run():
    ctk.set_appearance_mode("light")
    def ShowAll():
        data = pd.read_csv("suppliers.csv", index_col=False)
        data_print = ctk.CTkLabel(root_supplier, text=data.to_string(index=False), font=('Times New Roman', 16),
                                fg_color="light gray", corner_radius=10, height=200, width=100)
        data_print.place(x=190, y=200)
        btn5 = ctk.CTkButton(root_supplier, text="Sort Data", font=('Times New Roman', 14), command=Sort)
        btn5.place(x=300, y=420, bordermode="outside", width=150, height=50)


    def Sort():
        opt1 = ctk.CTkCheckBox(root_supplier, text="ID", font=('Times New Roman', 16), checkbox_height=20, checkbox_width=20,
                            corner_radius=5, checkmark_color="blue", hover_color="gray", command=lambda: SortData(1, 1))
        opt1.place(x=190, y=460)
        opt1.deselect()
        opt2 = ctk.CTkCheckBox(root_supplier, text="Name", font=('Times New Roman', 16), checkbox_height=20, checkbox_width=20,
                            corner_radius=5, checkmark_color="blue", hover_color="gray", command=lambda: SortData(2, 1))
        opt2.place(x=290, y=460)
        opt2.deselect()
        opt3 = ctk.CTkCheckBox(root_supplier, text="Phone No.", font=('Times New Roman', 16), checkbox_height=20, checkbox_width=20,
                            corner_radius=5, checkmark_color="blue", hover_color="gray", command=lambda: SortData(3, 1))
        opt3.place(x=390, y=460)
        opt3.deselect()
        opt4 = ctk.CTkCheckBox(root_supplier, text="Location", font=('Times New Roman', 16), checkbox_height=20, checkbox_width=20,
                            corner_radius=5, checkmark_color="blue", hover_color="gray", command=lambda: SortData(4, 1))
        opt4.place(x=490, y=460)
        opt4.deselect()
        ShowAll()


    def SortData(uchoice, order):
        if order == 1:
            s_order = True
        elif order == 2:
            s_order = False
        data = pd.read_csv("suppliers.csv", index_col=False)
        df = pd.DataFrame(data)
        if uchoice == 1:
            df = df.sort_values(by=['ID'], ascending=s_order)
        if uchoice == 2:
            df = df.sort_values(by=['Name'], ascending=s_order)
        if uchoice == 3:
            df = df.sort_values(by=['Phone No.'], ascending=s_order)
        if uchoice == 4:
            df = df.sort_values(by=['Location'], ascending=s_order)
        df.to_csv("suppliers.csv", index=False)


    def ShowOne():
        SupID.place(x=190, y=150)
        enter = ctk.CTkButton(root_supplier, text="Enter!", corner_radius=30, border_color="dark blue", border_spacing=1,
                            command=on_click, width=120, height=30)
        enter.place(x=360, y=150)


    def on_click():
        ID = int(SupID.get())
        data = pd.read_csv("suppliers.csv", index_col=False)
        df = pd.DataFrame(data)
        data_print = ctk.CTkLabel(root_supplier, text=(df[df['ID'] == ID]), font=('Times New Roman', 16),
                                fg_color="light gray", corner_radius=10, height=200, width=100)
        data_print.place(x=190, y=200)


    def DeleteItem():
        data = pd.read_csv("suppliers.csv", index_col=False)
        SupID.place(x=190, y=150)
        enter = ctk.CTkButton(root_supplier, text="Enter!", corner_radius=30, border_color="dark blue", border_spacing=1,
                            command=on_click2, width=120, height=30)
        enter.place(x=360, y=150)


    def on_click2():
        ID = int(SupID.get())
        data = pd.read_csv("suppliers.csv", index_col=False)
        if ID in data['ID'].unique():
            data.set_index('ID', inplace=True)
            data = data.drop(ID)
            data.to_csv("suppliers.csv")
            data_print = ctk.CTkLabel(root_supplier, text="Data deleted successfully!", font=('Times New Roman', 16),
                                    fg_color="light blue", corner_radius=10)
            data_print.place(x=265, y=250)
        else:
            data_print = ctk.CTkLabel(root_supplier, text="Supplier ID not found!", font=('Times New Roman', 16),
                                    fg_color="light blue", corner_radius=10)
            data_print.place(x=265, y=250)


    def AddItem():
        SupID.place(x=20, y=200)
        Name.place(x=20, y=240)
        Phone.place(x=20, y=280)
        Loc.place(x=20, y=320)
        enter = ctk.CTkButton(root_supplier, text="Enter!", corner_radius=30, border_color="dark blue", border_spacing=1,
                            command=on_click3, width=120, height=20)
        enter.place(x=20, y=360)


    def on_click3():
        supID = SupID.get()
        name = Name.get()
        phone = Phone.get()
        loc = Loc.get()
        data = pd.read_csv("suppliers.csv", index_col=False)
        df = pd.DataFrame(data)
        if SupID in df['ID'].unique():
            data_print = ctk.CTkLabel(root_supplier, text="Supplier already exists", font=('Times New Roman', 16),
                                    fg_color="light blue", corner_radius=10)
            data_print.place(x=265, y=360)
        else:
            newdata = {
                'ID': [supID],
                'Name': [name],
                'Phone No.': [phone],
                'Location': [loc]}
            df = pd.DataFrame(newdata)
            df.to_csv("suppliers.csv", mode='a', index=False, header=False)
            data_print = ctk.CTkLabel(root_supplier, text="Data added successfully!", font=('Times New Roman', 16),
                                    fg_color="light blue", corner_radius=10)
            data_print.place(x=265, y=360)


    root_supplier = ctk.CTk()
    root_supplier.geometry("700x600")
    root_supplier.title("Inventory Management System")


    SupID = ctk.CTkEntry(root_supplier, placeholder_text="ID", border_width=2, border_color="dark blue", corner_radius=5,width=120)
    Name = ctk.CTkEntry(root_supplier, placeholder_text="Name", border_width=2, border_color="dark blue", corner_radius=5,width=120)
    Phone = ctk.CTkEntry(root_supplier, placeholder_text="Phone No.", border_width=2, border_color="dark blue", corner_radius=5,width=120)
    Loc = ctk.CTkEntry(root_supplier, placeholder_text="Location", border_width=2, border_color="dark blue", corner_radius=5,width=120)

    head = ctk.CTkLabel(root_supplier, text="SUPPLIERS", font=('Times New Roman', 26), text_color="dark blue", corner_radius=20)
    head.place(x=265, y=10)

    subhead = ctk.CTkLabel(root_supplier, text="Please select an option:", font=('Times New Roman', 18), corner_radius=20)
    subhead.place(x=250, y=50)

    btn1 = ctk.CTkButton(root_supplier, text="View All", font=('Times New Roman', 14), command=ShowAll, corner_radius=20)
    btn1.place(x=20, y=100, bordermode="outside", width=300, height=50)

    btn2 = ctk.CTkButton(root_supplier, text="View by ID", font=('Times New Roman', 14), command=ShowOne, corner_radius=20)
    btn2.place(x=190, y=100, bordermode="outside", width=300, height=50)

    btn3 = ctk.CTkButton(root_supplier, text="Add Supplier", font=('Times New Roman', 14), command=AddItem, corner_radius=20)
    btn3.place(x=360, y=100, bordermode="outside", width=300, height=50)

    btn4 = ctk.CTkButton(root_supplier, text="Remove Supplier", font=('Times New Roman', 14), command=DeleteItem, corner_radius=20)
    btn4.place(x=530, y=100, bordermode="outside", width=300, height=50)
    root_supplier.mainloop()

