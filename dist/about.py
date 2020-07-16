"""This module manages the UI of the About window"""
import tkinter as tk
import webbrowser as wb

def redirect():
    """This function redirects to my blog"""
    wb.open('https://appsbypranav.blogspot.com')

def exit_window():
    """This function closes the About window"""
    window_about.destroy()

def open_window():
    """This function runs the UI of the About window"""

    def entered_blog(event):
        view_blog.configure(bg = 'pink')

    def leave_blog(event):
        view_blog.configure(bg = 'light blue')

    def entered_exit(event):
        exit_button.configure(bg = 'pink')

    def leave_exit(event):
        exit_button.configure(bg = 'light blue')


    global window_about
    window_about = tk.Toplevel()
    window_about.title('About')
    window_about.geometry('600x300')
    window_about.configure(bg = 'black')
    window_about.resizable(False, False)
    window_about.iconbitmap('resources/icon.ico')

    heading = tk.Label(window_about, text = 'About Me', font=(
                        'georgia', 24, 'bold'), bg='black', fg='orange')
    heading.pack()

    my_img = tk.PhotoImage(file = 'resources/my_image.png')
    my_label = tk.Label(window_about, image = my_img, bg = 'black')
    my_label.place(x = 5, y = 50)


    my_text = tk.Text(window_about, bg = 'black', fg = 'white',font = ('georgia',11), height = 10, width = 50, relief = 'flat')
    my_text.place(x=190, y=50)
    text ='''Hello Everyone!
I am Pranav and I have developed this Project - Password
Manager. Hope you like it and enjoy using it in your
daily life and make your life comfortable. If you want to
give me any suggestions you can contact me from the given
mail below. If you want to see more of my work please visit
my blog.That's it keep going...'''
    my_text.insert(tk.END, text)

    email = tk.Label(window_about, text = 'Email:', bg = 'black', fg = 'light green', font = ('arial',10))
    email.place(x = 200, y = 190)

    email_info = tk.Text(window_about, bg = 'black', font = ('times new roman',12,'underline'), fg = 'light blue',
                         relief = 'flat', height = 3, width = 25)
    email_info.place(x = 240, y = 187 )
    email_info.insert(tk.END, 'pranav.techiegeek@gmail.com')

    view_blog = tk.Button(window_about, text = 'View My Blog', bg = 'light blue',relief = 'groove',
                          font = ('georgia',12,'bold'), command = redirect)
    view_blog.place(x = 360, y = 250)
    view_blog.bind("<Enter>",entered_blog)
    view_blog.bind("<Leave>",leave_blog)

    exit_button = tk.Button(window_about, text = 'Exit', bg = 'light blue',relief = 'groove',
                          font = ('georgia',12,'bold'), width = 6, command = exit_window)
    exit_button.place(x = 490, y = 250)
    exit_button.bind("<Enter>",entered_exit)
    exit_button.bind("<Leave>",leave_exit)

    window_about.focus_force()
    window_about.mainloop()
