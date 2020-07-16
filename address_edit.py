"""This module manages the UI of the Address Edit window"""
import tkinter as tk
import about
import back_end
import pyperclip as pc

class Address_Window(object):

    def __init__(self,username, button_name,fe_name,address_1, address_2, town, district,state, pin):
        """This __init__ method is to defines the Address Window elements and strings from database"""
        self.username = username
        self.button_name = button_name
        self.fe_name = fe_name
        self.address_1 = address_1
        self.address_2 = address_2
        self.town = town
        self.district = district
        self.state = state
        self.pin = pin

        if (self.address_1 is None and self.address_2 is None and self.town is None and self.district is None and
            self.state is None and self.pin is None) and self.fe_name == "empty":
            """This condition is to set the variables to empty is database return None"""
            self.fe_name = 'empty'
            self.address_1 = ''
            self.address_2 = ''
            self.town = ''
            self.district = ''
            self.state = ''
            self.pin = ''

        else:
            pass

        self.window_edit_address = tk.Toplevel()
        self.window_edit_address.title('Store your address')
        self.window_edit_address.geometry('475x350')
        self.window_edit_address.resizable(False, False)
        self.window_edit_address.configure(bg='black')
        self.window_edit_address.iconbitmap('resources/icon.ico')
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
        self.background_image = tk.Label(self.window_edit_address, image=self.background,
                                    bg='black')
        self.background_image.place(x=5, y=240)

        self.heading = tk.Label(self.window_edit_address, text='Store your Information Safely',
                           font=('arial', 20, 'bold'), bg='black', fg='orange')
        self.heading.pack()

        self.about_image = tk.PhotoImage(file='resources/about.png')
        self.about_icon = tk.Button(self.window_edit_address, image=self.about_image, bg='black', fg='white', relief='flat',
                               command=lambda: about.About_Window())
        self.about_icon.place(x=440, y=0)

        self.feature_name = tk.Label(self.window_edit_address, text='Feature Name', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.feature_name.place(x=10, y=50)

        self.feature_name_entry_var = tk.StringVar()
        self.feature_name_entry = tk.Entry(self.window_edit_address, textvariable=self.feature_name_entry_var, font=(
                                            'arial', 12), bg='#C0C0C0', width=20)
        self.feature_name_entry.place(x=130, y=50)
        self.feature_name_entry_var.set(self.fe_name)
        self.feature_name_entry.focus()

        self.note_for_feature_name = tk.Label(self.window_edit_address,
                                    text='Note: Feature name is displayed on the button in the Main window', font=(
                                    'arial', 10), bg='black', fg='orange')
        self.note_for_feature_name.place(x=2, y=75)

        self.address_line_1 = tk.Label(self.window_edit_address, text='Address Line 1', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.address_line_1.place(x=5, y=100)

        self.address_line_1_entry_var = tk.StringVar()
        self.address_line_1_entry = tk.Entry(self.window_edit_address, textvariable=self.address_line_1_entry_var,
                                             font=('arial', 12), bg='#C0C0C0', width=30)
        self.address_line_1_entry.place(x=130, y=100)
        self.address_line_1_entry_var.set(self.address_1)
        self.data_add_1 = self.address_line_1_entry_var.get()

        self.copy_image = tk.PhotoImage(file='resources/copy.png')
        self.copy_add_1 = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                               command=lambda: self.copy_data(data_add_1))
        self.copy_add_1.place(x=410, y=100)

        self.address_line_2 = tk.Label(self.window_edit_address, text='Address Line 2', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.address_line_2.place(x=5, y=125)

        self.address_line_2_entry_var = tk.StringVar()
        self.address_line_2_entry = tk.Entry(self.window_edit_address, textvariable=self.address_line_2_entry_var,
                                             font=('arial', 12), bg='#C0C0C0', width=30)
        self.address_line_2_entry.place(x=130, y=125)
        self.address_line_2_entry_var.set(self.address_2)
        self.data_add_2 = self.address_line_2_entry_var.get()

        self.copy_add_2 = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                               command=lambda: self.copy_data(self.data_add_2))
        self.copy_add_2.place(x=410, y=125)

        self.town_label = tk.Label(self.window_edit_address, text='Town/City', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.town_label.place(x=40, y=150)

        self.town_entry_var = tk.StringVar()
        self.town_entry = tk.Entry(self.window_edit_address, textvariable=self.town_entry_var, font=(
            'arial', 12), bg='#C0C0C0', width=20)
        self.town_entry.place(x=130, y=150)
        self.town_entry_var.set(self.town)
        self.town_data = self.town_entry_var.get()

        self.copy_town = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                              command=lambda: self.copy_data(self.town_data))
        self.copy_town.place(x=320, y=150)

        self.district_label = tk.Label(self.window_edit_address, text='District', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.district_label.place(x=60, y=175)

        self.district_entry_var = tk.StringVar()
        self.district_entry = tk.Entry(self.window_edit_address, textvariable=self.district_entry_var,
                                  font=('arial', 12), bg='#C0C0C0', width=20)
        self.district_entry.place(x=130, y=175)
        self.district_entry_var.set(self.district)
        self.data_district = self.district_entry_var.get()

        self.copy_district = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                                  command=lambda: self.copy_data(self.data_district))
        self.copy_district.place(x=320, y=175)

        self.state_label = tk.Label(self.window_edit_address, text='State', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.state_label.place(x=75, y=200)

        self.state_entry_var = tk.StringVar()
        self.state_entry = tk.Entry(self.window_edit_address, textvariable=self.state_entry_var,
                               font=('arial', 12), bg='#C0C0C0', width=20)
        self.state_entry.place(x=130, y=200)
        self.state_entry_var.set(self.state)
        self.data_state = self.state_entry_var.get()

        self.copy_state = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                               command=lambda: self.copy_data(self.data_state))
        self.copy_state.place(x=320, y=200)

        self.pin_label = tk.Label(self.window_edit_address, text='Pin Code', font=(
            'arial', 12, 'bold'), bg='black', fg='white')
        self.pin_label.place(x=45, y=225)

        self.pin_code_entry_var = tk.StringVar()
        self.pin_code_entry = tk.Entry(self.window_edit_address, textvariable=self.pin_code_entry_var,
                                  font=('arial', 12), bg='#C0C0C0', width=20)
        self.pin_code_entry.place(x=130, y=225)
        self.pin_code_entry_var.set(self.pin)
        self.data_pin = self.pin_code_entry_var.get()

        self.copy_pin = tk.Button(self.window_edit_address, image=self.copy_image, relief='groove',
                             command=lambda: copy_data(data_pin))
        self.copy_pin.place(x=320, y=225)

        self.save_button = tk.Button(self.window_edit_address, text='Save', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0',
                                command=lambda: self.get_data(self.username, self.button_name))
        self.save_button.place(x=30, y=300)
        self.save_button.bind('<Enter>', self.entered_storage_save_button)
        self.save_button.bind('<Leave>', self.leave_storage_save_button)

        self.clear_button = tk.Button(self.window_edit_address, text='Clear', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.clear)
        self.clear_button.place(x=180, y=300)
        self.clear_button.bind('<Enter>', self.entered_storage_clear_button)
        self.clear_button.bind('<Leave>', self.leave_storage_clear_button)

        self.exit_button = tk.Button(self.window_edit_address, text='Exit', font=(
            'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=self.exit_window)
        self.exit_button.place(x=330, y=300)
        self.exit_button.bind('<Enter>', self.entered_storage_exit_button)
        self.exit_button.bind('<Leave>', self.leave_storage_exit_button)

        self.window_edit_address.focus_force()
        self.window_edit_address.mainloop()

    def get_data(self, username, button_value):
        """This method collects the data to update the database"""
        fe_name = self.feature_name_entry_var.get()
        add_1 = self.address_line_1_entry_var.get()
        add_2 = self.address_line_2_entry_var.get()
        town_var = self.town_entry_var.get()
        district_var = self.district_entry_var.get()
        state_var = self.state_entry_var.get()
        pin_var = self.pin_code_entry_var.get()

        back_end.update_address_data(username, button_value, fe_name, add_1, add_2, town_var, district_var, state_var,
                                     pin_var)

    @staticmethod
    def copy_data(text):
        """This method copies the selected data to the clipboard"""
        pc.copy(text)

    def exit_window(self):
        """This method exits Address Window"""
        self.window_edit_address.destroy()

    def clear(self):
        """ Clears all the input in the window"""
        self.feature_name_entry_var.set('empty')
        self.address_line_1_entry_var.set('')
        self.address_line_2_entry_var.set('')
        self.town_entry_var.set('')
        self.district_entry_var.set('')
        self.state_entry_var.set('')
        self.pin_code_entry_var.set('')
        self.feature_name_entry.focus()
