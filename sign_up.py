"""This module manages the UI of the Sign Up window"""

import tkinter as tk
import login
import back_end
import about
from tkinter import messagebox as msgb
import sqlite3 as sq
import hashlib as hl
from sqlite3 import Error


class Sign_Up_Window(object):
    """This class runs the UI of the Sign Up Window"""

    def __init__(self):
        """This __init__ method is to defines the Sign Up Window elements"""
        self.window_sign_up = tk.Tk()
        self.window_sign_up.title('Sign Up')
        self.window_sign_up.geometry('500x450')
        self.window_sign_up.resizable(False, False)
        self.window_sign_up.configure(bg='black')
        self.window_sign_up.iconbitmap('resources/icon.ico')
        self.init_ui()

    def entered_sign(self, event):
        self.sign_up.configure(bg='#a3ffb3')

    def leave_sign(self, event):
        self.sign_up.configure(bg='#f1f5e0')

    def entered_clear_button(self, event):
        self.clear_button.configure(bg='#a3ffb3')

    def leave_clear_button(self, event):
        self.clear_button.configure(bg='#f1f5e0')

    def entered_exit_button(self, event):
        self.exit_button.configure(bg='#a3ffb3')

    def leave_exit_button(self, event):
        self.exit_button.configure(bg='#f1f5e0')

    def entered_login(self, event):
        self.already_user.configure(font=('Maiandra GD', 11, 'underline'))

    def leave_login(self, event):
        self.already_user.configure(font=('Maiandra GD', 11))

    def init_ui(self):
        """This method handles the widgets of the Sign Up Window"""

        self.heading = tk.Label(self.window_sign_up, text='User Registration',
                           font=('arial', 24, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.about_image = tk.PhotoImage(file='resources/about.png')
        self.about_icon = tk.Button(self.window_sign_up, image=self.about_image, bg='black', fg='white', relief='flat',
                               command=self.open_about)
        self.about_icon.place(x=465, y=0)

        self.first_name = tk.Label(self.window_sign_up, text='First Name', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.first_name.place(x=5, y=50)


        self.first_name_var = tk.StringVar()
        self.first_name_entry = tk.Entry(self.window_sign_up, textvariable=self.first_name_var, font=(
                                        'arial', 12), bg='#C0C0C0')
        self.first_name_entry.place(x=100, y=50)
        self.first_name_entry.focus()

        self.last_name = tk.Label(self.window_sign_up, text='Last Name', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.last_name.place(x=5, y=80)


        self.last_name_var = tk.StringVar()
        self.last_name_entry = tk.Entry(self.window_sign_up, textvariable=self.last_name_var, font=(
                                        'arial', 12), bg='#C0C0C0')
        self.last_name_entry.place(x=100, y=80)

        self.username_label = tk.Label(self.window_sign_up, text='Username', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.username_label.place(x=60, y=120)

        self.sign_up_username_entry_var = tk.StringVar()
        self.username_entry = tk.Entry(self.window_sign_up, textvariable=self.sign_up_username_entry_var, font=(
                                        'arial', 12), bg='#C0C0C0')
        self.username_entry.place(x=150, y=120)

        self.password = tk.Label(self.window_sign_up, text='Password', font=(
            'arila', 12, 'bold'), bg='black', fg='white')
        self.password.place(x=60, y=150)

        self.sign_up_password_entry_var = tk.StringVar()
        self.password_entry = tk.Entry(self.window_sign_up, font=(
            'arial', 12), bg='#C0C0C0', textvariable=self.sign_up_password_entry_var, show='*')
        self.password_entry.place(x=150, y=150)

        self.retype_password = tk.Label(self.window_sign_up, text='Retype Password', font=(
            'arial', 12, 'bold'), bg='black', fg='white')

        self.retype_password.place(x=5, y=180)
        self.retype_password_var = tk.StringVar()
        self.retype_password_entry = tk.Entry(self.window_sign_up, textvariable=self.retype_password_var, font=(
                                                'arial', 12), bg='#C0C0C0', show='*')
        self.retype_password_entry.place(x=150, y=180)

        self.note_for_security_question = tk.Label(self.window_sign_up, font=('arial', 10),
                        text="Note: The below security questions are used for recovery if you forget your password",
                        bg='black', fg='orange')
        self.note_for_security_question.place(x=2, y=210)

        self.security_question_1 = tk.Label(self.window_sign_up, text='Question 1', font=(
            'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
        self.security_question_1.place(x=3, y=235)

        self.security_question_1_var = tk.StringVar()
        self.security_question_1_entry = tk.Entry(self.window_sign_up, textvariable=self.security_question_1_var, font=(
                                                'arial', 12), bg='#C0C0C0', width=40)
        self.security_question_1_entry.place(x=100, y=235)

        self.security_answer_1 = tk.Label(self.window_sign_up, text='Answer 1', font=(
            'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
        self.security_answer_1.place(x=14, y=260)

        self.security_answer_1_var = tk.StringVar()
        self.security_answer_1_entry = tk.Entry(self.window_sign_up, textvariable=self.security_answer_1_var, width=20,
                                                font=('arial', 12), bg='#C0C0C0', show="*")
        self.security_answer_1_entry.place(x=100, y=260)

        self.security_question_2 = tk.Label(self.window_sign_up, text='Question 2', font=(
            'arial', 12, 'bold'), bg='black', fg='#98FB98')
        self.security_question_2.place(x=3, y=300)

        self.security_question_2_var = tk.StringVar()
        self.security_question_2_entry = tk.Entry(self.window_sign_up, textvariable=self.security_question_2_var, font=(
            'arial', 12), bg='#C0C0C0', width=40)
        self.security_question_2_entry.place(x=100, y=300)

        self.security_answer_2 = tk.Label(self.window_sign_up, text='Answer 2', font=(
            'arial', 12, 'bold'), bg='black', fg='#98FB98')
        self.security_answer_2.place(x=14, y=325)

        self.security_answer_2_var = tk.StringVar()
        self.security_answer_2_entry = tk.Entry(self.window_sign_up, textvariable=self.security_answer_2_var, width=20,
                                                font=('arial', 12), bg='#C0C0C0', show="*")
        self.security_answer_2_entry.place(x=100, y=325)

        self.sign_up = tk.Button(self.window_sign_up, text='Sign Up', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.save_data)
        self.sign_up.place(x=80, y=380)
        self.sign_up.bind('<Enter>', self.entered_sign)
        self.sign_up.bind('<Leave>', self.leave_sign)

        self.clear_button = tk.Button(self.window_sign_up, text='Clear', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.clear)
        self.clear_button.place(x=210, y=380)
        self.clear_button.bind('<Enter>', self.entered_clear_button)
        self.clear_button.bind('<Leave>', self.leave_clear_button)

        self.exit_button = tk.Button(self.window_sign_up, text='Exit', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.exit)
        self.exit_button.place(x=340, y=380)
        self.exit_button.bind('<Enter>', self.entered_exit_button)
        self.exit_button.bind('<Leave>', self.leave_exit_button)

        self.already_user = tk.Button(self.window_sign_up, text='Already a User! Sign In Here', bg='black', font=(
            'Maiandra GD', 11,), fg='white', relief='flat', command=self.enter_login_page)
        self.already_user.place(x=155, y=420)
        self.already_user.bind('<Enter>', self.entered_login)
        self.already_user.bind('<Leave>', self.leave_login)

        self.window_sign_up.focus_force()

        self.window_sign_up.mainloop()

    def success_sign_up(self):
        """This method shows that sign up was successful and takes to login page"""

        msgb.showinfo('Success Sign Up', "You have signed up successfully")

    def clear(self):
        """ This method clears all the Entries in the Window"""

        self.first_name_var.set('')
        self.last_name_var.set('')
        self.sign_up_username_entry_var.set('')
        self.sign_up_password_entry_var.set('')
        self.retype_password_var.set('')
        self.security_question_1_var.set('')
        self.security_answer_1_var.set('')
        self.security_question_2_var.set('')
        self.security_answer_2_var.set('')
        self.first_name_entry.focus()

    def exit(self):
        """This method closes the Sign Up Window making to exit the Software"""

        self.window_sign_up.destroy()

    def enter_login_page(self):
        """This method destroy's the existing page and takes you to the Login Page"""

        self.window_sign_up.destroy()

        login.Login_Window()

    @staticmethod
    def open_about():
        """This method open the about window"""
        about.About_Window()


    def save_data(self):
        """ This method calls the backend and validates the data and saves it"""
        self.check_p = self.retype_password_var.get()
        self.d1 = self.first_name_var.get()
        self.d2 = self.last_name_var.get()
        self.d3 = self.sign_up_username_entry_var.get()
        self.d4 = self.sign_up_password_entry_var.get()
        self.d5 = self.security_question_1_var.get()
        self.d6 = self.security_answer_1_var.get()
        self.d7 = self.security_question_2_var.get()
        self.d8 = self.security_answer_2_var.get()

        self.username_value = self.check_username_for_signup(self.d3)

        if self.d1 == '':
            msgb.showerror('Error in Sign Up', 'Please Enter your First Name')

        elif self.d2 == '':
            msgb.showerror('Error in Sign Up', 'Please Enter the Last Name')

        elif self.d1 == self.d2:
            msgb.showerror('Error in Sign Up', 'Both First Name and Last Name are Same. Please consider to change')

        elif self.d3 == '':
            msgb.showerror('Error in Sign Up', 'Please Enter the Username')

        elif self.d3 == 'copy':
            msgb.showerror('Error in Sign Up',
                           'Please choose another username the entered username is used for back_end purpose')

        elif self.d3 == self.d1:
            msgb.showerror('Error in Sign Up', 'Your First Name and Username matches please change the username')

        elif self.d3 == self.d2:
            msgb.showerror('Error in Sign Up', 'Your Last Name and Username matches please change the username')

        elif not self.username_value:
            msgb.showerror('Error in Sign Up', 'The username already exists, Please Change')

        elif self.d4 == '':
            msgb.showerror('Error in Sign Up', 'Please Enter the Password')

        elif self.d4.isalpha():
            msgb.showerror('Error in Sign Up', 'Your Password only contains Alphabets try including some numbers')

        elif self.d4.isdigit():
            msgb.showerror('Error in Sign Up', 'Your Password only contains number try including some alphabets')

        elif self.d4 != self.check_p:
            msgb.showerror('Error in Sign Up', 'Your Passwords do not match please check again')

        elif self.d5 == '':
            msgb.showerror('Error in Sign Up', 'Please fill the security question 1')

        elif self.d6 == '':
            msgb.showerror('Error in Sign Up', 'Please fill the security answer 1')

        elif self.d7 == '':
            msgb.showerror('Error in Sign Up', 'Please fill the security question 2')

        elif self.d8 == '':
            msgb.showerror('Error in Sign Up', 'Please fill the security answer 2')

        elif self.d5 == self.d7:
            msgb.showerror('Error in Sign Up', 'The security questions match please change them')

        elif self.d6 == self.d8:
            msgb.showerror('Error in Sign Up', 'The security answers match please change them')

        else:
            self.insert_data(self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8)

    @staticmethod
    def check_username_for_signup(username):
        """This function checks whether given username exists or not"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()

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

        conn.commit()
        conn.close()

        if username not in username_list:
            return True

        else:
            return False


    def insert_data(self, f_name, l_name, username, password, q_1, a_1, q_2, a_2):
        """This functions Signs Up the user for the use of the program"""
        f_name = f_name.capitalize()
        l_name = l_name.capitalize()

        if q_1[-1] != '?':
            q_1 = q_1 + '?'

        if q_2[-1] != '?':
            q_2 = q_2 + '?'
        try:
            conn = sq.connect('database.db')
            cursor = conn.cursor()

            my_string = hl.sha256(password.encode('utf-8'))
            hash_password = my_string.hexdigest()

            string_1 = hl.sha256(a_1.encode('utf-8'))
            answer_1 = string_1.hexdigest()

            string_2 = hl.sha256(a_2.encode('utf-8'))
            answer_2 = string_2.hexdigest()

            sql = ("""INSERT INTO users_data 
                        (username, password, first_name, last_name, question_1, answer_1, question_2, answer_2)
                        VALUES (?,?,?,?,?,?,?,?)""")
            data = (username, hash_password, f_name, l_name, q_1, answer_1, q_2, answer_2)
            cursor.execute(sql, data)

            sql_1 = f"CREATE TABLE {username}_password (val_no text, fe_name text, username text, password text, ref_1 text, ref_2 text)"
            cursor.execute(sql_1)

            sql_2 = f"CREATE TABLE {username}_payment (val_no text, fe_name text, card_number integer, name_on_card text, expiry_date text, username text , password text)"
            cursor.execute(sql_2)

            sql_3 = f"CREATE TABLE {username}_address (val_no text, fe_name text, line_1 text, line_2 text, city text, district text, state text ,pin_code integer)"
            cursor.execute(sql_3)

            copy_1 = f"INSERT INTO {username}_password SELECT * FROM copy_password"
            cursor.execute(copy_1)

            copy_2 = f"INSERT INTO {username}_payment SELECT * FROM copy_payment"
            cursor.execute(copy_2)

            copy_3 = f"INSERT INTO {username}_address SELECT * FROM copy_address"
            cursor.execute(copy_3)

            conn.commit()
            conn.close()

            msgb.showinfo('Success Sign Up', 'You have successfully Signed Up')
            self.enter_login_page()

        except Error as e:
            print(e)
