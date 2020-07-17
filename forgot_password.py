"""This module manages the UI of the Forgot Password window"""
import tkinter as tk
import about
from tkinter import messagebox as msgb
import login
import sqlite3 as sq

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
                    'consolas', 13, 'bold'), bg='#f1f5e0', command=lambda: change_the_password(username))
        self.change_password.place(x=130, y=280)

        self.clear_password = tk.Button(self.window_forgot, text = 'Clear',relief='groove',width=8,font=(
                                        'consolas', 13, 'bold'), bg='#f1f5e0', command=self.password_clear)
        self.clear_password.place(x=300, y=280)

    @staticmethod
    def open_about():
        """This method opens the About Window"""
        about.About_Window()

    def back(self):
        """This method closes the forgot_password window and redirects to login window"""
        self.window_forgot.destroy()

        login.Login_Window()

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
            self.login.open_window()

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
