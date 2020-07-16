"""This module manages the UI of the Password Edit window"""

import tkinter as tk
import back_end
import about
import pyperclip as pc

def open_about():
    about.About_Window()

def get_data(username, button_value):
    """This function get's the data from the entry to save in the database"""
    fe_name = feature_name_entry_var.get()
    pass_username = save_username_entry_var.get()
    pass_password = save_password_entry_var.get()
    ref_1 = ref_1_entry_var.get()
    ref_2 = ref_2_entry_var.get()

    back_end.update_password_data(username, button_value, fe_name, pass_username, pass_password, ref_1, ref_2)


def copy_data(text):
    """This function copies the data in the entry box to the clipboard"""
    pc.copy(text)

def clear():
    """It clears all the entries in the function"""
    feature_name_entry_var.set('empty')
    save_username_entry_var.set('')
    save_password_entry_var.set('')
    ref_1_entry_var.set('')
    ref_2_entry_var.set('')
    feature_name_entry.focus()


def exit():
    """ It closes the window and exiting the program"""
    window_edit_password.destroy()


def open_window(username, button_name,fe_name,pass_username,pass_password, ref_1, ref_2):
    """This function runs the UI of the Password Edit window"""
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

    global window_edit_password
    window_edit_password = tk.Toplevel()
    window_edit_password.title('Store your passwords')
    window_edit_password.geometry('475x300')
    window_edit_password.resizable(False, False)
    window_edit_password.configure(bg='black')
    window_edit_password.iconbitmap('resources/icon.ico')

    background = tk.PhotoImage(file = 'resources/line.png')
    background_image = tk.Label(window_edit_password, image=background,
                                bg='black')
    background_image.place(x=5, y=190)

    heading = tk.Label(window_edit_password, text='Store your Passwords Safely',
                       font=('arial', 20, 'bold'), bg='black', fg='orange')
    heading.pack()

    about_image = tk.PhotoImage(file='resources/about.png')
    about_icon = tk.Button(window_edit_password, image=about_image, bg='black', fg='white', relief='flat',
                           command=open_about)
    about_icon.place(x=440, y=0)

    feature_name = tk.Label(window_edit_password, text='Feature Name', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    feature_name.place(x=10, y=50)

    global feature_name_entry_var
    feature_name_entry_var = tk.StringVar()
    global feature_name_entry
    feature_name_entry = tk.Entry(window_edit_password, textvariable=feature_name_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    feature_name_entry.place(x=130, y=50)
    feature_name_entry_var.set(fe_name)

    note_for_feature_name = tk.Label(window_edit_password, text='Note: Feature name is displayed on the button in the Main window', font=(
        'arial', 10), bg='black', fg='orange')
    note_for_feature_name.place(x=2, y=75)

    save_username = tk.Label(window_edit_password, text='Username', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    save_username.place(x=40, y=100)

    global save_username_entry_var
    save_username_entry_var = tk.StringVar()
    save_username_entry = tk.Entry(window_edit_password, textvariable=save_username_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    save_username_entry.place(x=130, y=100)
    save_username_entry_var.set(pass_username)
    data_user = save_username_entry_var.get()

    copy_image = tk.PhotoImage(file='resources/copy.png')
    copy_user = tk.Button(window_edit_password, image=copy_image, relief='groove',command=lambda: copy_data(data_user))
    copy_user.place(x=320, y=100)

    save_password = tk.Label(window_edit_password, text='Password', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    save_password.place(x=40, y=130)

    global save_password_entry_var
    save_password_entry_var = tk.StringVar()
    save_password_entry = tk.Entry(window_edit_password, textvariable=save_password_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20, show = "*")
    save_password_entry.place(x=130, y=130)
    save_password_entry_var.set(pass_password)
    data_password = save_password_entry_var.get()

    copy_password = tk.Button(window_edit_password, image=copy_image, relief='groove', command=lambda: copy_data(data_password))
    copy_password.place(x=320, y=130)

    ref_1_label = tk.Label(window_edit_password, text='Reference - 1', font=(
        'arial', 12, 'bold'), bg='black', fg='#FFB6C1')
    ref_1_label.place(x=20, y=160)

    global ref_1_entry_var
    ref_1_entry_var = tk.StringVar()
    ref_1_entry = tk.Entry(window_edit_password, textvariable=ref_1_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    ref_1_entry.place(x=130, y=160)
    ref_1_entry_var.set(ref_1)
    data_ref_1 = ref_1_entry_var.get()

    copy_ref_1 = tk.Button(window_edit_password, image=copy_image, relief='groove', command=lambda: copy_data(data_ref_1))
    copy_ref_1.place(x=320, y=160)

    ref_2_label = tk.Label(window_edit_password, text='Reference - 2', font=(
        'arial', 12, 'bold'), bg='black', fg='#61f2ff')
    ref_2_label.place(x=20, y=190)

    global ref_2_entry_var
    ref_2_entry_var = tk.StringVar()
    ref_2_entry = tk.Entry(window_edit_password, textvariable=ref_2_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    ref_2_entry.place(x=130, y=190)
    ref_2_entry_var.set(ref_2)
    data_ref_2 = ref_2_entry_var.get()

    copy_ref_2 = tk.Button(window_edit_password, image=copy_image, relief='groove', command=lambda: copy_data(data_ref_2))
    copy_ref_2.place(x=320, y=190)

    save_button = tk.Button(window_edit_password, text='Save', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command = lambda: get_data(username, button_name))
    save_button.place(x=30, y=250)
    save_button.bind('<Enter>', entered_storage_save_button)
    save_button.bind('<Leave>', leave_storage_save_button)

    clear_button = tk.Button(window_edit_password, text='Clear', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=clear)
    clear_button.place(x=180, y=250)
    clear_button.bind('<Enter>', entered_storage_clear_button)
    clear_button.bind('<Leave>', leave_storage_clear_button)

    exit_button = tk.Button(window_edit_password, text='Exit', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=exit)
    exit_button.place(x=330, y=250)
    exit_button.bind('<Enter>', entered_storage_exit_button)
    exit_button.bind('<Leave>', leave_storage_exit_button)

    window_edit_password.mainloop()
