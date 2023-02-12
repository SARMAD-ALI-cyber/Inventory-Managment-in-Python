import pandas as pd
from pandas import *
from numpy import *
from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import customtkinter
import billing
import MainMenu
class Loginform:
    def __init__(self,window):
        # def forgotpassword():
        #     pass
        def loginverification():
            username_input=self.username_entry.get()
            password_input=self.password_entry.get()
            df = read_csv('Book10.csv')
            matrix = df.to_numpy()
            found=False
            for record in matrix:
                if username_input in record[2]:
                    username_index=df[df['username']==username_input].index.values
                    password_onindex=df.loc[username_index,'password'].values[0]  #this will give the pass at user index
                    if '.admin' in username_input:
                        if (password_onindex == password_input):  # here redirect karao
                            MainMenu.MainMenuClass()
                            
                            found=True   
                    if '.employ' in username_input:
                        if (password_onindex == password_input):  # here redirect karao
                            billing.BillClass()
                            found=True
                            
            if found==False:
                messagebox.showerror('Error',"Wrong passwrod or User name",parent=self.window)
                    

        self.window=window
        self.window.geometry('1166x718')
        self.window.state('zoomed')
        self.window.resizable(0,0) #if it is removed we can resize our window
        #=========================background================================
        self.bg_frame=Image.open('assets\\loginbg.png')
        photo=ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel=Label(self.window,image=photo)
        self.bg_panel.image=photo
        self.bg_panel.pack(fill='both',expand='yes')

        #===========================login frame===================================
        self.lgn_frame=Frame(self.window,bg='white',width='950',height=600)##040405
        self.lgn_frame.place(x=200,y=70)
        self.txt = 'WELCOME'
        self.heading = Label(self.lgn_frame,text=self.txt,font=('yu gothic ui', 25,'bold'),bg='white',fg='black')
        self.heading.place(x=80,y=30,width=300,height=30)

        #===========================left side image==================================
        self.side_image = Image.open('assets\\loginframe.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo,bg='white') # blending ni hori
        self.side_image_label.image = photo
        self.side_image_label.place(x=-3,y=140)
        # ===========================sign in image==================================
        self.sign_in_image = Image.open('assets\\employface.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='white')  # blending ni hori
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=700, y=70)
        #=============sign in text========================
        self.sign_in_label=Label(self.lgn_frame,text='Sign In',bg='white',fg='black',font=('yu gothic ui',17,'bold'))
        self.sign_in_label.place(x=715,y=170)

        #=================username====================================================================================
        self.username_label=Label(self.lgn_frame,text='Username',bg='white',font=('yu gothic ui',13,'bold'),fg='black')
        self.username_label.place(x=550,y=250)

        #==========================userentry====================================
        self.username_entry=Entry(self.lgn_frame,highlightthickness=0,relief=FLAT,bg='white',fg='#6b6a69',font=('yu gothic ui',13,'bold'))
        self.username_entry.place(x=580,y=280,width=270)

        self.username_line=Canvas(self.lgn_frame,width=300,height=2.0,bg='#bdb9b1',highlightthickness=0)
        self.username_line.place(x=550,y=304)
        #=============================username icon=========================================================
        self.username_icon = Image.open('assets\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo,bg='white') # blending ni hori
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550,y=275)
        # =================Password====================================================================================
        self.password_label = Label(self.lgn_frame, text='Password', bg='white', font=('yu gothic ui', 13, 'bold'),
                                    fg='black')
        self.password_label.place(x=550, y=320)

        # =========================Password entry====================================
        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='white', fg='#6b6a69',
                                    font=('yu gothic ui', 13, 'bold'))
        self.password_entry.place(x=580, y=350, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=550, y=373)
         # =============================Password icon=========================================================
        self.password_icon = Image.open('assets\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='white')  # blending ni hori
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=345)
       #====================login button=====================================================================
        button=customtkinter.CTkButton(master=self.lgn_frame,text='LOGIN',width=200,height=25,command=loginverification)
        button.place(x=600,y=420)
        #====================================forget password=================================================
        # self.forgot_button=Button(self.lgn_frame,text='Fotget Password?',font=('yu gothic ui', 10, 'bold '),
        #                           fg='black',width=15,height=-2,bg='white',activebackground='white',cursor='hand2',command=forgotpassword)
        # self.forgot_button.place(x=810,y=417)
        # ===================================show hide pass==========================================================
        self.show_image = Image.open('assets\\password_hide.png')
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activeforeground='black',
                                  command=self.show, cursor='hand2', bd=0)
        self.show_button.image = self.photo1
        self.show_button.place(x=845, y=345)
        self.hide_image = Image.open('assets\\password_show.png')
        self.photo = ImageTk.PhotoImage(self.hide_image)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.photo, bg='white', activeforeground='black',
                                  cursor='hand2', bd=0, command=self.hide)
        self.hide_button.image = self.photo
        self.hide_button.place(x=845, y=345)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.photo1, bg='white', activeforeground='black',
                                  command=self.show, cursor='hand2', bd=0)
        self.show_button.image = self.photo1
        self.show_button.place(x=845, y=345)
        self.password_entry.config(show='*')






def page():
    window=Tk()
    Loginform(window)
    window.mainloop()
if __name__=='__main__':
    page()







