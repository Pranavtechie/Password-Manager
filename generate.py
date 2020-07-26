import random
import string
import tkinter as tk
import pyperclip as pc
import about
from tkinter import messagebox as msgb

class Generate_Window(object):

    def __init__(self):
        """This method defines the Generate Password Window elements"""
        self.window_generate = tk.Toplevel()
        self.window_generate.title('Generate Password')
        self.window_generate.resizable(False, False)
        self.window_generate.configure(bg = 'black')
        self.window_generate.geometry('500x500')
        self.window_generate.iconbitmap("resources/icon.ico")
        self.init_ui()

    def entered_generate_button(self, event):
        self.generate_button.configure(bg='#a3ffb3')

    def leave_generate_button(self, event):
        self.generate_button.configure(bg='#f1f5e0')

    def entered_clear_button(self, event):
        self.clear_button.configure(bg='#a3ffb3')

    def leave_clear_button(self, event):
        self.clear_button.configure(bg='#f1f5e0')

    def entered_exit_button(self, event):
        self.exit_button.configure(bg='#a3ffb3')

    def leave_exit_button(self, event):
        self.exit_button.configure(bg='#f1f5e0')

    def init_ui(self):
        self.heading = tk.Label(self.window_generate, text='Generate Password', font=(
            'arial', 18, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.background = tk.PhotoImage(file='resources/line.png')
        self.background_image = tk.Label(self.window_generate, image=self.background, bg='black')
        self.background_image.place(x=0, y=400)

        self.about_image = tk.PhotoImage(file='resources/about.png')
        self.about_icon = tk.Button(self.window_generate, image=self.about_image, bg='black', fg='white', relief='flat',
                                    command=self.open_about)
        self.about_icon.place(x=470, y=0)

        self.happy_img = tk.PhotoImage(file="resources/happy.png")
        self.happy = tk.Label(self.window_generate, text="Make your password more safer ",
                              image=self.happy_img, compound='right', bg='black', fg='white', font=('Maiandra GD', 14))
        self.happy.place(x=70, y=40)


        self.password_length_label = tk.Label(self.window_generate, text = 'Password Length', font=(
                                              'timesnewroman', 12), bg='black', fg='white')
        self.password_length_label.place(x = 5, y = 120)

        self.password_var = tk.IntVar()
        self.password_length = tk.Spinbox(self.window_generate, from_ = 5, to = 500, textvariable = self.password_var,
                                          width = 4)
        self.password_length.place(x = 140, y = 123)


        self.radio_var = tk.IntVar()
        self.radio_1 = tk.Radiobutton(self.window_generate, text = "(Weaker Password) Only Lowercase Letters", value = 1,
                                      activebackground = 'black', activeforeground = 'white', bg = 'black',
                                      fg = '#ff0000', variable = self.radio_var, font = ('Gabriola',17, 'bold'))
        self.radio_1.place(x = 10, y = 145)

        self.radio_2 = tk.Radiobutton(self.window_generate, text="(Weaker Password) Only Uppercase Letters", value=2,
                                      activebackground='black', activeforeground='white', bg='black', fg='#ff5252',
                                      variable = self.radio_var, font = ('Gabriola',17, 'bold'))
        self.radio_2.place(x=10, y=185)

        self.radio_3 = tk.Radiobutton(self.window_generate, text="(Weak Password) Only Letters", value=3,
                                      activebackground='black', activeforeground='white', bg='black', fg='#f59300',
                                      variable = self.radio_var, font = ('Gabriola',17, 'bold'))
        self.radio_3.place(x=10, y=225)

        self.radio_4 = tk.Radiobutton(self.window_generate, text="(Strong Password) Only Letters and digits", value=4,
                                      activebackground='black', activeforeground='white', bg='black', fg='#a2ff00',
                                      variable = self.radio_var, font = ('Gabriola',17, 'bold'))
        self.radio_4.place(x=10, y=265)

        self.radio_5 = tk.Radiobutton(self.window_generate, text="(Stronger Password) Letters, Digits and Symbols",
                                      value=5, activebackground='black', activeforeground='white', bg='black',
                                      fg='#00a63a',variable = self.radio_var, font = ('Gabriola',17, 'bold'))
        self.radio_5.place(x=10, y=305)

        self.generate_button = tk.Button(self.window_generate, text='Generate', font=(
            'consolas', 13, 'bold'), relief='groove', width=10, bg='#f1f5e0', command= self.generate_the_password)
        self.generate_button.place(x=30, y=460)
        self.generate_button.bind('<Enter>', self.entered_generate_button)
        self.generate_button.bind('<Leave>', self.leave_generate_button)

        self.clear_button = tk.Button(self.window_generate, text = 'Clear', font=(
            'consolas', 13, 'bold'), relief='groove', width=10, bg='#f1f5e0', command= self.clear_data)
        self.clear_button.place(x = 190, y = 460)
        self.clear_button.bind('<Enter>', self.entered_clear_button)
        self.clear_button.bind('<Leave>', self.leave_clear_button)

        self.exit_button = tk.Button(self.window_generate, text = 'Exit', font=(
            'consolas', 13, 'bold'), relief='groove', width=10, bg='#f1f5e0', command= self.exit_window)
        self.exit_button.place(x = 360, y = 460)
        self.exit_button.bind('<Enter>', self.entered_exit_button)
        self.exit_button.bind('<Leave>', self.leave_exit_button)

        self.window_generate.mainloop()

    def exit_window(self):
        self.window_generate.destroy()

    def clear_data(self):
        self.password_var.set(5)
        self.radio_var.set(0)

        try:
            self.show_label.destroy()
            self.show_password.destroy()
            self.copy_button.destroy()

        except:
            pass

    def generate_the_password(self):
        length = self.password_var.get()
        button_val = self.radio_var.get()

        if button_val == 1:
            password = self.generate_1(length)

        elif button_val == 2:
            password = self.generate_2(length)

        elif button_val == 3:
            password = self.generate_3(length)

        elif button_val == 4:
            password = self.generate_4(length)

        elif button_val == 5:
            password = self.generate_5(length)

        else:
            password = 'Sorry an Error Occurred Try Again '

        self.show_label = tk.Label(self.window_generate, text = 'Your Password is :  ',font=(
                                    'timesnewroman', 12), bg='black', fg='white')
        self.show_label.place(x = 5, y = 380)

        self.show_password = tk.Text(self.window_generate, font = ('arial',12), width = 30, height = 1)
        self.show_password.place(x = 150, y = 380)
        self.show_password.insert(tk.END, password)
        self.show_password.config(state = 'disabled')

        self.copy_image = tk.PhotoImage(file='resources/copy.png')
        self.copy_button = tk.Button(self.window_generate, image = self.copy_image, relief='groove',
                                    command = lambda: self.copy_data(password))
        self.copy_button.place(x=430, y=380)


    def copy_data(self, text):
        msgb.showinfo('Success', message = 'You have copied your password successfully')
        pc.copy(text)




    @staticmethod
    def open_about():
        about.About_Window()


    @staticmethod
    def generate_1(length):
        # Random string with the only lower case letters
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @staticmethod
    def generate_2(length):
        # Random string with the only upper case
        letters = string.ascii_uppercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @staticmethod
    def generate_3(length):
        # Random string with the combination of lower and upper case
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @staticmethod
    def generate_4(length):
        # Random string with alphanumeric characters
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        return result_str

    @staticmethod
    def generate_5(length):
        # Random string with alphabets, digits, symbols
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(length))
        return password


