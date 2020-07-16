"""This module manages the UI of the About window"""
import tkinter as tk
import webbrowser as wb

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







