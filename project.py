import tkinter as tk
from tkinter import messagebox as msgb
import sqlite3 as sq
from sqlite3 import Error
import pyperclip as pc
import hashlib as hl
import webbrowser as wb



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
        Sign_Up_Window()

    def open_forgot_password_window(self):
        """Takes the user to the forgot Password Window"""
        self.window_login.destroy()
        Forgot_Password()

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

                global root
                root = Main_Window(username, show_name)

            else:
                pass

        except:
            pass

    @staticmethod
    def about_window():
        """This function opens the about_window"""
        About_Window()


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

        Login_Window()

    @staticmethod
    def open_about():
        """This method open the about window"""
        About_Window()


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


class Forgot_Password(object):
    """This class runs the UI of the Forgot Password Window"""

    def __init__(self):
        self.window_forgot = tk.Tk()
        self.window_forgot.title('Forgot Password')
        self.window_forgot.resizable(False, False)
        self.window_forgot.configure(bg='black')
        self.window_forgot.geometry('600x500')
        self.window_forgot.iconbitmap('resources/icon.ico')
        self.init_ui()

    def entered_get_question(self, event):
        self.get_question.configure(bg='gold')

    def leave_get_question(self, event):
        self.get_question.configure(bg='light blue')

    def entered_clear_usr(self, event):
        self.clear_username.configure(bg='gold')

    def leave_clear_usr(self, event):
        self.clear_username.configure(bg='light blue')

    def entered_change(self, event):
        self.change_password.configure(bg='#a3ffb3')

    def leave_change(self, event):
        self.change_password.configure(bg='#f1f5e0')

    def entered_clear_answers(self, event):
        self.clear_answers.configure(bg='#a3ffb3')

    def leave_clear_answers(self, event):
        self.clear_answers.configure(bg='#f1f5e0')

    def entered_cancel_changes(self, event):
        self.cancel_changes.configure(bg='#a3ffb3')

    def leave_cancel_changes(self, event):
        self.cancel_changes.configure(bg='#f1f5e0')

    def init_ui(self):
        self.heading = tk.Label(self.window_forgot, text='Forgot Password', font=(
            'arial', 18, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.about_image = tk.PhotoImage(file='resources/about.png')
        self.about_icon = tk.Button(self.window_forgot, image=self.about_image, bg='black', fg='white', relief='flat',
                               command=self.open_about)
        self.about_icon.place(x=565, y=0)

        self.pic = tk.PhotoImage(file='resources/back.png')
        self.dis = tk.Button(self.window_forgot, image=self.pic, bg='black', command=self.back, relief='flat')
        self.dis.place(x=0, y=0)

        self.happy_img = tk.PhotoImage(file="resources/happy.png")
        self.happy = tk.Label(self.window_forgot, text="Don't worry we are here to recover you account ",
                              image=self.happy_img, compound='right',bg='black', fg='white', font=('Maiandra GD', 14))
        self.happy.place(x=70, y=40)

        self.username_label = tk.Label(self.window_forgot, text='Username', font=(
            'timesnewroman', 12), bg='black', fg='white')
        self.username_label.place(x=60, y=90)

        self.username_entry_var = tk.StringVar()
        self.username_entry = tk.Entry(self.window_forgot, font=('arial', 12),
                                  bg='#C0C0C0', textvariable=self.username_entry_var)
        self.username_entry.place(x=140, y=90)
        self.username_entry.focus()

        self.get_question = tk.Button(self.window_forgot, text='Get Questions', bg='light blue', relief='groove',
                                 font=('Maiandra GD', 12, 'bold'), width=12, command=self.show_question)
        self.get_question.place(x=160, y=130)
        self.get_question.bind('<Enter>', self.entered_get_question)
        self.get_question.bind('<Leave>', self.leave_get_question)

        self.clear_username = tk.Button(self.window_forgot, text='Clear', bg='light blue', relief='groove',
                                   font=('Maiandra GD', 12, 'bold'), width=8, command=self.clear_username_entry)
        self.clear_username.place(x=320, y=130)
        self.clear_username.bind('<Enter>', self.entered_clear_usr)
        self.clear_username.bind('<Leave>', self.leave_clear_usr)

        self.window_forgot.focus_force()
        self.window_forgot.mainloop()

    def show_question(self):

        self.given_username = self.username_entry_var.get()

        self.auth = self.check_username()



        if self.auth:

            self.username_entry.configure(state = 'disabled')
            self.get_question.destroy()
            self.clear_username.destroy()

            self.sq_1, self.sq_2 = self.get_question(self.given_username)

            self.security_question_1 = tk.Label(self.window_forgot, text='Security Question 1', font=(
                'arial', 12, 'bold'), fg='#FFB6C1', bg='black')
            self.security_question_1.place(x=3, y=180)

            self.security_question_1_text = tk.Text(self.window_forgot, height=1, width=48, font=(
                'georgia', 10), relief='flat', bg='white')
            self.security_question_1_text.place(x=160, y=180)
            self.question_1 = f"{self.sq_1}"
            self.security_question_1_text.insert(tk.END, self.question_1)
            self.security_question_1_text.configure(state='disabled')

            self.security_answer_1 = tk.Label(self.window_forgot, text='Answer 1', font=(
                'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
            self.security_answer_1.place(x=80, y=210)

            self.security_answer_1_var = tk.StringVar()
            self.security_answer_1_entry = tk.Entry(self.window_forgot, textvariable=self.security_answer_1_var,
                                                    width=20, font=('arial', 12), bg='#C0C0C0')
            self.security_answer_1_entry.place(x=160, y=210)
            self.security_answer_1_entry.focus()

            self.security_question_2 = tk.Label(self.window_forgot, text='Security Question 2', font=(
                                                'arial', 12, 'bold'), bg='black', fg='#98FB98')
            self.security_question_2.place(x=3, y=260)

            self.security_question_2_text = tk.Text(self.window_forgot, height=1, width=48, font=(
                                                    'georgia', 10), relief='flat', bg='white')
            self.security_question_2_text.place(x=160, y=260)
            self.question_2 = f"{self.sq_2}"
            self.security_question_2_text.insert(tk.END, self.question_2)
            self.security_question_2_text.configure(state='disabled')

            self.security_answer_2 = tk.Label(self.window_forgot, text='Answer 2', font=(
                'arial', 12, 'bold'), bg='black', fg='#98FB98')
            self.security_answer_2.place(x=80, y=290)

            self.security_answer_2_var = tk.StringVar()
            self.security_answer_2_entry = tk.Entry(self.window_forgot, textvariable=self.security_answer_2_var,
                                                    width=20, font=('arial', 12), bg='#C0C0C0')
            self.security_answer_2_entry.place(x=160, y=290)

            self.change_password = tk.Button(self.window_forgot, text='Change Password', font=(
                'consolas', 13, 'bold'), relief='groove', width=16, bg='#f1f5e0', command=self.change_pass)
            self.change_password.place(x=60, y=340)
            self.change_password.bind('<Enter>', self.entered_change)
            self.change_password.bind('<Leave>', self.leave_change)

            self.clear_answers = tk.Button(self.window_forgot, text='Clear', font=(
                'consolas', 13, 'bold'), relief='groove', width=10, bg='#f1f5e0', command=self.clear_the_answers)
            self.clear_answers.place(x=250, y=340)
            self.clear_answers.bind('<Enter>', self.entered_clear_answers)
            self.clear_answers.bind('<Leave>', self.leave_clear_answers)

            self.cancel_changes = tk.Button(self.window_forgot, text='Cancel', font=(
                'consolas', 13, 'bold'), relief='groove', width=10, bg='#f1f5e0', command=self.cancel_the_changes)
            self.cancel_changes.place(x=390, y=340)
            self.cancel_changes.bind('<Enter>', self.entered_cancel_changes)
            self.cancel_changes.bind('<Leave>', self.leave_cancel_changes)

        else:
            msgb.showerror('Error in Username Check', 'The entered Username does not exists please try again')

    @staticmethod
    def get_question(got_username):
        """This function returns the security questions of the user as output"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()

        sql = f"SELECT question_1, question_2 FROM users_data WHERE username = '{got_username}'"

        running = cursor.execute(sql)
        values = running.fetchone()

        question_1 = values[0]
        question_2 = values[1]

        conn.commit()
        conn.close()

        return question_1, question_2

    def check_username(self):
        """This function checks whether given username exists or not"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT COUNT(username) FROM users_data")
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

        if self.given_username not in username_list:
            return False

        else:
            return True

    def change_pass(self):
        """This function destroys the widgets in the window to show password widgets"""

        answer_1 = self.security_answer_1_var.get()
        answer_2 = self.security_answer_2_var.get()
        usr = self.given_username

        if answer_1 == '' and answer_2 == '':
            msgb.showerror('Error in Authentication','Please fill the Answers for recovery of your account')
            self.check_for_answer = False

        elif answer_1 == '':
            msgb.showerror('Error in Authentication','You have not entered the Answer 1. Please fill it.')
            self.check_for_answer = False

        elif answer_2 == '':
            msgb.showerror('Error in Authentication','You have not entered the Answer 2. Please fill it.')
            self.check_for_answer = False

        else:
            self.check_for_answer = self.check_answers(usr, answer_1, answer_2)

        if self.check_for_answer:

            self.security_question_1.destroy()
            self.security_question_1_text.destroy()
            self.security_answer_1.destroy()
            self.security_answer_1_entry.destroy()
            self.security_question_2.destroy()
            self.security_question_2_text.destroy()
            self.security_answer_2.destroy()
            self.security_answer_2_entry.destroy()
            self.change_password.destroy()
            self.get_question.destroy()
            self.clear_username.destroy()
            self.clear_answers.destroy()
            self.cancel_changes.destroy()
            self.username_entry.configure(state='disabled')

            self.enter_changes(usr)

        else:
            pass

    @staticmethod
    def check_answers(user_address, ans_1, ans_2):
        """This function returns True if the answers given are matched with the database"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()

        val_1 = hl.sha256(ans_1.encode('UTF-8'))
        got_ans_1 = val_1.hexdigest()

        val_2 = hl.sha256(ans_2.encode('UTF-8'))
        got_ans_2 = val_2.hexdigest()

        try:
            sql = f"SELECT answer_1, answer_2 FROM users_data WHERE username = '{user_address}'"
            value = cursor.execute(sql)
            data = value.fetchone()

            sql_ans_1 = data[0]
            sql_ans_2 = data[1]

            if sql_ans_1 != got_ans_1 and sql_ans_2 != got_ans_2:
                msgb.showerror('Error in Access', 'You both the answers are wrong. Please Enter again')
                return False

            elif sql_ans_1 != got_ans_1 and sql_ans_2 == got_ans_2:
                msgb.showerror('Error in Access', 'You answer for question 1 is incorrect please try again')
                return False

            elif sql_ans_1 == got_ans_1 and sql_ans_2 != got_ans_2:
                msgb.showerror('Error in Access', 'Your answer for question 2 is incorrect please try again')
                return False

            elif sql_ans_1 == got_ans_1 and sql_ans_2 == got_ans_2:
                msgb.showinfo('Access Granted', 'You have got the permission to change the password')
                return True

            else:
                return False

        except Error as e:
            print(e)

        conn.commit()
        conn.close()

    def enter_changes(self, username):
        """This function manages the UI of the password entry and gets the new password data """

        self.enter_new_password = tk.Label(self.window_forgot, text = 'Enter New Password',font=(
                                            'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
        self.enter_new_password.place(x=5, y=210)

        self.enter_new_password_entry_var = tk.StringVar()
        self.enter_new_password_entry = tk.Entry(self.window_forgot, textvariable=self.enter_new_password_entry_var,
                                                 width=20, font=('arial', 12), bg='#C0C0C0')
        self.enter_new_password_entry.place(x=170, y=210)

        self.retype_password = tk.Label(self.window_forgot, text='Retype Password', font=(
            'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
        self.retype_password.place(x=30, y=240)

        self.retype_password_entry_var = tk.StringVar()
        self.retype_password_entry = tk.Entry(self.window_forgot, textvariable=self.retype_password_entry_var,
                                              width=20, font=('arial', 12), bg='#C0C0C0')
        self.retype_password_entry.place(x=170, y=240)

        self.change_password = tk.Button(self.window_forgot, text = 'Change Password',relief='groove',width=15,font=(
                    'consolas', 13, 'bold'), bg='#f1f5e0', command=lambda: self.change_the_password(username))
        self.change_password.place(x=130, y=280)

        self.clear_password = tk.Button(self.window_forgot, text = 'Clear',relief='groove',width=8,font=(
                                        'consolas', 13, 'bold'), bg='#f1f5e0', command=self.password_clear)
        self.clear_password.place(x=300, y=280)

    @staticmethod
    def open_about():
        """This method opens the About Window"""
        About_Window()

    def back(self):
        """This method closes the forgot_password window and redirects to login window"""
        self.window_forgot.destroy()

        Login_Window()

    def clear_the_answers(self):
        self.security_answer_1_var.set('')
        self.security_answer_2_var.set('')
        self.security_answer_1_entry.focus()

    def cancel_the_changes(self):
        self.security_question_1.destroy()
        self.security_question_1_text.destroy()
        self.security_answer_1.destroy()
        self.security_answer_1_entry.destroy()
        self.security_question_2.destroy()
        self.security_question_2_text.destroy()
        self.security_answer_2.destroy()
        self.security_answer_2_entry.destroy()
        self.change_password.destroy()
        self.get_question.destroy()
        self.clear_username.destroy()
        self.clear_answers.destroy()
        self.cancel_changes.destroy()
        self.init_ui()

    def clear_username_entry(self):
        """This function clears the data in the entry box of the username"""
        self.username_entry_var.set('')

    def password_clear(self):
        """This function clears the data in the passwords entry boxes"""
        self.enter_new_password_entry_var.set('')
        self.retype_password_entry_var.set('')

    def change_the_password(self, username):
        """This function passes the data to update the password"""
        pass_1 = self.enter_new_password_entry_var.get()
        pass_2 = self.retype_password_entry_var.get()

        if pass_1 == pass_2:
            self.update_password(username, pass_1)
            self.window_forgot.destroy()
            Login_Window()


        else:
            pass

    @staticmethod
    def update_password(username, password):
        """This function updates the user password after recovery"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()

        value = hl.sha256(password.encode('UTF-8'))
        enc_password = value.hexdigest()

        sql = f"UPDATE users_data SET password = '{enc_password}' WHERE username = '{username}'"
        try:
            cursor.execute(sql)
            msgb.showinfo('Success', 'You have successfully changed your password please login')


        except Error as e:
            print(e)

        conn.commit()
        conn.close()


class About_Window(object):
    """This class runs the UI of the About Window"""

    def __init__(self):
        """This __init__ method is to defines the About Window elements"""
        self.window_about = tk.Toplevel()
        self.window_about.title('About')
        self.window_about.geometry('600x300')
        self.window_about.configure(bg='black')
        self.window_about.resizable(False, False)
        self.window_about.iconbitmap('resources/icon.ico')
        self.init_ui()

    def init_ui(self):
        """This method adds the widgets to the About Window"""

        self.heading = tk.Label(self.window_about, text='About Me', font=(
            'georgia', 24, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.my_img = tk.PhotoImage(file='resources/my_image.png')
        self.my_label = tk.Label(self.window_about, image=self.my_img, bg='black')
        self.my_label.place(x=5, y=50)

        self.my_text = tk.Text(self.window_about, bg='black', fg='white', font=('georgia', 11), height=10, width=50,
                          relief='flat')
        self.my_text.place(x=190, y=50)
        self.text = '''Hello Everyone!
        I am Pranav and I have developed this Project - Password
        Manager. Hope you like it and enjoy using it in your
        daily life and make your life comfortable. If you want to
        give me any suggestions you can contact me from the given
        mail below. If you want to see more of my work please visit
        my blog.That's it keep going...'''
        self.my_text.insert(tk.END, self.text)

        self.email = tk.Label(self.window_about, text='Email:', bg='black', fg='light green', font=('arial', 10))
        self.email.place(x=200, y=190)

        self.email_info = tk.Text(self.window_about, bg='black', font=('times new roman', 12, 'underline'), fg='light blue',
                             relief='flat', height=3, width=25)
        self.email_info.place(x=240, y=187)
        self.email_info.insert(tk.END, 'pranav.techiegeek@gmail.com')

        self.view_blog = tk.Button(self.window_about, text='View My Blog', bg='light blue', relief='groove',
                              font=('georgia', 12, 'bold'), command=self.redirect)
        self.view_blog.place(x=360, y=250)
        self.view_blog.bind("<Enter>", self.entered_blog)
        self.view_blog.bind("<Leave>", self.leave_blog)

        self.exit_button = tk.Button(self.window_about, text='Exit', bg='light blue', relief='groove',
                                font=('georgia', 12, 'bold'), width=6, command=self.exit_window)
        self.exit_button.place(x=490, y=250)
        self.exit_button.bind("<Enter>", self.entered_exit)
        self.exit_button.bind("<Leave>", self.leave_exit)

        self.window_about.focus_force()
        self.window_about.mainloop()

    def entered_blog(self, event):
        self.view_blog.configure(bg = 'pink')

    def leave_blog(self, event):
        self.view_blog.configure(bg = 'light blue')

    def entered_exit(self, event):
        self.exit_button.configure(bg = 'pink')

    def leave_exit(self, event):
        self.exit_button.configure(bg = 'light blue')

    @staticmethod
    def redirect():
        """This method redirects to my blog"""
        wb.open('https://appsbypranav.blogspot.com')


    def exit_window(self):
        """This method closes the About window"""
        self.window_about.destroy()


class Main_Window(object):
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

        self.change_the_address_box_name()

        self.delete_account = tk.Button(self.window_main, text='Delete Your Account', bg='red', fg='white', font=(
                                        'arial', 10, 'bold'), command=self.open_delete_window)
        self.delete_account.place(x=955, y=570)

        self.window_main.focus_force()
        self.window_main.mainloop()


    def change_the_address_box_name(self):
        """This method changes the button name after updating the feature name"""

        conn = sq.connect('database.db')
        cursor = conn.cursor()

        sql = f"SELECT fe_name from {self.username}_address"
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
        Login_Window()

    def show_password(self,button):
        """This method shows the data in the password_edit module"""
        fe_name,win_username,win_password,reference_1,reference_2 = self.get_password_button_data(button)

        Password_Window(self.username,button,fe_name,win_username,win_password,reference_1,reference_2)

    def show_address(self, button):
        """This method shows the data in the address_edit module"""
        fe_name, address_1, address_2, town, district, state, pin = self.get_address_button_data(button)

        Address_Window(self.username,self.full_name,button,fe_name,address_1,address_2,town,district,state,pin)

    def show_payment(self, button):
        """This method shows the data in the payment_edit module"""
        fe_name,card_num,name_on_card,expiry,pay_username,pay_password = self.get_payment_button_data(button)

        Payment_Window(self.username,button,fe_name,card_num,name_on_card,expiry,pay_username,pay_password)

    def open_delete_window(self):
        """This will open the delete user window"""
        self.window_main.destroy()
        Delete_Window(self.username)

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
        About_Window()



class Delete_Window(object):
    """This class runs the UI of the Delete Window"""

    def __init__(self, username):
        """This __init__ method is to defines the Login Window elements"""
        self.username = username
        self.window_delete = tk.Tk()
        self.window_delete.title("Delete users's Account")
        self.window_delete.resizable(False, False)
        self.window_delete.geometry('460x290')
        self.window_delete.configure(bg='black')
        self.window_delete.iconbitmap('resources/icon.ico')
        self.init_ui()

    def entered_delete_button(self, event):
        self.delete_button.configure(bg = 'light green', fg = 'red')

    def leave_delete_button(self, event):
        self.delete_button.configure(bg = 'red', fg = 'light green')

    def entered_clear_button(self, event):
        self.clear_button.configure(bg='#a3ffb3')

    def leave_clear_button(self, event):
        self.clear_button.configure(bg='#f1f5e0')

    def entered_exit_button(self, event):
        self.exit_button.configure(bg='#a3ffb3')

    def leave_exit_button(self, event):
        self.exit_button.configure(bg='#f1f5e0')

    def init_ui(self):
        """This method adds the widgets to the Delete Window"""

        self.heading = tk.Label(self.window_delete, text='Delete Your Account',
                           font=('arial', 20, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.background = tk.PhotoImage(file='resources/line.png')
        self.background_image = tk.Label(self.window_delete, image=self.background,
                                    bg='black')
        self.background_image.place(x=5, y=180)

        self.about_image = tk.PhotoImage(file='resources/about.png')
        self.about_icon = tk.Button(self.window_delete, image=self.about_image, bg='black', fg='white', relief='flat',
                               command=self.open_about)
        self.about_icon.place(x=425, y=0)

        self.sorry_img = tk.PhotoImage(file="resources/sorry.png")
        self.sorry = tk.Label(self.window_delete, text='  We are sorry to see you go', image=self.sorry_img, compound='left',
                         bg='black', fg='white', font=('Maiandra GD', 14))
        self.sorry.place(x=100, y=40)

        self.note = tk.Label(self.window_delete, font=('arial', 12),
                        text="Note: You cannot recover your account once deleted",
                        bg='black', fg='orange')
        self.note.place(x=2, y=100)

        self.password = tk.Label(self.window_delete, text='Password', font=(
            'timesnewroman', 12), bg='black', fg='white')
        self.password.place(x=62, y=140)


        self.password_entry_var = tk.StringVar()
        self.password_entry = tk.Entry(self.window_delete, font=('arial', 12), show='*',
                                  bg='#C0C0C0', textvariable=self.password_entry_var)
        self.password_entry.place(x=140, y=140)
        self.password_entry.focus()

        self.retype_password = tk.Label(self.window_delete, text='Retype Password', font=(
            'timesnewroman', 12), bg='black', fg='white')
        self.retype_password.place(x=10, y=170)


        self.retype_password_entry_var = tk.StringVar()
        self.retype_password_entry = tk.Entry(self.window_delete, font=('arial', 12), show='*',
                                         bg='#C0C0C0', textvariable=self.retype_password_entry_var)
        self.retype_password_entry.place(x=140, y=170)

        self.delete_button = tk.Button(self.window_delete, text='Delete your Account', font=(
            'consolas', 13, 'bold'), relief='groove', width=20, bg='red', fg='light green',
                                  command=lambda: self.delete_user(self.username))
        self.delete_button.place(x=20, y=240)
        self.delete_button.bind('<Enter>', self.entered_delete_button)
        self.delete_button.bind('<Leave>', self.leave_delete_button)

        self.clear_button = tk.Button(self.window_delete, text='Clear', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.clear)
        self.clear_button.place(x=240, y=240)
        self.clear_button.bind('<Enter>', self.entered_clear_button)
        self.clear_button.bind('<Leave>', self.leave_clear_button)

        self.exit_button = tk.Button(self.window_delete, text='Exit', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.exit_window)
        self.exit_button.place(x=350, y=240)
        self.exit_button.bind('<Enter>', self.entered_exit_button)
        self.exit_button.bind('<Leave>', self.leave_exit_button)

        self.window_delete.focus_force()
        self.window_delete.mainloop()


    def clear(self):
        """This method is called when clear button is pressed
    and it clears the inputs in the window"""
        self.password_entry_var.set('')
        self.retype_password_entry_var.set('')
        self.password_entry.focus()

    def delete_user(self, filled_username):
        """This function executes when delete account button is pressed
    It takes back to the back_end and evaluates password and delete your account
    if the password entered is matched"""
        pw1 = self.password_entry_var.get()
        pw2 = self.retype_password_entry_var.get()
        self.delete_account(filled_username, pw1, pw2)

    def exit_window(self):
        """This window is called when exit button is pressed and
    closes the window and exiting the application"""
        self.window_delete.destroy()


    def delete_account(self, usr, pw1, pw2):
        """This method checks whether the given passwords in the delete window are Correct
    and if evaluated True the account and its tables are deleted"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()
        cred = None
        try:
            sql = f"SELECT password FROM users_data WHERE username = '{usr}'"
            out = cursor.execute(sql)
            cred = out.fetchone()
            cred = cred[0]


        except Error as e:
            print(e)

        if pw1 == pw2:

            val = hl.sha256(pw1.encode('UTF-8'))
            password = val.hexdigest()

            if password == cred:
                try:
                    sequel = f"DELETE FROM users_data where username = '{usr}'"
                    cursor.execute(sequel)

                    sequel_1 = f"DROP TABLE {usr}_password"
                    cursor.execute(sequel_1)

                    sequel_2 = f"DROP TABLE {usr}_address"
                    cursor.execute(sequel_2)

                    sequel_3 = f"DROP TABLE {usr}_payment"
                    cursor.execute(sequel_3)

                    msgb.showinfo('Success', 'You have successfully deleted you account we are sorry to see you go')

                    self.window_delete.destroy()
                    Login_Window()
                except Error as e:
                    print(e)

            else:
                msgb.showerror('Error while deleting Account', 'The password is incorrect. Try Again')

        else:
            msgb.showerror('Error while deleting Account', 'The passwords entered do not match please re-enter')

        conn.commit()
        conn.close()

    @staticmethod
    def open_about():
        About_Window()


class Password_Window(Main_Window):
    """This class runs the UI of the Password Edit Window"""

    def __init__(self,username, button_name,fe_name,pass_username,pass_password, ref_1, ref_2):
        """This __init__ method defines the Window Elements"""
        self.username = username
        self.button_name = button_name
        self.fe_name = fe_name
        self.pass_username = pass_username
        self.pass_password = pass_password
        self.ref_1 = ref_1
        self.ref_2 = ref_2
        self.window_edit_password = tk.Toplevel()
        self.window_edit_password.title('Store your passwords')
        self.window_edit_password.geometry('475x300')
        self.window_edit_password.resizable(False, False)
        self.window_edit_password.configure(bg='black')
        self.window_edit_password.iconbitmap('resources/icon.ico')
        self.password_ui()

    def entered_storage_save_button(self, event):
        self.save_button.configure(bg='#a3ffb3')

    def leave_storage_save_button(self, event):
        self.save_button.configure(bg='#f1f5e0')

    def entered_storage_clear_button(self, event):
        self.clear_button.configure(bg='#a3ffb3')

    def leave_storage_clear_button(self, event):
        self.clear_button.configure(bg='#f1f5e0')

    def entered_storage_exit_button(self, event):
        self.exit_button.configure(bg='#a3ffb3')

    def leave_storage_exit_button(self, event):
        self.exit_button.configure(bg='#f1f5e0')

    def password_ui(self):
        """This method adds widgets to the Window"""

        self.background = tk.PhotoImage(file='resources/line.png')
        self.background_image = tk.Label(self.window_edit_password, image=self.background,bg='black')
        self.background_image.place(x=5, y=190)

        self.heading = tk.Label(self.window_edit_password, text='Store your Passwords Safely',
                           font=('arial', 20, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.about_image = tk.PhotoImage(file='resources/about.png')
        self.about_icon = tk.Button(self.window_edit_password, image=self.about_image, bg='black', fg='white', relief='flat',
                               command=self.open_about)
        self.about_icon.place(x=440, y=0)

        self.feature_name = tk.Label(self.window_edit_password, text='Feature Name', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.feature_name.place(x=10, y=50)

        self.feature_name_entry_var = tk.StringVar()
        self.feature_name_entry = tk.Entry(self.window_edit_password, textvariable=self.feature_name_entry_var, font=(
                                            'arial', 12), bg='#C0C0C0', width=20)
        self.feature_name_entry.place(x=130, y=50)
        self.feature_name_entry_var.set(self.fe_name)

        self.note_for_feature_name = tk.Label(self.window_edit_password,
                                         text='Note: Feature name is displayed on the button in the Main window', font=(
                                         'arial', 10), bg='black', fg='orange')
        self.note_for_feature_name.place(x=2, y=75)

        self.save_username = tk.Label(self.window_edit_password, text='Username', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.save_username.place(x=40, y=100)

        self.save_username_entry_var = tk.StringVar()
        self.save_username_entry = tk.Entry(self.window_edit_password, textvariable=self.save_username_entry_var, font=(
                                            'arial', 12), bg='#C0C0C0', width=20)
        self.save_username_entry.place(x=130, y=100)
        self.save_username_entry_var.set(self.pass_username)
        self.data_user = self.save_username_entry_var.get()

        self.copy_image = tk.PhotoImage(file='resources/copy.png')
        self.copy_user = tk.Button(self.window_edit_password, image=self.copy_image, relief='groove',
                              command=lambda: self.copy_data(self.data_user))
        self.copy_user.place(x=320, y=100)

        self.save_password = tk.Label(self.window_edit_password, text='Password', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.save_password.place(x=40, y=130)

        self.save_password_entry_var = tk.StringVar()
        self.save_password_entry = tk.Entry(self.window_edit_password, textvariable=self.save_password_entry_var, font=(
            'arial', 12), bg='#C0C0C0', width=20, show="*")
        self.save_password_entry.place(x=130, y=130)
        self.save_password_entry_var.set(self.pass_password)
        self.data_password = self.save_password_entry_var.get()

        self.copy_password = tk.Button(self.window_edit_password, image=self.copy_image, relief='groove',
                                  command=lambda: self.copy_data(self.data_password))
        self.copy_password.place(x=320, y=130)

        self.ref_1_label = tk.Label(self.window_edit_password, text='Reference - 1', font=(
                                    'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
        self.ref_1_label.place(x=20, y=160)

        self.ref_1_entry_var = tk.StringVar()
        self.ref_1_entry = tk.Entry(self.window_edit_password, textvariable=self.ref_1_entry_var, font=(
                                    'arial', 12), bg='#C0C0C0', width=20)
        self.ref_1_entry.place(x=130, y=160)
        self.ref_1_entry_var.set(self.ref_1)
        self.data_ref_1 = self.ref_1_entry_var.get()

        self.copy_ref_1 = tk.Button(self.window_edit_password, image=self.copy_image, relief='groove',
                                    command=lambda: self.copy_data(self.data_ref_1))
        self.copy_ref_1.place(x=320, y=160)

        self.ref_2_label = tk.Label(self.window_edit_password, text='Reference - 2', font=(
                                    'arial', 12, 'bold'), bg='black', fg='#61f2ff')
        self.ref_2_label.place(x=20, y=190)

        self.ref_2_entry_var = tk.StringVar()
        self.ref_2_entry = tk.Entry(self.window_edit_password, textvariable=self.ref_2_entry_var, font=(
            'arial', 12), bg='#C0C0C0', width=20)
        self.ref_2_entry.place(x=130, y=190)
        self.ref_2_entry_var.set(self.ref_2)
        self.data_ref_2 = self.ref_2_entry_var.get()

        self.copy_ref_2 = tk.Button(self.window_edit_password, image=self.copy_image, relief='groove',
                                    command=lambda: self.copy_data(self.data_ref_2))
        self.copy_ref_2.place(x=320, y=190)

        self.save_button = tk.Button(self.window_edit_password, text='Save', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0',
                                command=lambda: self.get_data)
        self.save_button.place(x=30, y=250)
        self.save_button.bind('<Enter>', self.entered_storage_save_button)
        self.save_button.bind('<Leave>', self.leave_storage_save_button)

        self.clear_button = tk.Button(self.window_edit_password, text='Clear', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.clear)
        self.clear_button.place(x=180, y=250)
        self.clear_button.bind('<Enter>', self.entered_storage_clear_button)
        self.clear_button.bind('<Leave>', self.leave_storage_clear_button)

        self.exit_button = tk.Button(self.window_edit_password, text='Exit', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.exit)
        self.exit_button.place(x=330, y=250)
        self.exit_button.bind('<Enter>', self.entered_storage_exit_button)
        self.exit_button.bind('<Leave>', self.leave_storage_exit_button)

        self.window_edit_password.mainloop()

    def clear(self):
        """It clears all the entries in the function"""
        self.feature_name_entry_var.set('empty')
        self.save_username_entry_var.set('')
        self.save_password_entry_var.set('')
        self.ref_1_entry_var.set('')
        self.ref_2_entry_var.set('')
        self.feature_name_entry.focus()

    def exit(self):
        """It closes the window and exiting the program"""
        self.window_edit_password.destroy()

    def get_data(self):
        """This function get's the data from the entry to save in the database"""
        fe_name = self.feature_name_entry_var.get()
        pass_username = self.save_username_entry_var.get()
        pass_password = self.save_password_entry_var.get()
        ref_1 = self.ref_1_entry_var.get()
        ref_2 = self.ref_2_entry_var.get()
        print(fe_name)

        self.update_password_data(fe_name, pass_username, pass_password, ref_1,ref_2)

    def update_password_data(self, fe_name, pass_username, pass_password, ref_1, ref_2):
        """This function updates the data to the database"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()

        update = f"""UPDATE {self.username}_password set fe_name = "{fe_name}",     
                username = "{pass_username}",
                password = "{pass_password}" ,
                ref_1 = "{ref_1}",
                ref_2 = "{ref_2}"
                WHERE val_no = "{self.button_name}" """
        cursor.execute(update)

        msgb.showinfo('Success', 'You have successfully update the data')

        conn.commit()
        conn.close()

        self.change_the_password_box_name()

        self.window_edit_password.destroy()

    @staticmethod
    def open_about():
        """This method opens the About Window"""
        About_Window()

    @staticmethod
    def copy_data(text):
        """This method copies the data in the entry box to the clipboard"""
        pc.copy(text)


class Payment_Window(Main_Window):

    def __init__(self,username, button_name,fe_name, card_number, name_on_card, expiry_date,
                 pay_username, pay_password):
        self.username = username
        self.button_name = button_name
        self.fe_name = fe_name
        self.card_number = card_number
        self.name_on_card = name_on_card
        self.expiry_date = expiry_date
        self.pay_username = pay_username
        self.pay_password = pay_password

        if (self.card_number is None and self.name_on_card is None and self.expiry_date is None and self.pay_username
            is None and self.pay_password is None) and self.fe_name == 'empty':
            self.fe_name = 'empty'
            self.card_number = ''
            self.name_on_card = ''
            self.expiry_date = ''
            self.pay_username = ''
            self.pay_password = ''

        else:
            pass

        self.window_edit_payment = tk.Toplevel()
        self.window_edit_payment.title('Store your Payment Information')
        self.window_edit_payment.geometry('475x350')
        self.window_edit_payment.resizable(False, False)
        self.window_edit_payment.configure(bg='black')
        self.window_edit_payment.iconbitmap('resources/icon.ico')
        self.payment_ui()

    def entered_storage_save_button(self, event):
        self.save_button.configure(bg='#a3ffb3')

    def leave_storage_save_button(self, event):
        self.save_button.configure(bg='#f1f5e0')

    def entered_storage_clear_button(self, event):
        self.clear_button.configure(bg='#a3ffb3')

    def leave_storage_clear_button(self, event):
        self.clear_button.configure(bg='#f1f5e0')

    def entered_storage_exit_button(self, event):
        self.exit_button.configure(bg='#a3ffb3')

    def leave_storage_exit_button(self, event):
        self.exit_button.configure(bg='#f1f5e0')

    def payment_ui(self):

        self.background = tk.PhotoImage(file='resources/line.png')
        self.background_image = tk.Label(self.window_edit_payment, image=self.background, bg='black')
        self.background_image.place(x=5, y=240)

        self.heading = tk.Label(self.window_edit_payment, text='Store your Information Safely',
                            font=('arial', 20, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.about_image = tk.PhotoImage(file='resources/about.png')
        self.about_icon = tk.Button(self.window_edit_payment, image=self.about_image, bg='black', fg='white',
                                 relief='flat', command=self.open_about)
        self.about_icon.place(x=440, y=0)

        self.feature_name = tk.Label(self.window_edit_payment, text='Feature Name', font=(
                                    'arial', 12, 'bold'), bg='black', fg='white')
        self.feature_name.place(x=13, y=50)

        self.feature_name_entry_var = tk.StringVar()
        self.feature_name_entry = tk.Entry(self.window_edit_payment, textvariable=self.feature_name_entry_var, font=(
                                            'arial', 12), bg='#C0C0C0', width=20)
        self.feature_name_entry.place(x=130, y=50)
        self.feature_name_entry_var.set(self.fe_name)
        self.feature_name_entry.focus()

        self.note_for_feature_name = tk.Label(self.window_edit_payment,
                                      text='Note: Feature name is displayed on the button in the Main window',
                                      font=('arial', 10), bg='black', fg='orange')
        self.note_for_feature_name.place(x=2, y=75)

        self.card_number_label = tk.Label(self.window_edit_payment, text='Card Number', font=(
                                          'arial', 12, 'bold'), bg='black', fg='white')
        self.card_number_label.place(x=20, y=100)

        self.card_number_entry_var = tk.StringVar()
        self.card_number_entry = tk.Entry(self.window_edit_payment, textvariable=self.card_number_entry_var, font=(
                                          'arial', 12), bg='#C0C0C0', width=20)
        self.card_number_entry.place(x=130, y=100)
        self.card_number_entry_var.set(self.card_number)
        self.data_card_number = self.card_number_entry_var.get()

        self.copy_image = tk.PhotoImage(file='resources/copy.png')
        self.copy_card_number = tk.Button(self.window_edit_payment, image=self.copy_image, relief='groove',
                                  command=lambda: self.copy_data(self.data_card_number))
        self.copy_card_number.place(x=320, y=100)

        self.name_on_card_label = tk.Label(self.window_edit_payment, text='Name on Card', font=(
                                           'arial', 12, 'bold'), bg='black', fg='white')
        self.name_on_card_label.place(x=13, y=125)

        self.name_on_card_entry_var = tk.StringVar()
        self.name_on_card_entry = tk.Entry(self.window_edit_payment, textvariable=self.name_on_card_entry_var, font=(
                                           'arial', 12), bg='#C0C0C0', width=20)
        self.name_on_card_entry.place(x=130, y=125)
        self.name_on_card_entry_var.set(self.name_on_card)
        self.data_name_card = self.name_on_card_entry_var.get()

        self.copy_card_number = tk.Button(self.window_edit_payment, image=self.copy_image, relief='groove',
                                          command=lambda: self.copy_data(self.data_name_card))
        self.copy_card_number.place(x=320, y=125)

        self.expiry_date_label = tk.Label(self.window_edit_payment, text='Expiry Date', font=(
                                          'arial', 12, 'bold'), bg='black', fg='white')
        self.expiry_date_label.place(x=35, y=150)

        self.expiry_date_entry_var = tk.StringVar()
        self.expiry_date_entry = tk.Entry(self.window_edit_payment, textvariable=self.expiry_date_entry_var, font=(
                                          'arial', 12), bg='#C0C0C0', width=20)
        self.expiry_date_entry.place(x=130, y=150)
        self.expiry_date_entry_var.set(self.expiry_date)
        self.data_expiry = self.expiry_date_entry_var.get()

        self.copy_card_number = tk.Button(self.window_edit_payment, image=self.copy_image, relief='groove',
                                  command=lambda: self.copy_data(self.data_expiry))
        self.copy_card_number.place(x=320, y=150)

        self.draw_line = tk.Label(self.window_edit_payment,bg='black', fg='white',
                text='-----------------------------------------------------------------------------------------------')
        self.draw_line.place(x=0, y=170)

        self.heading_2 = tk.Label(self.window_edit_payment, bg='black', fg='orange',
                                  text='Net Banking Details (If Any)', font=('arial', 10))
        self.heading_2.place(x=140, y=185)

        self.username_label = tk.Label(self.window_edit_payment, text='Username', font=(
                                       'arial', 12, 'bold'), bg='black', fg='white')
        self.username_label.place(x=40, y=210)

        self.username_entry_var = tk.StringVar()
        self.username_entry = tk.Entry(self.window_edit_payment, textvariable=self.username_entry_var, font=(
                                       'arial', 12), bg='#C0C0C0', width=20)
        self.username_entry.place(x=130, y=210)
        self.username_entry_var.set(self.pay_username)
        self.data_user = self.username_entry_var.get()

        self.copy_card_number = tk.Button(self.window_edit_payment, image=self.copy_image, relief='groove',
                                  command=lambda: self.copy_data(self.data_user))
        self.copy_card_number.place(x=320, y=210)

        self.password = tk.Label(self.window_edit_payment, text='Password', font=(
                                 'arial', 12, 'bold'), bg='black', fg='white')
        self.password.place(x=40, y=235)

        self.password_entry_var = tk.StringVar()
        self.password_entry = tk.Entry(self.window_edit_payment, textvariable=self.password_entry_var, font=(
                                       'arial', 12), bg='#C0C0C0', width=20, show="*")
        self.password_entry.place(x=130, y=235)
        self.password_entry_var.set(self.pay_password)
        self.data_password = self.password_entry_var.get()

        self.copy_card_number = tk.Button(self.window_edit_payment, image=self.copy_image, relief='groove',
                                          command=lambda: self.copy_data(self.data_password))
        self.copy_card_number.place(x=320, y=235)

        self.save_button = tk.Button(self.window_edit_payment,text='Save',relief='groove',width=8,bg='#f1f5e0',font=(
                        'consolas', 13, 'bold'),command=self.get_payment_data)
        self.save_button.place(x=30, y=300)
        self.save_button.bind('<Enter>', self.entered_storage_save_button)
        self.save_button.bind('<Leave>', self.leave_storage_save_button)

        self.clear_button = tk.Button(self.window_edit_payment, text='Clear', font=(
                                'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.clear)
        self.clear_button.place(x=180, y=300)
        self.clear_button.bind('<Enter>', self.entered_storage_clear_button)
        self.clear_button.bind('<Leave>', self.leave_storage_clear_button)

        self.exit_button = tk.Button(self.window_edit_payment,text='Exit',font=(
                            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.exit_window)
        self.exit_button.place(x=330, y=300)
        self.exit_button.bind('<Enter>', self.entered_storage_exit_button)
        self.exit_button.bind('<Leave>', self.leave_storage_exit_button)

        self.window_edit_payment.mainloop()

    def get_payment_data(self):
        """This method gets the data and sends to back_end to update the database"""
        fe_name = self.feature_name_entry_var.get()
        card_no = self.card_number_entry_var.get()
        name_card = self.name_on_card_entry_var.get()
        expiry = self.expiry_date_entry_var.get()
        pay_username = self.username_entry_var.get()
        pay_password = self.password_entry_var.get()

        self.update_payment_data(fe_name,card_no,name_card,expiry,pay_username,pay_password)

    def update_payment_data(self, fe_name, card_number, name_on_card, expiry_date, pay_username,
                            pay_password):
        """This method updates the payment data to the database"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()

        try:
            update_payment = f"""UPDATE {self.username}_payment set fe_name = "{fe_name}",     
                    card_number = "{card_number}",
                    name_on_card = "{name_on_card}" ,
                    expiry_date = "{expiry_date}",
                    username = "{pay_username}",
                    password = "{pay_password}"
                    WHERE val_no = "{self.button_name}" """

            cursor.execute(update_payment)

            msgb.showinfo('Success', 'You have successfully update the data')

        except Error as e:
            print(e)

        conn.commit()
        conn.close()

        self.change_the_payment_box_name()
        self.window_edit_payment.destroy()

    def clear(self):
        """This method clears all the entries of the window"""
        self.feature_name_entry_var.set('empty')
        self.card_number_entry_var.set('')
        self.name_on_card_entry_var.set('')
        self.expiry_date_entry_var.set('')
        self.username_entry_var.set('')
        self.password_entry_var.set('')
        self.feature_name_entry.focus()

    def exit_window(self):
        """This method closes the window thus ending the software"""
        self.window_edit_payment.destroy()

    @staticmethod
    def open_about():
        About_Window()

    @staticmethod
    def copy_data(text):
        """This method copies the data in the entry box to the clipboard"""
        pc.copy(text)


class Address_Window(Main_Window):
    """This class runs the UI of the Address Window"""

    def __init__(self,username,full_name, button_name,fe_name,address_1, address_2, town, district,state, pin):
        """This __init__ method is to defines the Address Window elements and strings from database"""
        self.username = username
        self.full_name = full_name
        super(Address_Window, self).__init__(self.username, self.full_name)
        self.button_name = button_name
        self.fe_name = fe_name
        self.address_1 = address_1
        self.address_2 = address_2
        self.town = town
        self.district = district
        self.state = state
        self.pin = pin

        if (self.address_1 is None and self.address_2 is None and self.town is None and self.district is None and
            self.state is None and self.pin is None) and self.fe_name == "empty":
            """This condition is to set the variables to empty is database return None"""
            self.fe_name = 'empty'
            self.address_1 = ''
            self.address_2 = ''
            self.town = ''
            self.district = ''
            self.state = ''
            self.pin = ''

        else:
            pass

        self.window_edit_address = tk.Toplevel()
        self.window_edit_address.title('Store your address')
        self.window_edit_address.geometry('475x350')
        self.window_edit_address.resizable(False, False)
        self.window_edit_address.configure(bg='black')
        self.window_edit_address.iconbitmap('resources/icon.ico')
        self.address_ui()

    def entered_storage_save_button(self, event):
        self.save_button.configure(bg='#a3ffb3')

    def leave_storage_save_button(self, event):
        self.save_button.configure(bg='#f1f5e0')

    def entered_storage_clear_button(self, event):
        self.clear_button.configure(bg='#a3ffb3')

    def leave_storage_clear_button(self, event):
        self.clear_button.configure(bg='#f1f5e0')

    def entered_storage_exit_button(self, event):
        self.exit_button.configure(bg='#a3ffb3')

    def leave_storage_exit_button(self, event):
        self.exit_button.configure(bg='#f1f5e0')

    def address_ui(self):
        """This methods adds widgets to the Address Window"""

        self.background = tk.PhotoImage(file='resources/line.png')
        self.background_image = tk.Label(self.window_edit_address, image=self.background,
                                    bg='black')
        self.background_image.place(x=5, y=240)

        self.heading = tk.Label(self.window_edit_address, text='Store your Information Safely',
                           font=('arial', 20, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.about_image = tk.PhotoImage(file='resources/about.png')
        self.about_icon = tk.Button(self.window_edit_address, image=self.about_image, bg='black', fg='white', relief='flat',
                               command=self.open_about)
        self.about_icon.place(x=440, y=0)

        self.feature_name = tk.Label(self.window_edit_address, text='Feature Name', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.feature_name.place(x=10, y=50)

        self.feature_name_entry_var = tk.StringVar()
        self.feature_name_entry = tk.Entry(self.window_edit_address, textvariable=self.feature_name_entry_var, font=(
                                            'arial', 12), bg='#C0C0C0', width=20)
        self.feature_name_entry.place(x=130, y=50)
        self.feature_name_entry_var.set(self.fe_name)
        self.feature_name_entry.focus()

        self.note_for_feature_name = tk.Label(self.window_edit_address,
                                    text='Note: Feature name is displayed on the button in the Main window', font=(
                                    'arial', 10), bg='black', fg='orange')
        self.note_for_feature_name.place(x=2, y=75)

        self.address_line_1 = tk.Label(self.window_edit_address, text='Address Line 1', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.address_line_1.place(x=5, y=100)

        self.address_line_1_entry_var = tk.StringVar()
        self.address_line_1_entry = tk.Entry(self.window_edit_address, textvariable=self.address_line_1_entry_var,
                                             font=('arial', 12), bg='#C0C0C0', width=30)
        self.address_line_1_entry.place(x=130, y=100)
        self.address_line_1_entry_var.set(self.address_1)
        self.data_add_1 = self.address_line_1_entry_var.get()

        self.copy_image = tk.PhotoImage(file='resources/copy.png')
        self.copy_add_1 = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                               command=lambda: self.copy_data(self.data_add_1))
        self.copy_add_1.place(x=410, y=100)

        self.address_line_2 = tk.Label(self.window_edit_address, text='Address Line 2', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.address_line_2.place(x=5, y=125)

        self.address_line_2_entry_var = tk.StringVar()
        self.address_line_2_entry = tk.Entry(self.window_edit_address, textvariable=self.address_line_2_entry_var,
                                             font=('arial', 12), bg='#C0C0C0', width=30)
        self.address_line_2_entry.place(x=130, y=125)
        self.address_line_2_entry_var.set(self.address_2)
        self.data_add_2 = self.address_line_2_entry_var.get()

        self.copy_add_2 = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                               command=lambda: self.copy_data(self.data_add_2))
        self.copy_add_2.place(x=410, y=125)

        self.town_label = tk.Label(self.window_edit_address, text='Town/City', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.town_label.place(x=40, y=150)

        self.town_entry_var = tk.StringVar()
        self.town_entry = tk.Entry(self.window_edit_address, textvariable=self.town_entry_var, font=(
            'arial', 12), bg='#C0C0C0', width=20)
        self.town_entry.place(x=130, y=150)
        self.town_entry_var.set(self.town)
        self.town_data = self.town_entry_var.get()

        self.copy_town = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                              command=lambda: self.copy_data(self.town_data))
        self.copy_town.place(x=320, y=150)

        self.district_label = tk.Label(self.window_edit_address, text='District', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.district_label.place(x=60, y=175)

        self.district_entry_var = tk.StringVar()
        self.district_entry = tk.Entry(self.window_edit_address, textvariable=self.district_entry_var,
                                  font=('arial', 12), bg='#C0C0C0', width=20)
        self.district_entry.place(x=130, y=175)
        self.district_entry_var.set(self.district)
        self.data_district = self.district_entry_var.get()

        self.copy_district = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                                  command=lambda: self.copy_data(self.data_district))
        self.copy_district.place(x=320, y=175)

        self.state_label = tk.Label(self.window_edit_address, text='State', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.state_label.place(x=75, y=200)

        self.state_entry_var = tk.StringVar()
        self.state_entry = tk.Entry(self.window_edit_address, textvariable=self.state_entry_var,
                               font=('arial', 12), bg='#C0C0C0', width=20)
        self.state_entry.place(x=130, y=200)
        self.state_entry_var.set(self.state)
        self.data_state = self.state_entry_var.get()

        self.copy_state = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                               command=lambda: self.copy_data(self.data_state))
        self.copy_state.place(x=320, y=200)

        self.pin_label = tk.Label(self.window_edit_address, text='Pin Code', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.pin_label.place(x=45, y=225)

        self.pin_code_entry_var = tk.StringVar()
        self.pin_code_entry = tk.Entry(self.window_edit_address, textvariable=self.pin_code_entry_var,
                                  font=('arial', 12), bg='#C0C0C0', width=20)
        self.pin_code_entry.place(x=130, y=225)
        self.pin_code_entry_var.set(self.pin)
        self.data_pin = self.pin_code_entry_var.get()

        self.copy_pin = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                             command=lambda: self.copy_data(self.data_pin))
        self.copy_pin.place(x=320, y=225)

        self.save_button = tk.Button(self.window_edit_address, text='Save', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0',
                                command=self.get_data)
        self.save_button.place(x=30, y=300)
        self.save_button.bind('<Enter>', self.entered_storage_save_button)
        self.save_button.bind('<Leave>', self.leave_storage_save_button)

        self.clear_button = tk.Button(self.window_edit_address, text='Clear', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.clear)
        self.clear_button.place(x=180, y=300)
        self.clear_button.bind('<Enter>', self.entered_storage_clear_button)
        self.clear_button.bind('<Leave>', self.leave_storage_clear_button)

        self.exit_button = tk.Button(self.window_edit_address, text='Exit', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.exit_window)
        self.exit_button.place(x=330, y=300)
        self.exit_button.bind('<Enter>', self.entered_storage_exit_button)
        self.exit_button.bind('<Leave>', self.leave_storage_exit_button)

        self.window_edit_address.focus_force()
        self.window_edit_address.mainloop()

    def get_data(self):
        """This method collects the data to update the database"""

        fe_name = self.feature_name_entry_var.get()
        add_1 = self.address_line_1_entry_var.get()
        add_2 = self.address_line_2_entry_var.get()
        town_var = self.town_entry_var.get()
        district_var = self.district_entry_var.get()
        state_var = self.state_entry_var.get()
        pin_var = self.pin_code_entry_var.get()

        self.update_address_data(fe_name, add_1, add_2, town_var, district_var, state_var,pin_var)

    def update_address_data(self, fe_name, add_1, add_2, town, district, state, pin):
        """This method updates the data in the address table in database"""
        conn = sq.connect('database.db')
        cursor = conn.cursor()

        update = f"""UPDATE {self.username}_address set fe_name = "{fe_name}",     
                line_1 = "{add_1}",
                line_2 = "{add_2}" ,
                city = "{town}",
                district = "{district}",
                state = "{state}",
                pin_code = "{pin}"
                WHERE val_no = "{self.button_name}" """
        cursor.execute(update)

        msgb.showinfo('Success', 'You have successfully update the data')

        conn.commit()
        conn.close()

        self.change_the_address_box_name(root)

        self.window_edit_address.destroy()

    @staticmethod
    def open_about():
        About_Window()

    @staticmethod
    def copy_data(text):
        """This method copies the selected data to the clipboard"""
        pc.copy(text)

    def exit_window(self):
        """This method exits Address Window"""
        self.window_edit_address.destroy()

    def clear(self):
        """ Clears all the input in the window"""
        self.feature_name_entry_var.set('empty')
        self.address_line_1_entry_var.set('')
        self.address_line_2_entry_var.set('')
        self.town_entry_var.set('')
        self.district_entry_var.set('')
        self.state_entry_var.set('')
        self.pin_code_entry_var.set('')
        self.feature_name_entry.focus()



if __name__ == '__main__':
    Login_Window()