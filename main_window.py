"""This module manages the UI of the Main Window"""
import tkinter as tk
import login
import about
import address_edit
import password_edit
import payment_edit
import delete_window
import back_end
import sqlite3 as sq
from sqlite3 import Error

def open_delete_window(filled_username):
    """This will open the delete user window"""
    window_main.destroy()
    delete_window.open_window(filled_username)

def change_the_address_box_name(username):
    """This function changes the button name after
updating the feature name"""

    conn = sq.connect('database.db')
    cursor = conn.cursor()

    sql = f"SELECT fe_name from {username}_address"
    getting = cursor.execute(sql)
    data = getting.fetchall()

    but_1 = data[0][0]
    col_1 = change_color(but_1)
    but_2 = data[1][0]
    col_2 = change_color(but_2)
    but_3 = data[2][0]
    col_3 = change_color(but_3)
    but_4 = data[3][0]
    col_4 = change_color(but_4)

    address_box_1.configure(text = f"{but_1}", fg = col_1)
    address_box_2.configure(text = f"{but_2}", fg = col_2)
    address_box_3.configure(text = f"{but_3}", fg = col_3)
    address_box_4.configure(text = f"{but_4}", fg = col_4)

    conn.commit()
    conn.close()

def change_the_payment_box_name(username):
    """This function updates the feature name of the payment buttons"""
    conn = sq.connect('database.db')
    cursor = conn.cursor()

    try:
        sql = f"SELECT fe_name from {username}_payment"
        getting = cursor.execute(sql)
        pay_data = getting.fetchall()

        but_1 = pay_data[0][0]
        col_1 = change_color(but_1)
        but_2 = pay_data[1][0]
        col_2 = change_color(but_2)
        but_3 = pay_data[2][0]
        col_3 = change_color(but_3)
        but_4 = pay_data[3][0]
        col_4 = change_color(but_4)
        but_5 = pay_data[4][0]
        col_5 = change_color(but_5)

        payment_options_1.configure(text=f"{but_1}", fg=col_1)
        payment_options_2.configure(text=f"{but_2}", fg=col_2)
        payment_options_3.configure(text=f"{but_3}", fg=col_3)
        payment_options_4.configure(text=f"{but_4}", fg=col_4)
        payment_options_5.configure(text=f"{but_5}", fg=col_5)

    except Error as e:
        print(e)

    conn.commit()
    conn.close()

def change_the_password_box_name(username):
    """This function changes the button names in the password buttons
after updating the feature name"""
    conn = sq.connect('database.db')
    cursor = conn.cursor()
    try:
        sql = f"SELECT fe_name from {username}_password"
        getting = cursor.execute(sql)
        pay_data = getting.fetchall()

        but_1 = pay_data[0][0]
        col_1 = change_color(but_1)
        but_2 = pay_data[1][0]
        col_2 = change_color(but_2)
        but_3 = pay_data[2][0]
        col_3 = change_color(but_3)
        but_4 = pay_data[3][0]
        col_4 = change_color(but_4)
        but_5 = pay_data[4][0]
        col_5 = change_color(but_5)
        but_6 = pay_data[5][0]
        col_6 = change_color(but_6)
        but_7 = pay_data[6][0]
        col_7 = change_color(but_7)
        but_8 = pay_data[7][0]
        col_8 = change_color(but_8)
        but_9 = pay_data[8][0]
        col_9 = change_color(but_9)
        but_10 = pay_data[9][0]
        col_10= change_color(but_10)
        but_11 = pay_data[10][0]
        col_11 = change_color(but_11)
        but_12 = pay_data[11][0]
        col_12 = change_color(but_12)
        but_13 = pay_data[12][0]
        col_13 = change_color(but_13)
        but_14 = pay_data[13][0]
        col_14 = change_color(but_14)
        but_15 = pay_data[14][0]
        col_15 = change_color(but_15)
        but_16 = pay_data[15][0]
        col_16 = change_color(but_16)
        but_17 = pay_data[16][0]
        col_17 = change_color(but_17)
        but_18 = pay_data[17][0]
        col_18 = change_color(but_18)
        but_19 = pay_data[18][0]
        col_19 = change_color(but_19)
        but_20 = pay_data[19][0]
        col_20 = change_color(but_20)
        but_21 = pay_data[20][0]
        col_21 = change_color(but_21)
        but_22 = pay_data[21][0]
        col_22 = change_color(but_22)
        but_23 = pay_data[22][0]
        col_23 = change_color(but_23)
        but_24 = pay_data[23][0]
        col_24 = change_color(but_24)
        but_25 = pay_data[24][0]
        col_25 = change_color(but_25)
        but_26 = pay_data[25][0]
        col_26 = change_color(but_26)
        but_27 = pay_data[26][0]
        col_27 = change_color(but_27)
        but_28 = pay_data[27][0]
        col_28 = change_color(but_28)
        but_29 = pay_data[28][0]
        col_29 = change_color(but_29)
        but_30 = pay_data[29][0]
        col_30 = change_color(but_30)
        but_31 = pay_data[30][0]
        col_31 = change_color(but_31)
        but_32 = pay_data[31][0]
        col_32 = change_color(but_32)
        but_33 = pay_data[32][0]
        col_33 = change_color(but_33)
        but_34 = pay_data[33][0]
        col_34 = change_color(but_34)
        but_35 = pay_data[34][0]
        col_35 = change_color(but_35)
        but_36 = pay_data[35][0]
        col_36 = change_color(but_36)
        but_37 = pay_data[36][0]
        col_37 = change_color(but_37)
        but_38 = pay_data[37][0]
        col_38 = change_color(but_38)
        but_39 = pay_data[38][0]
        col_39 = change_color(but_39)
        but_40 = pay_data[39][0]
        col_40 = change_color(but_40)
        but_41 = pay_data[40][0]
        col_41 = change_color(but_41)
        but_42 = pay_data[41][0]
        col_42 = change_color(but_42)
        but_43 = pay_data[42][0]
        col_43 = change_color(but_43)
        but_44 = pay_data[43][0]
        col_44 = change_color(but_44)
        but_45 = pay_data[44][0]
        col_45 = change_color(but_45)
        but_46 = pay_data[45][0]
        col_46 = change_color(but_46)
        but_47 = pay_data[46][0]
        col_47 = change_color(but_47)
        but_48 = pay_data[47][0]
        col_48 = change_color(but_48)

        data_1.configure(text=f"{but_1}", fg=col_1)
        data_2.configure(text=f"{but_2}", fg=col_2)
        data_3.configure(text=f"{but_3}", fg=col_3)
        data_4.configure(text=f"{but_4}", fg=col_4)
        data_5.configure(text=f"{but_5}", fg=col_5)
        data_6.configure(text=f"{but_6}", fg=col_6)
        data_7.configure(text=f"{but_7}", fg=col_7)
        data_8.configure(text=f"{but_8}", fg=col_8)
        data_9.configure(text=f"{but_9}", fg=col_9)
        data_10.configure(text=f"{but_10}", fg=col_10)
        data_11.configure(text=f"{but_11}", fg=col_11)
        data_12.configure(text=f"{but_12}", fg=col_12)
        data_13.configure(text=f"{but_13}", fg=col_13)
        data_14.configure(text=f"{but_14}", fg=col_14)
        data_15.configure(text=f"{but_15}", fg=col_15)
        data_16.configure(text=f"{but_16}", fg=col_16)
        data_17.configure(text=f"{but_17}", fg=col_17)
        data_18.configure(text=f"{but_18}", fg=col_18)
        data_19.configure(text=f"{but_19}", fg=col_19)
        data_20.configure(text=f"{but_20}", fg=col_20)
        data_21.configure(text=f"{but_21}", fg=col_21)
        data_22.configure(text=f"{but_22}", fg=col_22)
        data_23.configure(text=f"{but_23}", fg=col_23)
        data_24.configure(text=f"{but_24}", fg=col_24)
        data_25.configure(text=f"{but_25}", fg=col_25)
        data_26.configure(text=f"{but_26}", fg=col_26)
        data_27.configure(text=f"{but_27}", fg=col_27)
        data_28.configure(text=f"{but_28}", fg=col_28)
        data_29.configure(text=f"{but_29}", fg=col_29)
        data_30.configure(text=f"{but_30}", fg=col_30)
        data_31.configure(text=f"{but_31}", fg=col_31)
        data_32.configure(text=f"{but_32}", fg=col_32)
        data_33.configure(text=f"{but_33}", fg=col_33)
        data_34.configure(text=f"{but_34}", fg=col_34)
        data_35.configure(text=f"{but_35}", fg=col_35)
        data_36.configure(text=f"{but_36}", fg=col_36)
        data_37.configure(text=f"{but_37}", fg=col_37)
        data_38.configure(text=f"{but_38}", fg=col_38)
        data_39.configure(text=f"{but_39}", fg=col_39)
        data_40.configure(text=f"{but_40}", fg=col_40)
        data_41.configure(text=f"{but_41}", fg=col_41)
        data_42.configure(text=f"{but_42}", fg=col_42)
        data_43.configure(text=f"{but_43}", fg=col_43)
        data_44.configure(text=f"{but_44}", fg=col_44)
        data_45.configure(text=f"{but_45}", fg=col_45)
        data_46.configure(text=f"{but_46}", fg=col_46)
        data_47.configure(text=f"{but_47}", fg=col_47)
        data_48.configure(text=f"{but_48}", fg=col_48)

    except Error as e:
        print(e)

    conn.commit()
    conn.close()


def change_color(text):
    """This checks the feature name to change the color the text in the button"""
    if text[0:5] == 'empty' or text == '':
        return 'red'
    else:
        return 'green'

def back():
    """This function destroys the main window and returns to the login window"""

    window_main.destroy()

    login.open_window()

def open_about():
    """This function opens the about window"""
    about.About_Window()

def show_password(username, button):
    """This function shows the data in the password_edit module"""
    fe_name, win_username, win_password, reference_1, reference_2 = back_end.get_password_button_data(username, button)

    password_edit.open_window(username, button, fe_name,win_username, win_password, reference_1, reference_2 )

def show_address(username, button):
    """This function shows the data in the address_edit module"""
    fe_name,address_1, address_2, town, district,state, pin = back_end.get_address_button_data(username, button)
    address_edit.open_window(username, button,fe_name,address_1, address_2, town, district,state, pin)

def show_payment(username, button):
    """This function shows the data in the payment_edit module"""
    fe_name, card_number, name_on_card, expiry_date, pay_username, pay_password = back_end.get_payment_button_data(username, button)
    payment_edit.open_window(username, button,fe_name, card_number, name_on_card, expiry_date, pay_username, pay_password)


def open_the_main_window(username, full_name):
    """This function runs the UI of the Main Window"""


    def entered_data_1(event):
        data_1.configure(bg='#ffffff')

    def leave_data_1(event):
        data_1.configure(bg='#d9d89a')

    def entered_data_2(event):
        data_2.configure(bg='#ffffff')

    def leave_data_2(event):
        data_2.configure(bg='#d9d89a')

    def entered_data_3(event):
        data_3.configure(bg='#ffffff')

    def leave_data_3(event):
        data_3.configure(bg='#d9d89a')

    def entered_data_4(event):
        data_4.configure(bg='#ffffff')

    def leave_data_4(event):
        data_4.configure(bg='#d9d89a')

    def entered_data_5(event):
        data_5.configure(bg='#ffffff')

    def leave_data_5(event):
        data_5.configure(bg='#d9d89a')

    def entered_data_6(event):
        data_6.configure(bg='#ffffff')

    def leave_data_6(event):
        data_6.configure(bg='#d9d89a')

    def entered_data_7(event):
        data_7.configure(bg='#ffffff')

    def leave_data_7(event):
        data_7.configure(bg='#d9d89a')

    def entered_data_8(event):
        data_8.configure(bg='#ffffff')

    def leave_data_8(event):
        data_8.configure(bg='#d9d89a')

    def entered_data_9(event):
        data_9.configure(bg='#ffffff')

    def leave_data_9(event):
        data_9.configure(bg='#d9d89a')

    def entered_data_10(event):
        data_10.configure(bg='#ffffff')

    def leave_data_10(event):
        data_10.configure(bg='#d9d89a')

    def entered_data_11(event):
        data_11.configure(bg='#ffffff')

    def leave_data_11(event):
        data_11.configure(bg='#d9d89a')

    def entered_data_12(event):
        data_12.configure(bg='#ffffff')

    def leave_data_12(event):
        data_12.configure(bg='#d9d89a')

    def entered_data_13(event):
        data_13.configure(bg='#ffffff')

    def leave_data_13(event):
        data_13.configure(bg='#d9d89a')

    def entered_data_14(event):
        data_14.configure(bg='#ffffff')

    def leave_data_14(event):
        data_14.configure(bg='#d9d89a')

    def entered_data_15(event):
        data_15.configure(bg='#ffffff')

    def leave_data_15(event):
        data_15.configure(bg='#d9d89a')

    def entered_data_16(event):
        data_16.configure(bg='#ffffff')

    def leave_data_16(event):
        data_16.configure(bg='#d9d89a')

    def entered_data_17(event):
        data_17.configure(bg='#ffffff')

    def leave_data_17(event):
        data_17.configure(bg='#d9d89a')

    def entered_data_18(event):
        data_18.configure(bg='#ffffff')

    def leave_data_18(event):
        data_18.configure(bg='#d9d89a')

    def entered_data_19(event):
        data_19.configure(bg='#ffffff')

    def leave_data_19(event):
        data_19.configure(bg='#d9d89a')

    def entered_data_20(event):
        data_20.configure(bg='#ffffff')

    def leave_data_20(event):
        data_20.configure(bg='#d9d89a')

    def entered_data_21(event):
        data_21.configure(bg='#ffffff')

    def leave_data_21(event):
        data_21.configure(bg='#d9d89a')

    def entered_data_22(event):
        data_22.configure(bg='#ffffff')

    def leave_data_22(event):
        data_22.configure(bg='#d9d89a')

    def entered_data_23(event):
        data_23.configure(bg='#ffffff')

    def leave_data_23(event):
        data_23.configure(bg='#d9d89a')

    def entered_data_24(event):
        data_24.configure(bg='#ffffff')

    def leave_data_24(event):
        data_24.configure(bg='#d9d89a')

    def entered_data_25(event):
        data_25.configure(bg='#ffffff')

    def leave_data_25(event):
        data_25.configure(bg='#d9d89a')

    def entered_data_26(event):
        data_26.configure(bg='#ffffff')

    def leave_data_26(event):
        data_26.configure(bg='#d9d89a')

    def entered_data_27(event):
        data_27.configure(bg='#ffffff')

    def leave_data_27(event):
       data_27.configure(bg='#d9d89a')

    def entered_data_28(event):
        data_28.configure(bg='#ffffff')

    def leave_data_28(event):
        data_28.configure(bg='#d9d89a')

    def entered_data_29(event):
        data_29.configure(bg='#ffffff')

    def leave_data_29(event):
        data_29.configure(bg='#d9d89a')

    def entered_data_30(event):
        data_30.configure(bg='#ffffff')

    def leave_data_30(event):
        data_30.configure(bg='#d9d89a')

    def entered_data_31(event):
        data_31.configure(bg='#ffffff')

    def leave_data_31(event):
        data_31.configure(bg='#d9d89a')

    def entered_data_32(event):
        data_32.configure(bg='#ffffff')

    def leave_data_32(event):
        data_32.configure(bg='#d9d89a')

    def entered_data_33(event):
        data_33.configure(bg='#ffffff')

    def leave_data_33(event):
        data_33.configure(bg='#d9d89a')

    def entered_data_34(event):
        data_34.configure(bg='#ffffff')

    def leave_data_34(event):
        data_34.configure(bg='#d9d89a')

    def entered_data_35(event):
        data_35.configure(bg='#ffffff')

    def leave_data_35(event):
        data_35.configure(bg='#d9d89a')

    def entered_data_36(event):
        data_36.configure(bg='#ffffff')

    def leave_data_36(event):
        data_36.configure(bg='#d9d89a')

    def entered_data_37(event):
        data_37.configure(bg='#ffffff')

    def leave_data_37(event):
        data_37.configure(bg='#d9d89a')

    def entered_data_38(event):
        data_38.configure(bg='#ffffff')

    def leave_data_38(event):
        data_38.configure(bg='#d9d89a')

    def entered_data_39(event):
        data_39.configure(bg='#ffffff')

    def leave_data_39(event):
        data_39.configure(bg='#d9d89a')

    def entered_data_40(event):
        data_40.configure(bg='#ffffff')

    def leave_data_40(event):
        data_40.configure(bg='#d9d89a')

    def entered_data_41(event):
        data_41.configure(bg='#ffffff')

    def leave_data_41(event):
        data_41.configure(bg='#d9d89a')

    def entered_data_42(event):
        data_42.configure(bg='#ffffff')

    def leave_data_42(event):
        data_42.configure(bg='#d9d89a')

    def entered_data_43(event):
        data_43.configure(bg='#ffffff')

    def leave_data_43(event):
        data_43.configure(bg='#d9d89a')

    def entered_data_44(event):
        data_44.configure(bg='#ffffff')

    def leave_data_44(event):
        data_44.configure(bg='#d9d89a')

    def entered_data_45(event):
        data_45.configure(bg='#ffffff')

    def leave_data_45(event):
        data_45.configure(bg='#d9d89a')

    def entered_data_46(event):
        data_46.configure(bg='#ffffff')

    def leave_data_46(event):
        data_46.configure(bg='#d9d89a')

    def entered_data_47(event):
        data_47.configure(bg='#ffffff')

    def leave_data_47(event):
        data_47.configure(bg='#d9d89a')

    def entered_data_48(event):
        data_48.configure(bg='#ffffff')

    def leave_data_48(event):
        data_48.configure(bg='#d9d89a')



    def entered_payment_1(event):
        payment_options_1.configure(bg = '#ffffff')

    def leave_payment_1(event):
        payment_options_1.configure(bg = '#fdccff')

    def entered_payment_2(event):
        payment_options_2.configure(bg = '#ffffff')

    def leave_payment_2(event):
        payment_options_2.configure(bg = '#fdccff')

    def entered_payment_3(event):
        payment_options_3.configure(bg = '#ffffff')

    def leave_payment_3(event):
        payment_options_3.configure(bg = '#fdccff')

    def entered_payment_4(event):
        payment_options_4.configure(bg = '#ffffff')

    def leave_payment_4(event):
        payment_options_4.configure(bg = '#fdccff')

    def entered_payment_5(event):
        payment_options_5.configure(bg = '#ffffff')

    def leave_payment_5(event):
        payment_options_5.configure(bg = '#fdccff')

    def entered_ad_1(event):
        address_box_1.configure(bg = '#ffffff')

    def leave_ad_1(event):
        address_box_1.configure(bg = 'light blue')

    def entered_ad_2(event):
        address_box_2.configure(bg = '#ffffff')

    def leave_ad_2(event):
        address_box_2.configure(bg = 'light blue')

    def entered_ad_3(event):
        address_box_3.configure(bg = '#ffffff')

    def leave_ad_3(event):
        address_box_3.configure(bg = 'light blue')

    def entered_ad_4(event):
        address_box_4.configure(bg = '#ffffff')

    def leave_ad_4(event):
        address_box_4.configure(bg = 'light blue')



    global window_main
    window_main = tk.Tk()
    window_main.title('Password Handler')
    window_main.geometry('1100x600')
    window_main.resizable(False, False)
    window_main.configure(bg='black')
    window_main.iconbitmap('resources/icon.ico')

    heading = tk.Label(window_main, text='Welcome to Password Manager', font=(
                        'georgia', 24, 'bold'), bg='black', fg='orange')
    heading.pack()

    pic = tk.PhotoImage(file = 'resources/back.png')
    dis = tk.Button(window_main, image = pic, bg = 'black', command = back, relief = 'flat')
    dis.place(x = 5, y = 5)

    about_image = tk.PhotoImage(file='resources/about.png')
    about_icon = tk.Button(window_main, image=about_image, bg='black', fg='white', relief='flat',
                           command= open_about)
    about_icon.place(x=1060, y=0)

    greeting = f"Hello! {full_name}"
    greet_label = tk.Label(window_main, text=greeting,
                           bg='black', fg='sky blue', font=('Maiandra GD', 14))
    greet_label.place(x=30, y=70)

    global data_1
    data_1 = tk.Button(window_main, text='empty', bg='#d9d89a',
                       fg='red', font=('timesnewroman', 13), width=13, command = lambda: show_password(username,'data_1'))
    data_1.place(x=10, y=100)
    data_1.bind('<Enter>', entered_data_1)
    data_1.bind('<Leave>', leave_data_1)

    global data_2
    data_2 = tk.Button(window_main, text='empty', bg='#d9d89a',
                       fg='red', font=('timesnewroman', 13), width=13, command = lambda: show_password(username,'data_2'))
    data_2.place(x=140, y=100)
    data_2.bind('<Enter>', entered_data_2)
    data_2.bind('<Leave>', leave_data_2)

    global data_3
    data_3 = tk.Button(window_main, text='empty', bg='#d9d89a',
                       fg='red', font=('timesnewroman', 13), width=13, command = lambda: show_password(username,'data_3'))
    data_3.place(x=270, y=100)
    data_3.bind('<Enter>', entered_data_3)
    data_3.bind('<Leave>', leave_data_3)

    global data_4
    data_4 = tk.Button(window_main, text='empty', bg='#d9d89a',
                       fg='red', font=('timesnewroman', 13), width=13, command = lambda: show_password(username,'data_4'))
    data_4.place(x=400, y=100)
    data_4.bind('<Enter>', entered_data_4)
    data_4.bind('<Leave>', leave_data_4)

    global data_5
    data_5 = tk.Button(window_main, text='empty', bg='#d9d89a',
                       fg='red', font=('timesnewroman', 13), width=13, command = lambda: show_password(username,'data_5'))
    data_5.place(x=530, y=100)
    data_5.bind('<Enter>', entered_data_5)
    data_5.bind('<Leave>', leave_data_5)

    global data_6
    data_6 = tk.Button(window_main, text='empty', bg='#d9d89a',
                       fg='red', font=('timesnewroman', 13), width=13, command = lambda: show_password(username,'data_6'))
    data_6.place(x=660, y=100)
    data_6.bind('<Enter>', entered_data_6)
    data_6.bind('<Leave>', leave_data_6)

    global data_7
    data_7 = tk.Button(window_main, text='empty', bg='#d9d89a',
                       fg='red', font=('timesnewroman', 13), width=13, command = lambda: show_password(username,'data_7'))
    data_7.place(x=790, y=100)
    data_7.bind('<Enter>', entered_data_7)
    data_7.bind('<Leave>', leave_data_7)

    global data_8
    data_8 = tk.Button(window_main, text='empty', bg='#d9d89a',
                       fg='red', font=('timesnewroman', 13), width=13, command = lambda: show_password(username,'data_8'))
    data_8.place(x=920, y=100)
    data_8.bind('<Enter>', entered_data_8)
    data_8.bind('<Leave>', leave_data_8)

    global data_9
    data_9 = tk.Button(window_main, text='empty', bg='#d9d89a',
                       fg='red', font=('timesnewroman', 13), width=13, command = lambda: show_password(username,'data_9'))
    data_9.place(x=10, y=150)
    data_9.bind('<Enter>', entered_data_9)
    data_9.bind('<Leave>', leave_data_9)

    global data_10
    data_10 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_10'))
    data_10.place(x=140, y=150)
    data_10.bind('<Enter>', entered_data_10)
    data_10.bind('<Leave>', leave_data_10)

    global data_11
    data_11 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_11'))
    data_11.place(x=270, y=150)
    data_11.bind('<Enter>', entered_data_11)
    data_11.bind('<Leave>', leave_data_11)

    global data_12
    data_12 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_12'))
    data_12.place(x=400, y=150)
    data_12.bind('<Enter>', entered_data_12)
    data_12.bind('<Leave>', leave_data_12)

    global data_13
    data_13 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_13'))
    data_13.place(x=530, y=150)
    data_13.bind('<Enter>', entered_data_13)
    data_13.bind('<Leave>', leave_data_13)

    global data_14
    data_14 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_14'))
    data_14.place(x=660, y=150)
    data_14.bind('<Enter>', entered_data_14)
    data_14.bind('<Leave>', leave_data_14)

    global data_15
    data_15 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_15'))
    data_15.place(x=790, y=150)
    data_15.bind('<Enter>', entered_data_15)
    data_15.bind('<Leave>', leave_data_15)

    global data_16
    data_16 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_16'))
    data_16.place(x=920, y=150)
    data_16.bind('<Enter>', entered_data_16)
    data_16.bind('<Leave>', leave_data_16)

    global data_17
    data_17 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_17'))
    data_17.place(x=10, y=200)
    data_17.bind('<Enter>', entered_data_17)
    data_17.bind('<Leave>', leave_data_17)

    global data_18
    data_18 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_18'))
    data_18.place(x=140, y=200)
    data_18.bind('<Enter>', entered_data_18)
    data_18.bind('<Leave>', leave_data_18)

    global data_19
    data_19 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_19'))
    data_19.place(x=270, y=200)
    data_19.bind('<Enter>', entered_data_19)
    data_19.bind('<Leave>', leave_data_19)

    global data_20
    data_20 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_20'))
    data_20.place(x=400, y=200)
    data_20.bind('<Enter>', entered_data_20)
    data_20.bind('<Leave>', leave_data_20)

    global data_21
    data_21 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_21'))
    data_21.place(x=530, y=200)
    data_21.bind('<Enter>', entered_data_21)
    data_21.bind('<Leave>', leave_data_21)

    global data_22
    data_22 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_22'))
    data_22.place(x=660, y=200)
    data_22.bind('<Enter>', entered_data_22)
    data_22.bind('<Leave>', leave_data_22)

    global data_23
    data_23 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_23'))
    data_23.place(x=790, y=200)
    data_23.bind('<Enter>', entered_data_23)
    data_23.bind('<Leave>', leave_data_23)

    global data_24
    data_24 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_24'))
    data_24.place(x=920, y=200)
    data_24.bind('<Enter>', entered_data_24)
    data_24.bind('<Leave>', leave_data_24)

    global data_25
    data_25 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_25'))
    data_25.place(x=10, y=250)
    data_25.bind('<Enter>', entered_data_25)
    data_25.bind('<Leave>', leave_data_25)

    global data_26
    data_26 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_26'))
    data_26.place(x=140, y=250)
    data_26.bind('<Enter>', entered_data_26)
    data_26.bind('<Leave>', leave_data_26)

    global data_27
    data_27 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_27'))
    data_27.place(x=270, y=250)
    data_27.bind('<Enter>', entered_data_27)
    data_27.bind('<Leave>', leave_data_27)

    global data_28
    data_28 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_28'))
    data_28.place(x=400, y=250)
    data_28.bind('<Enter>', entered_data_28)
    data_28.bind('<Leave>', leave_data_28)

    global data_29
    data_29 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_29'))
    data_29.place(x=530, y=250)
    data_29.bind('<Enter>', entered_data_29)
    data_29.bind('<Leave>', leave_data_29)

    global data_30
    data_30 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_30'))
    data_30.place(x=660, y=250)
    data_30.bind('<Enter>', entered_data_30)
    data_30.bind('<Leave>', leave_data_30)

    global data_31
    data_31 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_31'))
    data_31.place(x=790, y=250)
    data_31.bind('<Enter>', entered_data_31)
    data_31.bind('<Leave>', leave_data_31)

    global data_32
    data_32 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_32'))
    data_32.place(x=920, y=250)
    data_32.bind('<Enter>', entered_data_32)
    data_32.bind('<Leave>', leave_data_32)

    global data_33
    data_33 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_33'))
    data_33.place(x=10, y=300)
    data_33.bind('<Enter>', entered_data_33)
    data_33.bind('<Leave>', leave_data_33)

    global data_34
    data_34 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_34'))
    data_34.place(x=140, y=300)
    data_34.bind('<Enter>', entered_data_34)
    data_34.bind('<Leave>', leave_data_34)

    global data_35
    data_35 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_35'))
    data_35.place(x=270, y=300)
    data_35.bind('<Enter>', entered_data_35)
    data_35.bind('<Leave>', leave_data_35)

    global data_36
    data_36 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_36'))
    data_36.place(x=400, y=300)
    data_36.bind('<Enter>', entered_data_36)
    data_36.bind('<Leave>', leave_data_36)

    global data_37
    data_37 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_37'))
    data_37.place(x=530, y=300)
    data_37.bind('<Enter>', entered_data_37)
    data_37.bind('<Leave>', leave_data_37)

    global data_38
    data_38 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_38'))
    data_38.place(x=660, y=300)
    data_38.bind('<Enter>', entered_data_38)
    data_38.bind('<Leave>', leave_data_38)

    global data_39
    data_39 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_39'))
    data_39.place(x=790, y=300)
    data_39.bind('<Enter>', entered_data_39)
    data_39.bind('<Leave>', leave_data_39)

    global data_40
    data_40 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_40'))
    data_40.place(x=920, y=300)
    data_40.bind('<Enter>', entered_data_40)
    data_40.bind('<Leave>', leave_data_40)

    global data_41
    data_41 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_41'))
    data_41.place(x=10, y=350)
    data_41.bind('<Enter>', entered_data_41)
    data_41.bind('<Leave>', leave_data_41)

    global data_42
    data_42 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_42'))
    data_42.place(x=140, y=350)
    data_42.bind('<Enter>', entered_data_42)
    data_42.bind('<Leave>', leave_data_42)

    global data_43
    data_43 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_43'))
    data_43.place(x=270, y=350)
    data_43.bind('<Enter>', entered_data_43)
    data_43.bind('<Leave>', leave_data_43)

    global data_44
    data_44 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_44'))
    data_44.place(x=400, y=350)
    data_44.bind('<Enter>', entered_data_44)
    data_44.bind('<Leave>', leave_data_44)

    global data_45
    data_45 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_45'))
    data_45.place(x=530, y=350)
    data_45.bind('<Enter>', entered_data_45)
    data_45.bind('<Leave>', leave_data_45)

    global data_46
    data_46 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_46'))
    data_46.place(x=660, y=350)
    data_46.bind('<Enter>', entered_data_46)
    data_46.bind('<Leave>', leave_data_46)

    global data_47
    data_47 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_47'))
    data_47.place(x=790, y=350)
    data_47.bind('<Enter>', entered_data_47)
    data_47.bind('<Leave>', leave_data_47)

    global data_48
    data_48 = tk.Button(window_main, text='empty', bg='#d9d89a',
                        fg='red', font=('timesnewroman', 13), width=13,command = lambda: show_password(username,'data_48'))
    data_48.place(x=920, y=350)
    data_48.bind('<Enter>', entered_data_48)
    data_48.bind('<Leave>', leave_data_48)

    change_the_password_box_name(username)

    payment_options = tk.Label(window_main, text='Payment Options',
                               font=('arial', 16, 'bold'), bg='black', fg='orange')
    payment_options.place(x=450, y=390)

    global payment_options_1
    payment_options_1 = tk.Button(window_main, text='empty', bg='#fdccff', fg='red', width=15,font=(
                                'arial', 15, 'bold'),command = lambda: show_payment(username, 'payment_options_1'))
    payment_options_1.place(x=50, y=420)
    payment_options_1.bind('<Enter>', entered_payment_1)
    payment_options_1.bind('<Leave>', leave_payment_1)

    global payment_options_2
    payment_options_2 = tk.Button(window_main, text='empty', bg='#fdccff', fg='red', width=15,font=(
                                'arial', 15, 'bold'),command = lambda: show_payment(username, 'payment_options_2'))
    payment_options_2.place(x=250, y=420)
    payment_options_2.bind('<Enter>', entered_payment_2)
    payment_options_2.bind('<Leave>', leave_payment_2)

    global payment_options_3
    payment_options_3 = tk.Button(window_main, text='empty', bg='#fdccff', fg='red', width=15,font=(
                                'arial', 15, 'bold'),command = lambda: show_payment(username, 'payment_options_3'))
    payment_options_3.place(x=450, y=420)
    payment_options_3.bind('<Enter>', entered_payment_3)
    payment_options_3.bind('<Leave>', leave_payment_3)

    global payment_options_4
    payment_options_4 = tk.Button(window_main, text='empty', bg='#fdccff', fg='red', width=15,font=(
                                'arial', 15, 'bold'),command = lambda: show_payment(username, 'payment_options_4'))
    payment_options_4.place(x=650, y=420)
    payment_options_4.bind('<Enter>', entered_payment_4)
    payment_options_4.bind('<Leave>', leave_payment_4)

    global payment_options_5
    payment_options_5 = tk.Button(window_main, text='empty', bg='#fdccff', fg='red', width=15,font=(
                                'arial', 15, 'bold'),command = lambda: show_payment(username, 'payment_options_5'))
    payment_options_5.place(x=850, y=420)
    payment_options_5.bind('<Enter>', entered_payment_5)
    payment_options_5.bind('<Leave>', leave_payment_5)

    change_the_payment_box_name(username)

    address_boxes = tk.Label(window_main, text='Address Boxes',
                             font=('arial', 14, 'bold'), bg='black', fg='orange')
    address_boxes.place(x=450, y=470)

    global address_box_1
    address_box_1 = tk.Button(window_main, text='empty', bg='light blue', fg='red', width=18,font=(
                    'timesnewroman', 16, 'bold'),  command = lambda: show_address(username,"address_box_1"))
    address_box_1.place(x=20, y=500)
    address_box_1.bind('<Enter>', entered_ad_1)
    address_box_1.bind('<Leave>', leave_ad_1)

    global address_box_2
    address_box_2 = tk.Button(window_main, text='empty', bg='light blue', fg='red', width=18, font=(
                            'timesnewroman', 16, 'bold'), command = lambda: show_address(username,"address_box_2"))
    address_box_2.place(x=280, y=500)
    address_box_2.bind('<Enter>', entered_ad_2)
    address_box_2.bind('<Leave>', leave_ad_2)

    global address_box_3
    address_box_3 = tk.Button(window_main, text='empty', bg='light blue', fg='red', width=18,font=(
                            'timesnewroman', 16, 'bold'),  command = lambda: show_address(username,"address_box_3"))
    address_box_3.place(x=540, y=500)
    address_box_3.bind('<Enter>', entered_ad_3)
    address_box_3.bind('<Leave>', leave_ad_3)


    global address_box_4
    address_box_4 = tk.Button(window_main, text='empty',bg='light blue', fg='red', width=18, font=(
                                'timesnewroman', 16, 'bold'),  command = lambda: show_address(username,"address_box_4"))
    address_box_4.place(x=800, y=500)
    address_box_4.bind('<Enter>', entered_ad_4)
    address_box_4.bind('<Leave>', leave_ad_4)

    change_the_address_box_name(username)

    delete_account = tk.Button(window_main, text = 'Delete Your Account', bg = 'red', fg = 'white',font = (
                                'arial',10, 'bold'),  command = lambda: open_delete_window(username))
    delete_account.place(x = 955, y = 570)

    window_main.focus_force()
    window_main.mainloop()
