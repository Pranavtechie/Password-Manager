"""This module manages the UI of the Sign Up window"""

import tkinter as tk
import login
import back_end
import about
from tkinter import messagebox as msgb


def success_sign_up():
    """This Function shows that sign up was successful and takes to login page"""
    msgb.showinfo('Success Sign Up', "You have signed up successfully")


def save_data():
    """ This function calls the backend and validates the data and saves it"""
    check_p = retype_password_var.get()
    d1 = first_name_var.get()
    d2 = last_name_var.get()
    d3 = sign_up_username_entry_var.get()
    d4 = sign_up_password_entry_var.get()
    d5 = security_question_1_var.get()
    d6 = security_answer_1_var.get()
    d7 = security_question_2_var.get()
    d8 = security_answer_2_var.get()
    
    username_value = back_end.check_username_for_signup(d3)

    if d1 == '':
        msgb.showerror('Error in Sign Up', 'Please Enter your First Name')
        
    elif d2 == '':
        msgb.showerror('Error in Sign Up', 'Please Enter the Last Name')

    elif d1 == d2:
        msgb.showerror('Error in Sign Up', 'Both First Name and Last Name are Same. Please consider to change')
    
    elif d3 == '':
        msgb.showerror('Error in Sign Up', 'Please Enter the Username')

    elif d3 == 'copy':
         msgb.showerror('Error in Sign Up', 'Please choose another username the entered username is used for back_end purpose')

    elif d3 == d1:
        msgb.showerror('Error in Sign Up', 'Your First Name and Username matches please change the username')

    elif d3 == d2:
        msgb.showerror('Error in Sign Up', 'Your Last Name and Username matches please change the username')
        
    elif not username_value:
        msgb.showerror('Error in Sign Up', 'The username already exists, Please Change')
        
    elif d4 == '':
        msgb.showerror('Error in Sign Up', 'Please Enter the Password')
        
    elif d4.isalpha():
        msgb.showerror('Error in Sign Up', 'Your Password only contains Alphabets try including some numbers')
        
    elif d4.isdigit():
        msgb.showerror('Error in Sign Up', 'Your Password only contains number try including some alphabets')
    
    elif  d4 != check_p:
        msgb.showerror('Error in Sign Up', 'Your Passwords do not match please check again')
        
    elif d5 == '':
        msgb.showerror('Error in Sign Up', 'Please fill the security question 1')
        
    elif d6 == '':
        msgb.showerror('Error in Sign Up', 'Please fill the security answer 1')
        
    elif d7 == '':
        msgb.showerror('Error in Sign Up', 'Please fill the security question 2')

    elif d8 == '':
        msgb.showerror('Error in Sign Up', 'Please fill the security answer 2')

    elif d5 == d7:
        msgb.showerror('Error in Sign Up', 'The security questions match please change them')

    elif d6 == d8:
        msgb.showerror('Error in Sign Up', 'The security answers match please change them')

    else:
        back_end.insert_data(d1, d2, d3, d4, d5, d6, d7, d8)



def clear():
    """ This function clears all the Entries in the Window"""
    first_name_var.set('')
    last_name_var.set('')
    sign_up_username_entry_var.set('')
    sign_up_password_entry_var.set('')
    retype_password_var.set('')
    security_question_1_var.set('')
    security_answer_1_var.set('')
    security_question_2_var.set('')
    security_answer_2_var.set('')
    first_name_entry.focus()


def exit():
    """This function closes the Sign Up Window making to exit the Software"""

    window_sign_up.destroy()


def enter_login_page():
    """This function destroy's the existing page and takes you to the Login Page"""

    window_sign_up.destroy()

    login.open_window()


def open_window():
    """This function runs the UI of the Sign Up window"""

    def entered_sign(event):
        sign_up.configure(bg='#a3ffb3')

    def leave_sign(event):
        sign_up.configure(bg='#f1f5e0')

    def entered_clear_button(event):
        clear_button.configure(bg='#a3ffb3')

    def leave_clear_button(event):
        clear_button.configure(bg='#f1f5e0')

    def entered_exit_button(event):
        exit_button.configure(bg='#a3ffb3')

    def leave_exit_button(event):
        exit_button.configure(bg='#f1f5e0')

    def entered_login(event):
        already_user.configure(font=('Maiandra GD', 11, 'underline'))

    def leave_login(event):
        already_user.configure(font=('Maiandra GD', 11))

    global window_sign_up

    window_sign_up = tk.Tk()
    window_sign_up.title('Sign Up')
    window_sign_up.geometry('500x450')
    window_sign_up.resizable(False, False)
    window_sign_up.configure(bg='black')
    window_sign_up.iconbitmap('resources/icon.ico')

    heading = tk.Label(window_sign_up, text='User Registration',
                       font=('arial', 24, 'bold'), bg='black', fg='orange')
    heading.pack()

    about_image = tk.PhotoImage(file='resources/about.png')
    about_icon = tk.Button(window_sign_up, image=about_image, bg='black', fg='white', relief='flat',
                           command=about.open_window)
    about_icon.place(x=465, y=0)

    first_name = tk.Label(window_sign_up, text='First Name', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    first_name.place(x=5, y=50)

    global first_name_var, first_name_entry
    first_name_var = tk.StringVar()
    first_name_entry = tk.Entry(
        window_sign_up, textvariable=first_name_var, bg='#C0C0C0', font=('arial', 12))
    first_name_entry.place(x=100, y=50)
    first_name_entry.focus()

    last_name = tk.Label(window_sign_up, text='Last Name', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    last_name.place(x=5, y=80)

    global last_name_var
    last_name_var = tk.StringVar()
    last_name_entry = tk.Entry(
        window_sign_up, textvariable=last_name_var, bg='#C0C0C0', font=('arial', 12))
    last_name_entry.place(x=100, y=80)

    username = tk.Label(window_sign_up, text='Username', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    username.place(x=60, y=120)

    global sign_up_username_entry_var
    sign_up_username_entry_var = tk.StringVar()
    username_entry = tk.Entry(
        window_sign_up, textvariable=sign_up_username_entry_var, font=('arial', 12), bg='#C0C0C0')
    username_entry.place(x=150, y=120)

    password = tk.Label(window_sign_up, text='Password', font=(
        'arila', 12, 'bold'), bg='black', fg='white')
    password.place(x=60, y=150)

    global sign_up_password_entry_var
    sign_up_password_entry_var = tk.StringVar()
    password_entry = tk.Entry(window_sign_up, font=(
        'arial', 12), bg='#C0C0C0', textvariable=sign_up_password_entry_var, show='*')
    password_entry.place(x=150, y=150)

    retype_password = tk.Label(window_sign_up, text='Retype Password', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    retype_password.place(x=5, y=180)

    global retype_password_var
    retype_password_var = tk.StringVar()
    retype_password_entry = tk.Entry(
        window_sign_up, textvariable=retype_password_var, font=('arial', 12), bg='#C0C0C0', show='*')
    retype_password_entry.place(x=150, y=180)

    note_for_security_question = tk.Label(window_sign_up, font=('arial', 10),
                                          text="Note: The below security questions are used for recovery if you forget your password", bg='black', fg='orange')
    note_for_security_question.place(x=2, y=210)

    security_question_1 = tk.Label(window_sign_up, text='Question 1', font=(
        'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
    security_question_1.place(x=3, y=235)

    global security_question_1_var
    security_question_1_var = tk.StringVar()
    security_question_1_entry = tk.Entry(
        window_sign_up, textvariable=security_question_1_var, font=('arial', 12), bg='#C0C0C0', width=40)
    security_question_1_entry.place(x=100, y=235)

    security_answer_1 = tk.Label(window_sign_up, text='Answer 1', font=(
        'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
    security_answer_1.place(x=14, y=260)

    global security_answer_1_var
    security_answer_1_var = tk.StringVar()
    security_answer_1_entry = tk.Entry(window_sign_up, textvariable=security_answer_1_var, width=20, font=(
        'arial', 12), bg='#C0C0C0', show = "*")
    security_answer_1_entry.place(x=100, y=260)

    security_question_2 = tk.Label(window_sign_up, text='Question 2', font=(
        'arial', 12, 'bold'), bg='black', fg='#98FB98')
    security_question_2.place(x=3, y=300)

    global security_question_2_var
    security_question_2_var = tk.StringVar()
    security_question_2_entry = tk.Entry(window_sign_up, textvariable=security_question_2_var, font=(
        'arial', 12), bg='#C0C0C0', width=40)
    security_question_2_entry.place(x=100, y=300)

    security_answer_2 = tk.Label(window_sign_up, text='Answer 2', font=(
        'arial', 12, 'bold'), bg='black', fg='#98FB98')
    security_answer_2.place(x=14, y=325)

    global security_answer_2_var
    security_answer_2_var = tk.StringVar()
    security_answer_2_entry = tk.Entry(window_sign_up, textvariable=security_answer_2_var, width=20, font=(
        'arial', 12), bg='#C0C0C0',show = "*")
    security_answer_2_entry.place(x=100, y=325)

    sign_up = tk.Button(window_sign_up, text='Sign Up', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=save_data)
    sign_up.place(x=80, y=380)
    sign_up.bind('<Enter>', entered_sign)
    sign_up.bind('<Leave>', leave_sign)

    clear_button = tk.Button(window_sign_up, text='Clear', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=clear)
    clear_button.place(x=210, y=380)
    clear_button.bind('<Enter>', entered_clear_button)
    clear_button.bind('<Leave>', leave_clear_button)

    exit_button = tk.Button(window_sign_up, text='Exit', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=exit)
    exit_button.place(x=340, y=380)
    exit_button.bind('<Enter>', entered_exit_button)
    exit_button.bind('<Leave>', leave_exit_button)

    already_user = tk.Button(window_sign_up, text='Already a User! Sign In Here', bg='black', font=(
        'Maiandra GD', 11,), fg='white', relief='flat', command=enter_login_page)
    already_user.place(x=155, y=420)
    already_user.bind('<Enter>', entered_login)
    already_user.bind('<Leave>', leave_login)

    window_sign_up.focus_force()

    window_sign_up.mainloop()
