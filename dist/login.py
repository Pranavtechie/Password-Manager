"""This is the Login Window for the Password Manager Software"""

import tkinter as tk
import back_end
import sign_up
import forgot_password
import about


def login():
    """Checks the autentication of the user's login credentials"""
    username = username_entry_var.get()
    password = password_entry_var.get()

    back_end.login_for_use(username, password)


def signup():
    """Takes the user to the Sign_Up Window"""

    window_login.destroy()
    sign_up.open_window()


def forgot():
    """Takes the user to the forgot Password Window"""
    window_login.destroy()
    forgot_password.open_window()


def clear():
    """Clear the data entered in the Entry Boxes"""
    username_entry_var.set('')
    password_entry_var.set('')
    username_entry.focus()


def exit():
    """Exits the Appilication and destroy's the Window"""
    window_login.destroy()

def about_window():
    """This function opens the about_window"""
    about.open_window()

def open_window():
    """This function runs the UI of the Login window"""

    def entered_login_button(event):
        login_button.configure(bg='#a3ffb3')

    def leave_login_button(event):
        login_button.configure(bg='#f1f5e0')

    def entered_clear_button(event):
        clear_button.configure(bg='#a3ffb3')

    def leave_clear_button(event):
        clear_button.configure(bg='#f1f5e0')

    def entered_exit_button(event):
        exit_button.configure(bg='#a3ffb3')

    def leave_exit_button(event):
        exit_button.configure(bg='#f1f5e0')

    def entered_sign_up(event):
        sign_up_button.configure(font=('Maiandra GD', 12, 'underline'))

    def leave_sign_up(event):
        sign_up_button.configure(font=('Maiandra GD', 12))

    def entered_forgot(event):
        forgot_password_button.configure(font=('Maiandra GD', 12, 'underline'))

    def leave_forgot(event):
        forgot_password_button.configure(font=('Maiandra GD', 12))

    global window_login
    window_login = tk.Tk()
    window_login.title('Login Page')
    window_login.geometry('400x270')
    window_login.resizable(False, False)
    window_login.configure(bg='black')
    window_login.iconbitmap('resources/icon.ico')

    heading = tk.Label(window_login, text='Please Login!!!', font=(
        'arial', 18, 'bold'), bg='black', fg='orange')
    heading.pack()

    username = tk.Label(window_login, text='Username:', font=(
        'timesnewroman', 15), bg='black', fg='white')
    username.place(x=10, y=60)

    about_image = tk.PhotoImage(file = 'resources/about.png')
    about_icon = tk.Button(window_login, image = about_image, bg = 'black', fg = 'white', relief = 'flat', command = about_window)
    about_icon.place(x = 365, y = 0)

    global username_entry_var, username_entry
    username_entry_var = tk.StringVar()
    username_entry = tk.Entry(window_login, font=('arial', 15),
                              bg='#C0C0C0', textvariable=username_entry_var)
    username_entry.place(x=125, y=60)
    username_entry.focus()

    password = tk.Label(window_login, text='Password:', font=(
        'timesnewroman', 15), bg='black', fg='white')
    password.place(x=10, y=100)


    global password_entry_var
    password_entry_var = tk.StringVar()
    password_entry = tk.Entry(window_login, font=('arial', 15),
                               show='*', bg='#C0C0C0', textvariable=password_entry_var)
    password_entry.place(x=125, y=100)

    login_button = tk.Button(window_login, text='Login', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=login)
    login_button.place(x=50, y=150)
    login_button.bind('<Enter>', entered_login_button)
    login_button.bind('<Leave>', leave_login_button)

    clear_button = tk.Button(window_login, text='Clear', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=clear)
    clear_button.place(x=170, y=150)
    clear_button.bind('<Enter>', entered_clear_button)
    clear_button.bind('<Leave>', leave_clear_button)

    exit_button = tk.Button(window_login, text='Exit', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=exit)
    exit_button.place(x=290, y=150)
    exit_button.bind('<Enter>', entered_exit_button)
    exit_button.bind('<Leave>', leave_exit_button)

    sign_up_button = tk.Button(window_login, text='Not a user! Sign Up Here', bg='black', font=(
        'Maiandra GD', 12), fg='white', relief='flat', command=signup)
    sign_up_button.place(x=110, y=200)
    sign_up_button.bind('<Enter>', entered_sign_up)
    sign_up_button.bind('<Leave>', leave_sign_up)

    forgot_password_button = tk.Button(window_login, text='Forgot Password - Recover your account here', bg='black', font=(
        'Maiandra GD', 12,), fg='white', relief='flat', command=forgot)
    forgot_password_button.place(x=30, y=230)
    forgot_password_button.bind('<Enter>', entered_forgot)
    forgot_password_button.bind('<Leave>', leave_forgot)

    window_login.focus_force()

    window_login.mainloop()
