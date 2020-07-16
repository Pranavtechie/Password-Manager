"""This module manages the UI of the Forgot Password window"""
import tkinter as tk
import about
import back_end
from tkinter import messagebox as msgb
import login

def back():
    """This function closes the forgot_password window and
redirects to login window"""
    window_forgot.destroy()

    login.open_window()

def change_the_password(username):
    """This function passes the data to the back_end to update the password"""
    pass_1 = enter_new_password_entry_var.get()
    pass_2 = retype_password_entry_var.get()

    if pass_1 == pass_2:
        back_end.update_password(username, pass_1)
        window_forgot.destroy()
        login.open_window()


    else:
        pass

def clear_username_entry():
    """This function clears the data in the entry box of the username"""
    username_entry_var.set('')

def password_clear():
    """This function clears the data in the passwords entry boxes"""
    enter_new_password_entry_var.set('')
    retype_password_entry_var.set('')


def open_window():
    """This function runs the UI of the forgot_password"""
    
    def entered_get_question(event):
        get_question.configure(bg = 'gold')
        
    def leave_get_question(event):
        get_question.configure(bg = 'light blue')
        
    def entered_clear_usr(event):
        clear_username.configure(bg = 'gold')
        
    def leave_clear_usr(event):
        clear_username.configure(bg = 'light blue')
        

    def enter_changes(username):
        """This function manages the UI of the password entry and gets the new password data """

        enter_new_password = tk.Label(window_forgot, text = 'Enter New Password',font=(
            'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
        enter_new_password.place(x=5, y=210)

        global enter_new_password_entry_var
        enter_new_password_entry_var = tk.StringVar()
        enter_new_password_entry = tk.Entry(window_forgot, textvariable=enter_new_password_entry_var, width=20, font=(
            'arial', 12), bg='#C0C0C0')
        enter_new_password_entry.place(x=170, y=210)

        retype_password = tk.Label(window_forgot, text='Retype Password', font=(
            'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
        retype_password.place(x=30, y=240)

        global retype_password_entry_var
        retype_password_entry_var = tk.StringVar()
        retype_password_entry = tk.Entry(window_forgot, textvariable=retype_password_entry_var, width=20, font=(
                                            'arial', 12), bg='#C0C0C0')
        retype_password_entry.place(x=170, y=240)

        change_password = tk.Button(window_forgot, text = 'Change Password',font=(
        'consolas', 13, 'bold'), relief='groove', width=15, bg='#f1f5e0', command=lambda: change_the_password(username))
        change_password.place(x=130, y=280)

        clear_password = tk.Button(window_forgot, text = 'Clear',font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=password_clear)
        clear_password.place(x=300, y=280)




    def show_question():
        """This function shows the security question to change the password"""

        def change_pass():
            """This function destroys the widgets in the window to show password widgets"""

            answer_1 = security_answer_1_var.get()
            answer_2 = security_answer_2_var.get()
            usr = given_username
            security_question_1.destroy()
            security_question_1_text.destroy()
            security_answer_1.destroy()
            security_answer_1_entry.destroy()
            security_question_2.destroy()
            security_question_2_text.destroy()
            security_answer_2.destroy()
            security_answer_2_entry.destroy()
            change_password.destroy()
            get_question.destroy()
            clear_username.destroy()
            username_entry.configure(state = 'disabled')

            check_for_answer = back_end.check_answers(usr, answer_1, answer_2)

            if check_for_answer:
                enter_changes(usr)

        def entered_change(event):
            change_password.configure(bg='#a3ffb3')

        def leave_change(event):
            change_password.configure(bg='#f1f5e0')

        global given_username
        given_username = username_entry_var.get()

        auth = back_end.check_username_for_signup(given_username)
        if not auth:
            sq_1, sq_2 = back_end.get_question(given_username)

            security_question_1 = tk.Label(window_forgot, text='Security Question 1', font=(
                'arial', 12, 'bold'), fg='#FFB6C1', bg='black')
            security_question_1.place(x=3, y=180)
    
            security_question_1_text = tk.Text(window_forgot, height=1, width=48, font=(
                'georgia', 10), relief='flat', bg='white')
            security_question_1_text.place(x=160, y=180)
            question_1 = f"{sq_1}"
            security_question_1_text.insert(tk.END, question_1)
            security_question_1_text.configure(state='disabled')
    
            security_answer_1 = tk.Label(window_forgot, text='Answer 1', font=(
                'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
            security_answer_1.place(x=80, y=210)
    
            global security_answer_1_var
            security_answer_1_var = tk.StringVar()
            security_answer_1_entry = tk.Entry(window_forgot, textvariable=security_answer_1_var, width=20, font=(
                'arial', 12), bg='#C0C0C0')
            security_answer_1_entry.place(x=160, y=210)
    
            security_question_2 = tk.Label(window_forgot, text='Security Question 2', font=(
                'arial', 12, 'bold'), bg='black', fg='#98FB98')
            security_question_2.place(x=3, y=260)
    
            security_question_2_text = tk.Text(window_forgot, height=1, width=48, font=(
                'georgia', 10), relief='flat', bg='white')
            security_question_2_text.place(x=160, y=260)
            question_2 = f"{sq_2}"
            security_question_2_text.insert(tk.END, question_2)
            security_question_2_text.configure(state='disabled')
    
            security_answer_2 = tk.Label(window_forgot, text='Answer 2', font=(
                'arial', 12, 'bold'), bg='black', fg='#98FB98')
            security_answer_2.place(x=80, y=290)
    
            global security_answer_2_var
            security_answer_2_var = tk.StringVar()
            security_answer_2_entry = tk.Entry(window_forgot, textvariable=security_answer_2_var, width=20, font=(
                'arial', 12), bg='#C0C0C0')
            security_answer_2_entry.place(x=160, y=290)
    
            change_password = tk.Button(window_forgot, text='Change Password', font=(
                'consolas', 13, 'bold'), relief='groove', width=16, bg='#f1f5e0', command=change_pass)
            change_password.place(x=170, y=320)
            change_password.bind('<Enter>', entered_change)
            change_password.bind('<Leave>', leave_change)
            
        else:
            msgb.showerror('Error in Username Check', 'The entered Username does not exists please try again')

    global window_forgot
    window_forgot = tk.Tk()
    window_forgot.title('Forgot Password')
    window_forgot.resizable(False, False)
    window_forgot.configure(bg = 'black')
    window_forgot.geometry('600x500')
    window_forgot.iconbitmap('resources/icon.ico')

    heading = tk.Label(window_forgot, text = 'Forgot Password', font=(
                        'arial', 18, 'bold'), bg='black', fg='orange')
    heading.pack()

    about_image = tk.PhotoImage(file='resources/about.png')
    about_icon = tk.Button(window_forgot, image=about_image, bg='black', fg='white', relief='flat',
                           command=about.open_window)
    about_icon.place(x=565, y=0)

    pic = tk.PhotoImage(file='resources/back.png')
    dis = tk.Button(window_forgot, image=pic, bg='black', command=back, relief='flat')
    dis.place(x=0, y=0)

    happy_img = tk.PhotoImage(file="resources/happy.png")
    happy = tk.Label(window_forgot, text="Don't worry we are here to recover you account ", image=happy_img, compound='right',
                     bg='black', fg='white', font=('Maiandra GD', 14))
    happy.place(x=70, y=40)

    username = tk.Label(window_forgot, text = 'Username',font=(
                        'timesnewroman', 12), bg='black', fg='white')
    username.place(x=60, y=90)

    global username_entry_var
    username_entry_var = tk.StringVar()
    username_entry = tk.Entry(window_forgot, font=('arial', 12),
                              bg='#C0C0C0', textvariable=username_entry_var)
    username_entry.place(x=140, y=90)
    username_entry.focus()

    get_question = tk.Button(window_forgot, text = 'Get Questions',bg = 'light blue',relief = 'groove',
                          font = ('Maiandra GD',12,'bold'), width = 12, command = show_question)
    get_question.place(x = 160, y = 130)
    get_question.bind('<Enter>', entered_get_question)
    get_question.bind('<Leave>', leave_get_question)
    

    clear_username = tk.Button(window_forgot, text='Clear', bg='light blue', relief='groove',
                             font=('Maiandra GD', 12, 'bold'), width=8, command=clear_username_entry)
    clear_username.place(x=320,y=130)
    clear_username.bind('<Enter>', entered_clear_usr)
    clear_username.bind('<Leave>', leave_clear_usr)

    window_forgot.focus_force()
    window_forgot.mainloop()
