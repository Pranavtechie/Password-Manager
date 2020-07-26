"""This module manages the UI of the Password Edit window"""

import tkinter as tk
import about
import pyperclip as pc
import main_window
import sqlite3 as sq
from sqlite3 import Error
from tkinter import messagebox as msgb

class Password_Window(object):
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
        self.init_ui()

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

    def init_ui(self):
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
                                    command=lambda: copy_data(data_ref_2))
        self.copy_ref_2.place(x=320, y=190)

        self.save_button = tk.Button(self.window_edit_password, text='Save', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0',
                                command=self.get_data)
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

        self.window_edit_password.focus_force()
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

        msgb.showinfo('Success', 'You have successfully updated the data')

        conn.commit()
        conn.close()

        main_window.object.change_the_password_box_name(self.username)

        self.window_edit_password.destroy()

    @staticmethod
    def open_about():
        """This method opens the About Window"""
        about.About_Window()

    @staticmethod
    def copy_data(text):
        """This method copies the data in the entry box to the clipboard"""
        pc.copy(text)
