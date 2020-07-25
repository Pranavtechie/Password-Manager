"""This is the Login Window for the Password Manager Software"""

import tkinter as tk
from tkinter import messagebox as msgb
from sqlite3 import Error
import sign_up
import forgot_password
import about
import main_window
import sqlite3 as sq
import hashlib as hl


class Login_Window(object):

    def __init__(self):
        """This __init__ method is to defines the Login Window elements"""
        self.window_login = tk.Tk()
        self.window_login.title('Login Page')
        self.window_login.geometry('400x270')
        self.window_login.resizable(False, False)
        self.window_login.configure(bg='black')
        self.window_login.iconbitmap('resources/icon.ico')

        self.init_ui()

    def entered_login_button(self, event):
        self.login_button.configure(bg='#a3ffb3')

    def leave_login_button(self, event):
        self.login_button.configure(bg='#f1f5e0')

    def entered_clear_button(self, event):
        self.clear_button.configure(bg='#a3ffb3')

    def leave_clear_button(self, event):
        self.clear_button.configure(bg='#f1f5e0')

    def entered_exit_button(self, event):
        self.exit_button.configure(bg='#a3ffb3')

    def leave_exit_button(self, event):
        self.exit_button.configure(bg='#f1f5e0')

    def entered_sign_up(self, event):
        self.sign_up_button.configure(font=('Maiandra GD', 12, 'underline'))

    def leave_sign_up(self, event):
        self.sign_up_button.configure(font=('Maiandra GD', 12))

    def entered_forgot(self, event):
        self.forgot_password_button.configure(font=('Maiandra GD', 12, 'underline'))

    def leave_forgot(self, event):
        self.forgot_password_button.configure(font=('Maiandra GD', 12))

    def init_ui(self):

        self.heading = tk.Label(self.window_login, text='Please Login!!!', font=(
            'arial', 18, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.username_label = tk.Label(self.window_login, text='Username:', font=(
            'timesnewroman', 15), bg='black', fg='white')
        self.username_label.place(x=10, y=60)

        self.about_image = tk.PhotoImage(file='resources/about.png')
        self.about_icon = tk.Button(self.window_login, image=self.about_image, bg='black', fg='white', relief='flat',
                               command=self.about_window)
        self.about_icon.place(x=365, y=0)


        self.username_entry_var = tk.StringVar()
        self.username_entry = tk.Entry(self.window_login, font=('arial', 15),
                                  bg='#C0C0C0', textvariable=self.username_entry_var)
        self.username_entry.place(x=125, y=60)
        self.username_entry.focus()

        self.password = tk.Label(self.window_login, text='Password:', font=(
            'timesnewroman', 15), bg='black', fg='white')
        self.password.place(x=10, y=100)

        self.password_entry_var = tk.StringVar()
        self.password_entry = tk.Entry(self.window_login, font=('arial', 15),
                                  show='*', bg='#C0C0C0', textvariable=self.password_entry_var)
        self.password_entry.place(x=125, y=100)

        self.login_button = tk.Button(self.window_login, text='Login', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.login)
        self.login_button.place(x=50, y=150)
        self.login_button.bind('<Enter>', self.entered_login_button)
        self.login_button.bind('<Leave>', self.leave_login_button)

        self.clear_button = tk.Button(self.window_login, text='Clear', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.clear)
        self.clear_button.place(x=170, y=150)
        self.clear_button.bind('<Enter>', self.entered_clear_button)
        self.clear_button.bind('<Leave>', self.leave_clear_button)

        self.exit_button = tk.Button(self.window_login, text='Exit', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.exit)
        self.exit_button.place(x=290, y=150)
        self.exit_button.bind('<Enter>', self.entered_exit_button)
        self.exit_button.bind('<Leave>', self.leave_exit_button)

        self.sign_up_button = tk.Button(self.window_login, text='Not a user! Sign Up Here', bg='black', font=(
            'Maiandra GD', 12), fg='white', relief='flat', command=self.signup)
        self.sign_up_button.place(x=110, y=200)
        self.sign_up_button.bind('<Enter>', self.entered_sign_up)
        self.sign_up_button.bind('<Leave>', self.leave_sign_up)

        self.forgot_password_button = tk.Button(self.window_login, text='Forgot Password - Recover your account here',
                                                bg='black',font=('Maiandra GD', 12,), fg='white', relief='flat',
                                                command=self.open_forgot_password_window)
        self.forgot_password_button.place(x=30, y=230)
        self.forgot_password_button.bind('<Enter>', self.entered_forgot)
        self.forgot_password_button.bind('<Leave>', self.leave_forgot)

        self.window_login.focus_force()

        self.window_login.mainloop()

    def signup(self):
        """Takes the user to the Sign_Up Window"""

        self.window_login.destroy()
        sign_up.Sign_Up_Window()

    def open_forgot_password_window(self):
        """Takes the user to the forgot Password Window"""
        self.window_login.destroy()
        forgot_password.Forgot_Password()

    def exit(self):
        """Exits the Appilication and destroy's the Window"""

        self.window_login.destroy()


    def clear(self):
        """Clear the data entered in the Entry Boxes"""
        self.username_entry_var.set('')
        self.password_entry_var.set('')
        self.username_entry.focus()

    def login(self):
        """Checks the authentication of the user's login credentials"""
        get_username = self.username_entry_var.get()
        get_password = self.password_entry_var.get()

        self.login_for_use(get_username, get_password)

    def login_for_use(self, username, text_password):
        """This method is for validating the Login of the user"""

        global username_credentials, password_credentials
        word = hl.sha256(text_password.encode('utf-8'))
        password = word.hexdigest()

        conn = sq.connect('database.db')
        cursor = conn.cursor()

        try:
            cursor.execute('SELECT COUNT(username) FROM users_data')
            count = cursor.fetchone()
            count = count[0]

            cursor.execute('SELECT username FROM users_data;')
            database_usernames = cursor.fetchall()

            username_list = []
            for i in range(count):
                var = database_usernames[i][0]
                if var not in username_list:
                    username_list.append(var)

            cursor.execute(
                "SELECT * FROM users_data WHERE username = '%s'" % username)
            credentials = cursor.fetchall()

            if username not in username_list:
                msgb.showerror('Error in Login', 'No such username exists')

            try:
                username_credentials = credentials[0][0]
                password_credentials = credentials[0][1]

                show_name = f"{credentials[0][2]} {credentials[0][3]}"

            except:
                pass

        except Error as e:
            print(e)
            username_credentials = ''
            password_credentials = ''
            msgb.showwarning('Login Error', 'Please enter a valid username')

        try:

            if username == '':
                msgb.showwarning('Login Error', 'Please enter the username')


            elif password == '':
                msgb.showwarning('Login Error', 'Please enter the password')


            elif username == username_credentials and password != password_credentials:
                msgb.showwarning('Login Error', 'Please enter the correct password')


            elif password == password_credentials and username == username_credentials:
                self.window_login.destroy()

                call_main(username, show_name)

            else:
                pass

        except:
            pass

    @staticmethod
    def about_window():
        """This function opens the about_window"""
        about.About_Window()


def call_main(username, full_name):
    """This function calls the UI of the Main Window"""
    main_window.object.start_ui(username, full_name)

if __name__ == '__main__':
    Login_Window()
