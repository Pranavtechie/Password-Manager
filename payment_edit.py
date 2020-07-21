"""This module manages the UI of the Payment edit window"""
import tkinter as tk
import about
import pyperclip as pc
import sqlite3 as sq
from sqlite3 import Error
from tkinter import messagebox as msgb
import main_window

class Payment_Window(object):

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

        self.update_payment_data(fe_name, card_no, name_card, expiry,
                                     pay_username, pay_password)

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

            msgb.showinfo('Success', 'You have successfully updated the data')

        except Error as e:
            print(e)

        conn.commit()
        conn.close()

        main_window.object.change_the_payment_box_name(self.username)

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
        about.About_Window()

    @staticmethod
    def copy_data(text):
        """This method copies the data in the entry box to the clipboard"""
        pc.copy(text)
