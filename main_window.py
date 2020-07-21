"""This module manages the UI of the Main Window"""
import tkinter as tk
import login
import about
import address_edit
import password_edit
import payment_edit
import delete_window
import sqlite3 as sq
from sqlite3 import Error
from tkinter import messagebox as msgb

class Main_Window:
    """This class runs the UI of the Main Window"""

    def __init__(self,username, full_name):
        self.username = username
        self.full_name = full_name
        self.window_main = tk.Tk()
        self.window_main.title('Password Handler')
        self.window_main.geometry('1100x600')
        self.window_main.resizable(False, False)
        self.window_main.configure(bg='black')
        self.window_main.iconbitmap('resources/icon.ico')
        self.init_ui()

    def entered_data_1(self, event):
        self.data_1.configure(bg='#ffffff')

    def leave_data_1(self, event):
        self.data_1.configure(bg='#d9d89a')

    def entered_data_2(self, event):
        self.data_2.configure(bg='#ffffff')

    def leave_data_2(self, event):
        self.data_2.configure(bg='#d9d89a')

    def entered_data_3(self, event):
        self.data_3.configure(bg='#ffffff')

    def leave_data_3(self, event):
        self.data_3.configure(bg='#d9d89a')

    def entered_data_4(self, event):
        self.data_4.configure(bg='#ffffff')

    def leave_data_4(self, event):
        self.data_4.configure(bg='#d9d89a')

    def entered_data_5(self, event):
        self.data_5.configure(bg='#ffffff')

    def leave_data_5(self, event):
        self.data_5.configure(bg='#d9d89a')

    def entered_data_6(self, event):
        self.data_6.configure(bg='#ffffff')

    def leave_data_6(self, event):
        self.data_6.configure(bg='#d9d89a')

    def entered_data_7(self, event):
        self.data_7.configure(bg='#ffffff')

    def leave_data_7(self, event):
        self.data_7.configure(bg='#d9d89a')

    def entered_data_8(self, event):
        self.data_8.configure(bg='#ffffff')

    def leave_data_8(self, event):
        self.data_8.configure(bg='#d9d89a')

    def entered_data_9(self, event):
        self.data_9.configure(bg='#ffffff')

    def leave_data_9(self, event):
        self.data_9.configure(bg='#d9d89a')

    def entered_data_10(self, event):
        self.data_10.configure(bg='#ffffff')

    def leave_data_10(self, event):
        self.data_10.configure(bg='#d9d89a')

    def entered_data_11(self, event):
        self.data_11.configure(bg='#ffffff')

    def leave_data_11(self, event):
        self.data_11.configure(bg='#d9d89a')

    def entered_data_12(self, event):
        self.data_12.configure(bg='#ffffff')

    def leave_data_12(self, event):
        self.data_12.configure(bg='#d9d89a')

    def entered_data_13(self, event):
        self.data_13.configure(bg='#ffffff')

    def leave_data_13(self, event):
        self.data_13.configure(bg='#d9d89a')

    def entered_data_14(self, event):
        self.data_14.configure(bg='#ffffff')

    def leave_data_14(self, event):
        self.data_14.configure(bg='#d9d89a')

    def entered_data_15(self, event):
        self.data_15.configure(bg='#ffffff')

    def leave_data_15(self, event):
        self.data_15.configure(bg='#d9d89a')

    def entered_data_16(self, event):
        self.data_16.configure(bg='#ffffff')

    def leave_data_16(self, event):
        self.data_16.configure(bg='#d9d89a')

    def entered_data_17(self, event):
        self.data_17.configure(bg='#ffffff')

    def leave_data_17(self, event):
        self.data_17.configure(bg='#d9d89a')

    def entered_data_18(self, event):
        self.data_18.configure(bg='#ffffff')

    def leave_data_18(self, event):
        self.data_18.configure(bg='#d9d89a')

    def entered_data_19(self, event):
        self.data_19.configure(bg='#ffffff')

    def leave_data_19(self, event):
        self.data_19.configure(bg='#d9d89a')

    def entered_data_20(self, event):
        self.data_20.configure(bg='#ffffff')

    def leave_data_20(self, event):
        self.data_20.configure(bg='#d9d89a')

    def entered_data_21(self, event):
        self.data_21.configure(bg='#ffffff')

    def leave_data_21(self, event):
        self.data_21.configure(bg='#d9d89a')

    def entered_data_22(self, event):
        self.data_22.configure(bg='#ffffff')

    def leave_data_22(self, event):
        self.data_22.configure(bg='#d9d89a')

    def entered_data_23(self, event):
        self.data_23.configure(bg='#ffffff')

    def leave_data_23(self, event):
        self.data_23.configure(bg='#d9d89a')

    def entered_data_24(self, event):
        self.data_24.configure(bg='#ffffff')

    def leave_data_24(self, event):
        self.data_24.configure(bg='#d9d89a')

    def entered_data_25(self, event):
        self.data_25.configure(bg='#ffffff')

    def leave_data_25(self, event):
        self.data_25.configure(bg='#d9d89a')

    def entered_data_26(self, event):
        self.data_26.configure(bg='#ffffff')

    def leave_data_26(self, event):
        self.data_26.configure(bg='#d9d89a')

    def entered_data_27(self, event):
        self.data_27.configure(bg='#ffffff')

    def leave_data_27(self, event):
       self.data_27.configure(bg='#d9d89a')

    def entered_data_28(self, event):
        self.data_28.configure(bg='#ffffff')

    def leave_data_28(self, event):
        self.data_28.configure(bg='#d9d89a')

    def entered_data_29(self, event):
        self.data_29.configure(bg='#ffffff')

    def leave_data_29(self, event):
        self.data_29.configure(bg='#d9d89a')

    def entered_data_30(self, event):
        self.data_30.configure(bg='#ffffff')

    def leave_data_30(self, event):
        self.data_30.configure(bg='#d9d89a')

    def entered_data_31(self, event):
        self.data_31.configure(bg='#ffffff')

    def leave_data_31(self, event):
        self.data_31.configure(bg='#d9d89a')

    def entered_data_32(self, event):
        self.data_32.configure(bg='#ffffff')

    def leave_data_32(self, event):
        self.data_32.configure(bg='#d9d89a')

    def entered_data_33(self, event):
        self.data_33.configure(bg='#ffffff')

    def leave_data_33(self, event):
        self.data_33.configure(bg='#d9d89a')

    def entered_data_34(self, event):
        self.data_34.configure(bg='#ffffff')

    def leave_data_34(self, event):
        self.data_34.configure(bg='#d9d89a')

    def entered_data_35(self, event):
        self.data_35.configure(bg='#ffffff')

    def leave_data_35(self, event):
        self.data_35.configure(bg='#d9d89a')

    def entered_data_36(self, event):
        self.data_36.configure(bg='#ffffff')

    def leave_data_36(self, event):
        self.data_36.configure(bg='#d9d89a')

    def entered_data_37(self, event):
        self.data_37.configure(bg='#ffffff')

    def leave_data_37(self, event):
        self.data_37.configure(bg='#d9d89a')

    def entered_data_38(self, event):
        self.data_38.configure(bg='#ffffff')

    def leave_data_38(self, event):
        self.data_38.configure(bg='#d9d89a')

    def entered_data_39(self, event):
        self.data_39.configure(bg='#ffffff')

    def leave_data_39(self, event):
        self.data_39.configure(bg='#d9d89a')

    def entered_data_40(self, event):
        self.data_40.configure(bg='#ffffff')

    def leave_data_40(self, event):
        self.data_40.configure(bg='#d9d89a')

    def entered_data_41(self, event):
        self.data_41.configure(bg='#ffffff')

    def leave_data_41(self, event):
        self.data_41.configure(bg='#d9d89a')

    def entered_data_42(self, event):
        self.data_42.configure(bg='#ffffff')

    def leave_data_42(self, event):
        self.data_42.configure(bg='#d9d89a')

    def entered_data_43(self, event):
        self.data_43.configure(bg='#ffffff')

    def leave_data_43(self, event):
        self.data_43.configure(bg='#d9d89a')

    def entered_data_44(self, event):
        self.data_44.configure(bg='#ffffff')

    def leave_data_44(self, event):
        self.data_44.configure(bg='#d9d89a')

    def entered_data_45(self, event):
        self.data_45.configure(bg='#ffffff')

    def leave_data_45(self, event):
        self.data_45.configure(bg='#d9d89a')

    def entered_data_46(self, event):
        self.data_46.configure(bg='#ffffff')

    def leave_data_46(self, event):
        self.data_46.configure(bg='#d9d89a')

    def entered_data_47(self, event):
        self.data_47.configure(bg='#ffffff')

    def leave_data_47(self, event):
        self.data_47.configure(bg='#d9d89a')

    def entered_data_48(self, event):
        self.data_48.configure(bg='#ffffff')

    def leave_data_48(self, event):
        self.data_48.configure(bg='#d9d89a')

    def entered_payment_1(self, event):
        self.payment_options_1.configure(bg = '#ffffff')

    def leave_payment_1(self, event):
        self.payment_options_1.configure(bg = '#fdccff')

    def entered_payment_2(self, event):
        self.payment_options_2.configure(bg = '#ffffff')

    def leave_payment_2(self, event):
        self.payment_options_2.configure(bg = '#fdccff')

    def entered_payment_3(self, event):
        self.payment_options_3.configure(bg = '#ffffff')

    def leave_payment_3(self, event):
        self.payment_options_3.configure(bg = '#fdccff')

    def entered_payment_4(self, event):
        self.payment_options_4.configure(bg = '#ffffff')

    def leave_payment_4(self, event):
        self.payment_options_4.configure(bg = '#fdccff')

    def entered_payment_5(self, event):
        self.payment_options_5.configure(bg = '#ffffff')

    def leave_payment_5(self, event):
        self.payment_options_5.configure(bg = '#fdccff')

    def entered_ad_1(self, event):
        self.address_box_1.configure(bg = '#ffffff')

    def leave_ad_1(self, event):
        self.address_box_1.configure(bg = 'light blue')

    def entered_ad_2(self, event):
        self.address_box_2.configure(bg = '#ffffff')

    def leave_ad_2(self, event):
        self.address_box_2.configure(bg = 'light blue')

    def entered_ad_3(self, event):
        self.address_box_3.configure(bg = '#ffffff')

    def leave_ad_3(self, event):
        self.address_box_3.configure(bg = 'light blue')

    def entered_ad_4(self, event):
        self.address_box_4.configure(bg = '#ffffff')

    def leave_ad_4(self, event):
        self.address_box_4.configure(bg = 'light blue')

    def init_ui(self):
        """This method adds the widgets to the Window"""

        self.heading = tk.Label(self.window_main, text='Welcome to Password Manager', font=(
                                'georgia', 24, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.pic = tk.PhotoImage(file='resources/back.png')
        self.dis = tk.Button(self.window_main, image=self.pic, bg='black', command=self.back, relief='flat')
        self.dis.place(x=5, y=5)

        self.about_image = tk.PhotoImage(file='resources/about.png')
        self.about_icon = tk.Button(self.window_main, image=self.about_image, bg='black', fg='white', relief='flat',
                                    command=self.open_about)
        self.about_icon.place(x=1060, y=0)

        self.greeting = f"Hello! {self.full_name}"
        self.greet_label = tk.Label(self.window_main, text=self.greeting,
                                    bg='black', fg='sky blue', font=('Maiandra GD', 14))
        self.greet_label.place(x=30, y=70)

        self.data_1 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_1'))
        self.data_1.place(x=10, y=100)
        self.data_1.bind('<Enter>', self.entered_data_1)
        self.data_1.bind('<Leave>', self.leave_data_1)

        self.data_2 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_2'))
        self.data_2.place(x=140, y=100)
        self.data_2.bind('<Enter>', self.entered_data_2)
        self.data_2.bind('<Leave>', self.leave_data_2)

        self.data_3 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_3'))
        self.data_3.place(x=270, y=100)
        self.data_3.bind('<Enter>', self.entered_data_3)
        self.data_3.bind('<Leave>', self.leave_data_3)

        self.data_4 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_4'))
        self.data_4.place(x=400, y=100)
        self.data_4.bind('<Enter>', self.entered_data_4)
        self.data_4.bind('<Leave>', self.leave_data_4)

        self.data_5 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_5'))
        self.data_5.place(x=530, y=100)
        self.data_5.bind('<Enter>', self.entered_data_5)
        self.data_5.bind('<Leave>', self.leave_data_5)

        self.data_6 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_6'))
        self.data_6.place(x=660, y=100)
        self.data_6.bind('<Enter>', self.entered_data_6)
        self.data_6.bind('<Leave>', self.leave_data_6)

        self.data_7 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_7'))
        self.data_7.place(x=790, y=100)
        self.data_7.bind('<Enter>', self.entered_data_7)
        self.data_7.bind('<Leave>', self.leave_data_7)

        self.data_8 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_8'))
        self.data_8.place(x=920, y=100)
        self.data_8.bind('<Enter>', self.entered_data_8)
        self.data_8.bind('<Leave>', self.leave_data_8)

        self.data_9 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_9'))
        self.data_9.place(x=10, y=150)
        self.data_9.bind('<Enter>', self.entered_data_9)
        self.data_9.bind('<Leave>', self.leave_data_9)

        self.data_10 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_10'))
        self.data_10.place(x=140, y=150)
        self.data_10.bind('<Enter>', self.entered_data_10)
        self.data_10.bind('<Leave>', self.leave_data_10)

        self.data_11 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_11'))
        self.data_11.place(x=270, y=150)
        self.data_11.bind('<Enter>', self.entered_data_11)
        self.data_11.bind('<Leave>', self.leave_data_11)

        self.data_12 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_12'))
        self.data_12.place(x=400, y=150)
        self.data_12.bind('<Enter>', self.entered_data_12)
        self.data_12.bind('<Leave>', self.leave_data_12)

        self.data_13 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_13'))
        self.data_13.place(x=530, y=150)
        self.data_13.bind('<Enter>', self.entered_data_13)
        self.data_13.bind('<Leave>', self.leave_data_13)

        self.data_14 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_14'))
        self.data_14.place(x=660, y=150)
        self.data_14.bind('<Enter>', self.entered_data_14)
        self.data_14.bind('<Leave>', self.leave_data_14)

        self.data_15 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_15'))
        self.data_15.place(x=790, y=150)
        self.data_15.bind('<Enter>', self.entered_data_15)
        self.data_15.bind('<Leave>', self.leave_data_15)

        self.data_16 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_16'))
        self.data_16.place(x=920, y=150)
        self.data_16.bind('<Enter>', self.entered_data_16)
        self.data_16.bind('<Leave>', self.leave_data_16)

        self.data_17 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_17'))
        self.data_17.place(x=10, y=200)
        self.data_17.bind('<Enter>', self.entered_data_17)
        self.data_17.bind('<Leave>', self.leave_data_17)

        self.data_18 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_18'))
        self.data_18.place(x=140, y=200)
        self.data_18.bind('<Enter>', self.entered_data_18)
        self.data_18.bind('<Leave>', self.leave_data_18)

        self.data_19 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_19'))
        self.data_19.place(x=270, y=200)
        self.data_19.bind('<Enter>', self.entered_data_19)
        self.data_19.bind('<Leave>', self.leave_data_19)

        self.data_20 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_20'))
        self.data_20.place(x=400, y=200)
        self.data_20.bind('<Enter>', self.entered_data_20)
        self.data_20.bind('<Leave>', self.leave_data_20)

        self.data_21 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_21'))
        self.data_21.place(x=530, y=200)
        self.data_21.bind('<Enter>', self.entered_data_21)
        self.data_21.bind('<Leave>', self.leave_data_21)

        self.data_22 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_22'))
        self.data_22.place(x=660, y=200)
        self.data_22.bind('<Enter>', self.entered_data_22)
        self.data_22.bind('<Leave>', self.leave_data_22)

        self.data_23 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_23'))
        self.data_23.place(x=790, y=200)
        self.data_23.bind('<Enter>', self.entered_data_23)
        self.data_23.bind('<Leave>', self.leave_data_23)

        self.data_24 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_24'))
        self.data_24.place(x=920, y=200)
        self.data_24.bind('<Enter>', self.entered_data_24)
        self.data_24.bind('<Leave>', self.leave_data_24)

        self.data_25 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_25'))
        self.data_25.place(x=10, y=250)
        self.data_25.bind('<Enter>', self.entered_data_25)
        self.data_25.bind('<Leave>', self.leave_data_25)

        self.data_26 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_26'))
        self.data_26.place(x=140, y=250)
        self.data_26.bind('<Enter>', self.entered_data_26)
        self.data_26.bind('<Leave>', self.leave_data_26)

        self.data_27 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_27'))
        self.data_27.place(x=270, y=250)
        self.data_27.bind('<Enter>', self.entered_data_27)
        self.data_27.bind('<Leave>', self.leave_data_27)

        self.data_28 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_28'))
        self.data_28.place(x=400, y=250)
        self.data_28.bind('<Enter>', self.entered_data_28)
        self.data_28.bind('<Leave>', self.leave_data_28)

        self.data_29 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_29'))
        self.data_29.place(x=530, y=250)
        self.data_29.bind('<Enter>', self.entered_data_29)
        self.data_29.bind('<Leave>', self.leave_data_29)

        self.data_30 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_30'))
        self.data_30.place(x=660, y=250)
        self.data_30.bind('<Enter>', self.entered_data_30)
        self.data_30.bind('<Leave>', self.leave_data_30)

        self.data_31 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_31'))
        self.data_31.place(x=790, y=250)
        self.data_31.bind('<Enter>', self.entered_data_31)
        self.data_31.bind('<Leave>', self.leave_data_31)

        self.data_32 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_32'))
        self.data_32.place(x=920, y=250)
        self.data_32.bind('<Enter>', self.entered_data_32)
        self.data_32.bind('<Leave>', self.leave_data_32)

        self.data_33 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_33'))
        self.data_33.place(x=10, y=300)
        self.data_33.bind('<Enter>', self.entered_data_33)
        self.data_33.bind('<Leave>', self.leave_data_33)

        self.data_34 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_34'))
        self.data_34.place(x=140, y=300)
        self.data_34.bind('<Enter>', self.entered_data_34)
        self.data_34.bind('<Leave>', self.leave_data_34)

        self.data_35 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_35'))
        self.data_35.place(x=270, y=300)
        self.data_35.bind('<Enter>', self.entered_data_35)
        self.data_35.bind('<Leave>', self.leave_data_35)

        self.data_36 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_36'))
        self.data_36.place(x=400, y=300)
        self.data_36.bind('<Enter>', self.entered_data_36)
        self.data_36.bind('<Leave>', self.leave_data_36)

        self.data_37 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_37'))
        self.data_37.place(x=530, y=300)
        self.data_37.bind('<Enter>', self.entered_data_37)
        self.data_37.bind('<Leave>', self.leave_data_37)

        self.data_38 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_38'))
        self.data_38.place(x=660, y=300)
        self.data_38.bind('<Enter>', self.entered_data_38)
        self.data_38.bind('<Leave>', self.leave_data_38)

        self.data_39 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_39'))
        self.data_39.place(x=790, y=300)
        self.data_39.bind('<Enter>', self.entered_data_39)
        self.data_39.bind('<Leave>', self.leave_data_39)

        self.data_40 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_40'))
        self.data_40.place(x=920, y=300)
        self.data_40.bind('<Enter>', self.entered_data_40)
        self.data_40.bind('<Leave>', self.leave_data_40)

        self.data_41 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_41'))
        self.data_41.place(x=10, y=350)
        self.data_41.bind('<Enter>', self.entered_data_41)
        self.data_41.bind('<Leave>', self.leave_data_41)

        self.data_42 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_42'))
        self.data_42.place(x=140, y=350)
        self.data_42.bind('<Enter>', self.entered_data_42)
        self.data_42.bind('<Leave>', self.leave_data_42)

        self.data_43 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_43'))
        self.data_43.place(x=270, y=350)
        self.data_43.bind('<Enter>', self.entered_data_43)
        self.data_43.bind('<Leave>', self.leave_data_43)

        self.data_44 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_44'))
        self.data_44.place(x=400, y=350)
        self.data_44.bind('<Enter>', self.entered_data_44)
        self.data_44.bind('<Leave>', self.leave_data_44)

        self.data_45 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_45'))
        self.data_45.place(x=530, y=350)
        self.data_45.bind('<Enter>', self.entered_data_45)
        self.data_45.bind('<Leave>', self.leave_data_45)

        self.data_46 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_46'))
        self.data_46.place(x=660, y=350)
        self.data_46.bind('<Enter>', self.entered_data_46)
        self.data_46.bind('<Leave>', self.leave_data_46)

        self.data_47 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_47'))
        self.data_47.place(x=790, y=350)
        self.data_47.bind('<Enter>', self.entered_data_47)
        self.data_47.bind('<Leave>', self.leave_data_47)

        self.data_48 = tk.Button(self.window_main, text='empty', bg='#d9d89a',fg='red', font=('timesnewroman', 13),
                                width=13,command=lambda: self.show_password('data_48'))
        self.data_48.place(x=920, y=350)
        self.data_48.bind('<Enter>', self.entered_data_48)
        self.data_48.bind('<Leave>', self.leave_data_48)

        self.change_the_password_box_name()

        self.payment_options = tk.Label(self.window_main, text='Payment Options',
                                   font=('arial', 16, 'bold'), bg='black', fg='orange')
        self.payment_options.place(x=450, y=390)

        self.payment_options_1 = tk.Button(self.window_main, text='empty', bg='#fdccff', fg='red', width=15, font=(
                                    'arial', 15, 'bold'), command=lambda: self.show_payment('payment_options_1'))
        self.payment_options_1.place(x=50, y=420)
        self.payment_options_1.bind('<Enter>', self.entered_payment_1)
        self.payment_options_1.bind('<Leave>', self.leave_payment_1)

        self.payment_options_2 = tk.Button(self.window_main, text='empty', bg='#fdccff', fg='red', width=15, font=(
                                    'arial', 15, 'bold'), command=lambda: self.show_payment('payment_options_2'))
        self.payment_options_2.place(x=250, y=420)
        self.payment_options_2.bind('<Enter>', self.entered_payment_2)
        self.payment_options_2.bind('<Leave>', self.leave_payment_2)

        self.payment_options_3 = tk.Button(self.window_main, text='empty', bg='#fdccff', fg='red', width=15, font=(
                                        'arial', 15, 'bold'), command=lambda: self.show_payment('payment_options_3'))
        self.payment_options_3.place(x=450, y=420)
        self.payment_options_3.bind('<Enter>', self.entered_payment_3)
        self.payment_options_3.bind('<Leave>', self.leave_payment_3)

        self.payment_options_4 = tk.Button(self.window_main, text='empty', bg='#fdccff', fg='red', width=15, font=(
                                        'arial', 15, 'bold'), command=lambda: self.show_payment('payment_options_4'))
        self.payment_options_4.place(x=650, y=420)
        self.payment_options_4.bind('<Enter>', self.entered_payment_4)
        self.payment_options_4.bind('<Leave>', self.leave_payment_4)

        self.payment_options_5 = tk.Button(self.window_main, text='empty', bg='#fdccff', fg='red', width=15, font=(
                                        'arial', 15, 'bold'), command=lambda: self.show_payment('payment_options_5'))
        self.payment_options_5.place(x=850, y=420)
        self.payment_options_5.bind('<Enter>', self.entered_payment_5)
        self.payment_options_5.bind('<Leave>', self.leave_payment_5)

        self.change_the_payment_box_name()

        self.address_boxes = tk.Label(self.window_main, text='Address Boxes',
                                 font=('arial', 14, 'bold'), bg='black', fg='orange')
        self.address_boxes.place(x=450, y=470)

        self.address_box_1 = tk.Button(self.window_main, text='empty', bg='light blue', fg='red', width=18, font=(
                                'timesnewroman', 16, 'bold'), command=lambda: self.show_address("address_box_1"))
        self.address_box_1.place(x=20, y=500)
        self.address_box_1.bind('<Enter>', self.entered_ad_1)
        self.address_box_1.bind('<Leave>', self.leave_ad_1)

        self.address_box_2 = tk.Button(self.window_main, text='empty', bg='light blue', fg='red', width=18, font=(
                                'timesnewroman', 16, 'bold'), command=lambda: self.show_address("address_box_2"))
        self.address_box_2.place(x=280, y=500)
        self.address_box_2.bind('<Enter>', self.entered_ad_2)
        self.address_box_2.bind('<Leave>', self.leave_ad_2)

        self.address_box_3 = tk.Button(self.window_main, text='empty', bg='light blue', fg='red', width=18, font=(
                                'timesnewroman', 16, 'bold'), command=lambda: self.show_address("address_box_3"))
        self.address_box_3.place(x=540, y=500)
        self.address_box_3.bind('<Enter>', self.entered_ad_3)
        self.address_box_3.bind('<Leave>', self.leave_ad_3)

        self.address_box_4 = tk.Button(self.window_main, text='empty', bg='light blue', fg='red', width=18, font=(
                                'timesnewroman', 16, 'bold'), command=lambda: self.show_address("address_box_4"))
        self.address_box_4.place(x=800, y=500)
        self.address_box_4.bind('<Enter>', self.entered_ad_4)
        self.address_box_4.bind('<Leave>', self.leave_ad_4)

        self.change_the_address_box_name(self.username)

        self.delete_account = tk.Button(self.window_main, text='Delete Your Account', bg='red', fg='white', font=(
                                        'arial', 10, 'bold'), command=self.open_delete_window)
        self.delete_account.place(x=955, y=570)

        self.window_main.focus_force()
        self.window_main.mainloop()


    def change_the_address_box_name(self, username):
        """This method changes the button name after updating the feature name"""

        conn = sq.connect('database.db')
        cursor = conn.cursor()

        sql = f"SELECT fe_name from {username}_address"
        getting = cursor.execute(sql)
        data = getting.fetchall()

        but_1 = data[0][0]
        col_1 = self.change_color(but_1)
        but_2 = data[1][0]
        col_2 = self.change_color(but_2)
        but_3 = data[2][0]
        col_3 = self.change_color(but_3)
        but_4 = data[3][0]
        col_4 = self.change_color(but_4)

        self.address_box_1.configure(text=f"{but_1}", fg=col_1)
        self.address_box_2.configure(text=f"{but_2}", fg=col_2)
        self.address_box_3.configure(text=f"{but_3}", fg=col_3)
        self.address_box_4.configure(text=f"{but_4}", fg=col_4)

        conn.commit()
        conn.close()



    def change_the_payment_box_name(self):
        """This function updates the feature name of the payment buttons"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()

        try:
            sql = f"SELECT fe_name from {self.username}_payment"
            getting = cursor.execute(sql)
            pay_data = getting.fetchall()

            but_1 = pay_data[0][0]
            col_1 = self.change_color(but_1)
            but_2 = pay_data[1][0]
            col_2 = self.change_color(but_2)
            but_3 = pay_data[2][0]
            col_3 = self.change_color(but_3)
            but_4 = pay_data[3][0]
            col_4 = self.change_color(but_4)
            but_5 = pay_data[4][0]
            col_5 = self.change_color(but_5)

            self.payment_options_1.configure(text=f"{but_1}", fg=col_1)
            self.payment_options_2.configure(text=f"{but_2}", fg=col_2)
            self.payment_options_3.configure(text=f"{but_3}", fg=col_3)
            self.payment_options_4.configure(text=f"{but_4}", fg=col_4)
            self.payment_options_5.configure(text=f"{but_5}", fg=col_5)

        except Error as e:
            print(e)

        conn.commit()
        conn.close()

    def change_the_password_box_name(self):
        """This method changes the button names in the password buttons after updating the feature name"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()
        try:
            sql = f"SELECT fe_name from {self.username}_password"
            getting = cursor.execute(sql)
            pay_data = getting.fetchall()

            but_1 = pay_data[0][0]
            col_1 = self.change_color(but_1)
            but_2 = pay_data[1][0]
            col_2 = self.change_color(but_2)
            but_3 = pay_data[2][0]
            col_3 = self.change_color(but_3)
            but_4 = pay_data[3][0]
            col_4 = self.change_color(but_4)
            but_5 = pay_data[4][0]
            col_5 = self.change_color(but_5)
            but_6 = pay_data[5][0]
            col_6 = self.change_color(but_6)
            but_7 = pay_data[6][0]
            col_7 = self.change_color(but_7)
            but_8 = pay_data[7][0]
            col_8 = self.change_color(but_8)
            but_9 = pay_data[8][0]
            col_9 = self.change_color(but_9)
            but_10 = pay_data[9][0]
            col_10 = self.change_color(but_10)
            but_11 = pay_data[10][0]
            col_11 = self.change_color(but_11)
            but_12 = pay_data[11][0]
            col_12 = self.change_color(but_12)
            but_13 = pay_data[12][0]
            col_13 = self.change_color(but_13)
            but_14 = pay_data[13][0]
            col_14 = self.change_color(but_14)
            but_15 = pay_data[14][0]
            col_15 = self.change_color(but_15)
            but_16 = pay_data[15][0]
            col_16 = self.change_color(but_16)
            but_17 = pay_data[16][0]
            col_17 = self.change_color(but_17)
            but_18 = pay_data[17][0]
            col_18 = self.change_color(but_18)
            but_19 = pay_data[18][0]
            col_19 = self.change_color(but_19)
            but_20 = pay_data[19][0]
            col_20 = self.change_color(but_20)
            but_21 = pay_data[20][0]
            col_21 = self.change_color(but_21)
            but_22 = pay_data[21][0]
            col_22 = self.change_color(but_22)
            but_23 = pay_data[22][0]
            col_23 = self.change_color(but_23)
            but_24 = pay_data[23][0]
            col_24 = self.change_color(but_24)
            but_25 = pay_data[24][0]
            col_25 = self.change_color(but_25)
            but_26 = pay_data[25][0]
            col_26 = self.change_color(but_26)
            but_27 = pay_data[26][0]
            col_27 = self.change_color(but_27)
            but_28 = pay_data[27][0]
            col_28 = self.change_color(but_28)
            but_29 = pay_data[28][0]
            col_29 = self.change_color(but_29)
            but_30 = pay_data[29][0]
            col_30 = self.change_color(but_30)
            but_31 = pay_data[30][0]
            col_31 = self.change_color(but_31)
            but_32 = pay_data[31][0]
            col_32 = self.change_color(but_32)
            but_33 = pay_data[32][0]
            col_33 = self.change_color(but_33)
            but_34 = pay_data[33][0]
            col_34 = self.change_color(but_34)
            but_35 = pay_data[34][0]
            col_35 = self.change_color(but_35)
            but_36 = pay_data[35][0]
            col_36 = self.change_color(but_36)
            but_37 = pay_data[36][0]
            col_37 = self.change_color(but_37)
            but_38 = pay_data[37][0]
            col_38 = self.change_color(but_38)
            but_39 = pay_data[38][0]
            col_39 = self.change_color(but_39)
            but_40 = pay_data[39][0]
            col_40 = self.change_color(but_40)
            but_41 = pay_data[40][0]
            col_41 = self.change_color(but_41)
            but_42 = pay_data[41][0]
            col_42 = self.change_color(but_42)
            but_43 = pay_data[42][0]
            col_43 = self.change_color(but_43)
            but_44 = pay_data[43][0]
            col_44 = self.change_color(but_44)
            but_45 = pay_data[44][0]
            col_45 = self.change_color(but_45)
            but_46 = pay_data[45][0]
            col_46 = self.change_color(but_46)
            but_47 = pay_data[46][0]
            col_47 = self.change_color(but_47)
            but_48 = pay_data[47][0]
            col_48 = self.change_color(but_48)

            self.data_1.configure(text=f"{but_1}", fg=col_1)
            self.data_2.configure(text=f"{but_2}", fg=col_2)
            self.data_3.configure(text=f"{but_3}", fg=col_3)
            self.data_4.configure(text=f"{but_4}", fg=col_4)
            self.data_5.configure(text=f"{but_5}", fg=col_5)
            self.data_6.configure(text=f"{but_6}", fg=col_6)
            self.data_7.configure(text=f"{but_7}", fg=col_7)
            self.data_8.configure(text=f"{but_8}", fg=col_8)
            self.data_9.configure(text=f"{but_9}", fg=col_9)
            self.data_10.configure(text=f"{but_10}", fg=col_10)
            self.data_11.configure(text=f"{but_11}", fg=col_11)
            self.data_12.configure(text=f"{but_12}", fg=col_12)
            self.data_13.configure(text=f"{but_13}", fg=col_13)
            self.data_14.configure(text=f"{but_14}", fg=col_14)
            self.data_15.configure(text=f"{but_15}", fg=col_15)
            self.data_16.configure(text=f"{but_16}", fg=col_16)
            self.data_17.configure(text=f"{but_17}", fg=col_17)
            self.data_18.configure(text=f"{but_18}", fg=col_18)
            self.data_19.configure(text=f"{but_19}", fg=col_19)
            self.data_20.configure(text=f"{but_20}", fg=col_20)
            self.data_21.configure(text=f"{but_21}", fg=col_21)
            self.data_22.configure(text=f"{but_22}", fg=col_22)
            self.data_23.configure(text=f"{but_23}", fg=col_23)
            self.data_24.configure(text=f"{but_24}", fg=col_24)
            self.data_25.configure(text=f"{but_25}", fg=col_25)
            self.data_26.configure(text=f"{but_26}", fg=col_26)
            self.data_27.configure(text=f"{but_27}", fg=col_27)
            self.data_28.configure(text=f"{but_28}", fg=col_28)
            self.data_29.configure(text=f"{but_29}", fg=col_29)
            self.data_30.configure(text=f"{but_30}", fg=col_30)
            self.data_31.configure(text=f"{but_31}", fg=col_31)
            self.data_32.configure(text=f"{but_32}", fg=col_32)
            self.data_33.configure(text=f"{but_33}", fg=col_33)
            self.data_34.configure(text=f"{but_34}", fg=col_34)
            self.data_35.configure(text=f"{but_35}", fg=col_35)
            self.data_36.configure(text=f"{but_36}", fg=col_36)
            self.data_37.configure(text=f"{but_37}", fg=col_37)
            self.data_38.configure(text=f"{but_38}", fg=col_38)
            self.data_39.configure(text=f"{but_39}", fg=col_39)
            self.data_40.configure(text=f"{but_40}", fg=col_40)
            self.data_41.configure(text=f"{but_41}", fg=col_41)
            self.data_42.configure(text=f"{but_42}", fg=col_42)
            self.data_43.configure(text=f"{but_43}", fg=col_43)
            self.data_44.configure(text=f"{but_44}", fg=col_44)
            self.data_45.configure(text=f"{but_45}", fg=col_45)
            self.data_46.configure(text=f"{but_46}", fg=col_46)
            self.data_47.configure(text=f"{but_47}", fg=col_47)
            self.data_48.configure(text=f"{but_48}", fg=col_48)

        except Error as e:
            print(e)

        conn.commit()
        conn.close()

    def back(self):
        """This method destroys the Main Window and returns to the Login Window"""

        self.window_main.destroy()
        login.Login_Window()

    def show_password(self,button):
        """This method shows the data in the password_edit module"""
        fe_name,win_username,win_password,reference_1,reference_2 = self.get_password_button_data(button)

        password_edit.Password_Window(self.username,button,fe_name,win_username,win_password,reference_1,reference_2)

    def show_address(self, button):
        """This method shows the data in the address_edit module"""
        fe_name, address_1, address_2, town, district, state, pin = self.get_address_button_data(button)

        address_edit.Address_Window(self.username,button,fe_name,address_1,address_2,town,district,state,pin)

    def show_payment(self, button):
        """This method shows the data in the payment_edit module"""
        fe_name,card_num,name_on_card,expiry,pay_username,pay_password = self.get_payment_button_data(button)

        payment_edit.Payment_Window(self.username,button,fe_name,card_num,name_on_card,expiry,pay_username,pay_password)

    def open_delete_window(self):
        """This will open the delete user window"""
        self.window_main.destroy()
        delete_window.Delete_Window(self.username)

    def get_password_button_data(self, value):
        """This function shows the values of the address related data"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()
        try:
            sql = f"SELECT * FROM {self.username}_password WHERE val_no = '{value}'"
            pass_sql = cursor.execute(sql)
            data = pass_sql.fetchmany()

            fe_name = data[0][1]
            pass_username = data[0][2]
            pass_password = data[0][3]
            ref_1 = data[0][4]
            ref_2 = data[0][5]

            if fe_name[0:5] == 'empty':
                msgb.showwarning('Open first time',
                                 'You are opening this box for the first time please fill the details for further use')
                pass_username = ''
                pass_password = ''
                ref_1 = ''
                ref_2 = ''

            else:
                pass

            return fe_name, pass_username, pass_password, ref_1, ref_2

        except Error as e:
            print(e)

        conn.commit()
        conn.close()

    def get_payment_button_data(self, value):
        """This function shows the values of the payment related data"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()
        try:
            sql = f"SELECT * FROM {self.username}_payment WHERE val_no = '{value}'"
            pass_sql = cursor.execute(sql)
            data = pass_sql.fetchmany()

            fe_name = data[0][1]
            card_number = data[0][2]
            name_on_card = data[0][3]
            expiry_date = data[0][4]
            pay_username = data[0][5]
            pay_password = data[0][6]

            if fe_name[0:5] == 'empty':
                msgb.showwarning('Open first time',
                                 'You are opening this box for the first time please fill the details for further use')
                card_number = ''
                name_on_card = ''
                expiry_date = ''
                pay_username = ''
                pay_password = ''

            else:
                pass

            return fe_name, card_number, name_on_card, expiry_date, pay_username, pay_password

        except Error as e:
            print(e)

        conn.commit()
        conn.close()

    def get_address_button_data(self, value):
        """This function shows the values of the address related data"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()
        try:
            sql = f"SELECT * FROM {self.username}_address WHERE val_no = '{value}'"
            pass_sql = cursor.execute(sql)
            data = pass_sql.fetchmany()

            fe_name = data[0][1]
            address_1 = data[0][2]
            address_2 = data[0][3]
            town = data[0][4]
            district = data[0][5]
            state = data[0][6]
            pin = data[0][7]

            if fe_name[0:5] == 'empty':
                msgb.showwarning('Open first time',
                                 'You are opening this box for the first time please fill the details for further use')
                address_1 = ''
                address_2 = ''
                town = ''
                district = ''
                state = ''
                pin = ''

            else:
                pass

            return fe_name, address_1, address_2, town, district, state, pin

        except Error as e:
            print(e)

        conn.commit()
        conn.close()

    @staticmethod
    def change_color(text):
        """This checks the feature name to change the color the text in the button"""
        if text[0:5] == 'empty' or text == '':
            return 'red'
        else:
            return 'green'

    @staticmethod
    def open_about():
        """This method opens the about window"""
        about.About_Window()

if __name__ == '__main__':
    Main_Window('admin', 'pranav mandava')