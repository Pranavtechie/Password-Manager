"""This module manages the UI of the Delete User window"""
import tkinter as tk
import about
import back_end

def delete_user(filled_username):
    """This function executes when delete account button is pressed
It takes back to the back_end and evaluates password and delete your account
if the password entered is matched"""
    pw1 = password_entry_var.get()
    pw2 = retype_password_entry_var.get()
    back_end.delete_account(filled_username, pw1, pw2)



def clear():
    """This function is called when clear button is pressed
and it clears the inputs in the window"""
    password_entry_var.set('')
    retype_password_entry_var.set('')
    password_entry.focus()

def exit_window():
    """This window is called when exit button is pressed and
closes the window and exiting the application"""
    window_delete.destroy()

def open_window(username):
    """This function runs the UI of the Delete Window"""

    def entered_delete_button(event):
        delete_button.configure(bg = 'light green', fg = 'red')

    def leave_delete_button(event):
        delete_button.configure(bg = 'red', fg = 'light green')

    def entered_clear_button(event):
        clear_button.configure(bg='#a3ffb3')

    def leave_clear_button(event):
        clear_button.configure(bg='#f1f5e0')

    def entered_exit_button(event):
        exit_button.configure(bg='#a3ffb3')

    def leave_exit_button(event):
        exit_button.configure(bg='#f1f5e0')

    """This function runs the UI of the Delete User window"""
    global window_delete
    window_delete = tk.Tk()
    window_delete.title("Delete users's Account")
    window_delete.resizable(False, False)
    window_delete.geometry('460x290')
    window_delete.configure(bg='black')
    window_delete.iconbitmap('resources/icon.ico')

    heading = tk.Label(window_delete, text = 'Delete Your Account',
                        font = ('arial', 20, 'bold'), bg = 'black', fg = 'orange')
    heading.pack()

    background = tk.PhotoImage(file='resources/line.png')
    background_image = tk.Label(window_delete, image=background,
                                bg='black')
    background_image.place(x=5, y=180)

    about_image = tk.PhotoImage(file='resources/about.png')
    about_icon = tk.Button(window_delete, image=about_image, bg='black', fg='white', relief='flat',
                           command=about.open_window)
    about_icon.place(x=425, y=0)

    sorry_img = tk.PhotoImage(file = "resources/sorry.png")
    sorry = tk.Label(window_delete, text = '  We are sorry to see you go' , image = sorry_img, compound = 'left',
                     bg = 'black', fg = 'white', font = ('Maiandra GD',14))
    sorry.place(x = 100, y = 40)

    note = tk.Label(window_delete, font=('arial', 12),
                    text="Note: You cannot recover your account once deleted",
                    bg='black', fg='orange')
    note.place(x=2, y=100)

    password = tk.Label(window_delete, text='Password', font=(
                        'timesnewroman', 12), bg='black', fg='white')
    password.place(x=62, y=140)

    global password_entry_var, password_entry
    password_entry_var = tk.StringVar()
    password_entry = tk.Entry(window_delete,font=('arial', 12), show = '*',
                              bg='#C0C0C0',textvariable = password_entry_var)
    password_entry.place(x = 140, y = 140)
    
    retype_password = tk.Label(window_delete, text = 'Retype Password',font=(
                        'timesnewroman', 12), bg='black', fg='white')
    retype_password.place(x = 10, y = 170)
    
    global retype_password_entry_var 
    retype_password_entry_var = tk.StringVar()
    retype_password_entry = tk.Entry(window_delete,font=('arial', 12),show = '*',
                              bg='#C0C0C0',textvariable = retype_password_entry_var)
    retype_password_entry.place(x = 140, y = 170)

    delete_button = tk.Button(window_delete, text='Delete your Account', font=(
        'consolas', 13, 'bold'), relief='groove', width=20, bg='red', fg = 'light green', command = lambda: delete_user(username))
    delete_button.place(x=20, y=240)
    delete_button.bind('<Enter>', entered_delete_button)
    delete_button.bind('<Leave>', leave_delete_button)

    clear_button = tk.Button(window_delete, text='Clear', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=clear)
    clear_button.place(x=240, y=240)
    clear_button.bind('<Enter>', entered_clear_button)
    clear_button.bind('<Leave>', leave_clear_button)

    exit_button = tk.Button(window_delete, text='Exit', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=exit_window)
    exit_button.place(x=350, y=240)
    exit_button.bind('<Enter>', entered_exit_button)
    exit_button.bind('<Leave>', leave_exit_button)

    window_delete.focus_force()
    window_delete.mainloop()
