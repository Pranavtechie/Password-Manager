"""This module manages the UI of the Payment edit window"""
import tkinter as tk
import about
import back_end
import pyperclip as pc

def open_about():
    about.About_Window()

def copy_data(text):
    """This function copies the data in the entry box to the clipboard"""
    pc.copy(text)

def get_payment_data(candidate_username, button_value):
    """This function gets the data and sends to back_end to update the database"""
    fe_name = feature_name_entry_var.get()
    card_no = card_number_entry_var.get()
    name_card = name_on_card_entry_var.get()
    expiry = expiry_date_entry_var.get()
    pay_username = username_entry_var.get()
    pay_password = password_entry_var.get()


    back_end.update_payment_data(candidate_username, button_value,fe_name, card_no, name_card, expiry, pay_username, pay_password)

def clear():
    """This function clears all the entries of the window"""
    feature_name_entry_var.set('empty')
    card_number_entry_var.set('')
    name_on_card_entry_var.set('')
    expiry_date_entry_var.set('')
    username_entry_var.set('')
    password_entry_var.set('')

    feature_name_entry.focus()


def exit_window():
    """This function closes the window thus ending the software"""
    window_edit_payment.destroy()


def open_window(username, button_name,fe_name, card_number, name_on_card, expiry_date, pay_username, pay_password):
    """This function runs the UI of the payment edit window"""

    if card_number is None and name_on_card is None and expiry_date is None and pay_username is None and pay_password is None:
        card_number = ''
        name_on_card = ''
        expiry_date = ''
        pay_username = ''
        pay_password = ''

    else:
        pass

    def entered_storage_save_button(event):
        save_button.configure(bg='#a3ffb3')

    def leave_storage_save_button(event):
        save_button.configure(bg='#f1f5e0')

    def entered_storage_clear_button(event):
        clear_button.configure(bg='#a3ffb3')

    def leave_storage_clear_button(event):
        clear_button.configure(bg='#f1f5e0')

    def entered_storage_exit_button(event):
        exit_button.configure(bg='#a3ffb3')

    def leave_storage_exit_button(event):
        exit_button.configure(bg='#f1f5e0')

    global window_edit_payment
    window_edit_payment = tk.Toplevel()
    window_edit_payment.title('Store your Payment Information')
    window_edit_payment.geometry('475x350')
    window_edit_payment.resizable(False, False)
    window_edit_payment.configure(bg='black')
    window_edit_payment.iconbitmap('resources/icon.ico')

    background = tk.PhotoImage(file = 'resources/line.png')
    background_image = tk.Label(window_edit_payment, image=background,
                                bg='black')
    background_image.place(x=5, y=240)

    heading = tk.Label(window_edit_payment, text='Store your Information Safely',
                       font=('arial', 20, 'bold'), bg='black', fg='orange')
    heading.pack()

    about_image = tk.PhotoImage(file='resources/about.png')
    about_icon = tk.Button(window_edit_payment, image=about_image, bg='black', fg='white', relief='flat',
                           command=open_about)
    about_icon.place(x=440, y=0)

    feature_name = tk.Label(window_edit_payment, text='Feature Name', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    feature_name.place(x=13, y=50)

    global feature_name_entry_var
    feature_name_entry_var = tk.StringVar()
    global feature_name_entry
    feature_name_entry = tk.Entry(window_edit_payment, textvariable=feature_name_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    feature_name_entry.place(x=130, y=50)
    feature_name_entry_var.set(fe_name)
    feature_name_entry.focus()

    note_for_feature_name = tk.Label(window_edit_payment, text='Note: Feature name is displayed on the button in the Main window', font=(
        'arial', 10), bg='black', fg='orange')
    note_for_feature_name.place(x=2, y=75)

    card_number_label = tk.Label(window_edit_payment, text='Card Number', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    card_number_label.place(x=20, y=100)

    global card_number_entry_var
    card_number_entry_var = tk.StringVar()
    card_number_entry = tk.Entry(window_edit_payment, textvariable=card_number_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    card_number_entry.place(x=130, y=100)
    card_number_entry_var.set(card_number)
    data_card_number = card_number_entry_var.get()

    copy_image = tk.PhotoImage(file='resources/copy.png')
    copy_card_number = tk.Button(window_edit_payment, image=copy_image, relief='groove', command=lambda: copy_data(data_card_number))
    copy_card_number.place(x=320, y=100)

    name_on_card_label = tk.Label(window_edit_payment, text='Name on Card', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    name_on_card_label.place(x=13,  y=125)

    global name_on_card_entry_var
    name_on_card_entry_var = tk.StringVar()
    name_on_card_entry = tk.Entry(window_edit_payment, textvariable=name_on_card_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    name_on_card_entry.place(x=130, y=125)
    name_on_card_entry_var.set(name_on_card)
    data_name_card = name_on_card_entry_var.get()

    copy_card_number = tk.Button(window_edit_payment, image=copy_image, relief='groove',
                                 command=lambda: copy_data(data_name_card))
    copy_card_number.place(x=320, y=125)


    expiry_date_label = tk.Label(window_edit_payment, text='Expiry Date', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    expiry_date_label.place(x=35, y=150)

    global expiry_date_entry_var
    expiry_date_entry_var = tk.StringVar()
    expiry_date_entry = tk.Entry(window_edit_payment, textvariable=expiry_date_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    expiry_date_entry.place(x=130, y=150)
    expiry_date_entry_var.set(expiry_date)
    data_expiry = expiry_date_entry_var.get()

    copy_card_number = tk.Button(window_edit_payment, image=copy_image, relief='groove',
                                 command=lambda: copy_data(data_expiry))
    copy_card_number.place(x=320, y=150)

    draw_line = tk.Label(
        window_edit_payment, text='-----------------------------------------------------------------------------------------------', bg='black', fg='white')
    draw_line.place(x=0, y=170)

    header = tk.Label(window_edit_payment,
                      text='Net Banking Details (If Any)', bg='black', fg='orange', font=('arial', 10))
    header.place(x=140, y=185)

    username_label = tk.Label(window_edit_payment, text='Username', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    username_label.place(x=40, y=210)

    global username_entry_var
    username_entry_var = tk.StringVar()
    username_entry = tk.Entry(window_edit_payment, textvariable=username_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    username_entry.place(x=130, y=210)
    username_entry_var.set(pay_username)
    data_user = username_entry_var.get()

    copy_card_number = tk.Button(window_edit_payment, image=copy_image, relief='groove',
                                 command=lambda: copy_data(data_user))
    copy_card_number.place(x=320, y=210)

    password = tk.Label(window_edit_payment, text='Password', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    password.place(x=40, y=235)

    global password_entry_var
    password_entry_var = tk.StringVar()
    password_entry = tk.Entry(window_edit_payment, textvariable=password_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20, show = "*")
    password_entry.place(x=130, y=235)
    password_entry_var.set(pay_password)
    data_password = password_entry_var.get()

    copy_card_number = tk.Button(window_edit_payment, image=copy_image, relief='groove',
                                 command=lambda: copy_data(data_password))
    copy_card_number.place(x=320, y=235)

    save_button = tk.Button(window_edit_payment, text='Save', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command = lambda: get_payment_data(username, button_name))
    save_button.place(x=30, y=300)
    save_button.bind('<Enter>', entered_storage_save_button)
    save_button.bind('<Leave>', leave_storage_save_button)

    clear_button = tk.Button(window_edit_payment, text='Clear', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=clear)
    clear_button.place(x=180, y=300)
    clear_button.bind('<Enter>', entered_storage_clear_button)
    clear_button.bind('<Leave>', leave_storage_clear_button)

    exit_button = tk.Button(window_edit_payment, text='Exit', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=exit_window)
    exit_button.place(x=330, y=300)
    exit_button.bind('<Enter>', entered_storage_exit_button)
    exit_button.bind('<Leave>', leave_storage_exit_button)

    window_edit_payment.mainloop()
