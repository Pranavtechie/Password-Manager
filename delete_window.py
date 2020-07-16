"""This module manages the UI of the Delete User window"""
import tkinter as tk
import about
import back_end

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
        back_end.delete_account(filled_username, pw1, pw2)

    def exit_window(self):
        """This window is called when exit button is pressed and
    closes the window and exiting the application"""
        self.window_delete.destroy()

    @staticmethod
    def open_about():
        about.About_Window()
