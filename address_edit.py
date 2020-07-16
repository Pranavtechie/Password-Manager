"""This module manages the UI of the Address Edit window"""
import tkinter as tk
import about
import back_end
import pyperclip as pc

def copy_data(text):
    """This function copies the selected data to the clipboard"""
    pc.copy(text)

def get_data(username, button_value):
    """This function collects the data to update the database"""
    fe_name = feature_name_entry_var.get()
    add_1 = address_line_1_entry_var.get()
    add_2 = address_line_2_entry_var.get()
    town_var = town_entry_var.get()
    district_var = district_entry_var.get()
    state_var = state_entry_var.get()
    pin_var = pin_code_entry_var.get()

    back_end.update_address_data(username,button_value, fe_name, add_1, add_2,town_var, district_var, state_var, pin_var)


def clear():
    """ Clears all the input in the window"""
    feature_name_entry_var.set('empty')
    address_line_1_entry_var.set('')
    address_line_2_entry_var.set('')
    town_entry_var.set('')
    district_entry_var.set('')
    state_entry_var.set('')
    pin_code_entry_var.set('')
    feature_name_entry.focus()

def exit_window():
    """ Exit the function and closes the program"""
    window_edit_address.destroy()


def open_window(username, button_name,fe_name,address_1, address_2, town, district,state, pin):
    """This function runs the UI of the Address Edit window"""
    if address_1 is None and address_2 is None and town is None and district is None and state is None and pin is None:
        fe_name = ''
        address_1 = ''
        address_2 = ''
        town = ''
        district = ''
        state = ''
        pin = ''

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



    global window_edit_address
    window_edit_address = tk.Toplevel()
    window_edit_address.title('Store your address')
    window_edit_address.geometry('475x350')
    window_edit_address.resizable(False, False)
    window_edit_address.configure(bg='black')
    window_edit_address.iconbitmap('resources/icon.ico')

    background = tk.PhotoImage(file = 'resources/line.png')
    background_image = tk.Label(window_edit_address, image=background,
                                bg='black')
    background_image.place(x=5, y=240)

    heading = tk.Label(window_edit_address, text='Store your Information Safely',
                       font=('arial', 20, 'bold'), bg='black', fg='orange')
    heading.pack()

    about_image = tk.PhotoImage(file='resources/about.png')
    about_icon = tk.Button(window_edit_address, image=about_image, bg='black', fg='white', relief='flat',
                           command=about.open_window)
    about_icon.place(x=440, y=0)

    feature_name = tk.Label(window_edit_address, text='Feature Name', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    feature_name.place(x=10, y=50)

    global feature_name_entry_var, feature_name_entry
    feature_name_entry_var = tk.StringVar()
    feature_name_entry = tk.Entry(window_edit_address, textvariable=feature_name_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    feature_name_entry.place(x=130, y=50)
    feature_name_entry_var.set(fe_name)
    feature_name_entry.focus()

    note_for_feature_name = tk.Label(window_edit_address,
                                    text='Note: Feature name is displayed on the button in the Main window', font=(
                                    'arial', 10), bg='black', fg='orange')
    note_for_feature_name.place(x=2, y=75)


    address_line_1 = tk.Label(window_edit_address, text='Address Line 1', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    address_line_1.place(x=5, y=100)


    global address_line_1_entry_var
    address_line_1_entry_var = tk.StringVar()
    address_line_1_entry = tk.Entry(window_edit_address, textvariable=address_line_1_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=30)
    address_line_1_entry.place(x=130, y=100)
    address_line_1_entry_var.set(address_1)
    data_add_1 = address_line_1_entry_var.get()

    copy_image = tk.PhotoImage(file = 'resources/copy.png')
    copy_add_1 = tk.Button(window_edit_address, image = copy_image, relief = 'groove',command = lambda: copy_data(data_add_1))
    copy_add_1.place(x = 410, y = 100)


    address_line_2 = tk.Label(window_edit_address, text='Address Line 2', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    address_line_2.place(x=5, y=125)

    global address_line_2_entry_var
    address_line_2_entry_var = tk.StringVar()
    address_line_2_entry = tk.Entry(window_edit_address, textvariable=address_line_2_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=30)
    address_line_2_entry.place(x=130, y=125)
    address_line_2_entry_var.set(address_2)
    data_add_2 = address_line_2_entry_var.get()

    copy_add_2 = tk.Button(window_edit_address, image=copy_image, relief='groove',command = lambda: copy_data(data_add_2))
    copy_add_2.place(x=410, y=125)

    town_label = tk.Label(window_edit_address, text='Town/City', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    town_label.place(x=40, y=150)

    global town_entry_var
    town_entry_var = tk.StringVar()
    town_entry = tk.Entry(window_edit_address, textvariable=town_entry_var, font=(
        'arial', 12), bg='#C0C0C0', width=20)
    town_entry.place(x=130, y=150)
    town_entry_var.set(town)
    town_data = town_entry_var.get()

    copy_town = tk.Button(window_edit_address, image=copy_image, relief='groove',command = lambda: copy_data(town_data))
    copy_town.place(x=320, y=150)

    district_label = tk.Label(window_edit_address, text='District', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    district_label.place(x=60, y=175)

    global district_entry_var
    district_entry_var = tk.StringVar()
    district_entry = tk.Entry(window_edit_address, textvariable=district_entry_var,
                              font=('arial', 12), bg='#C0C0C0', width=20)
    district_entry.place(x=130, y=175)
    district_entry_var.set(district)
    data_district = district_entry_var.get()

    copy_district = tk.Button(window_edit_address, image=copy_image, relief='groove',command = lambda: copy_data(data_district))
    copy_district.place(x=320, y=175)

    state_label = tk.Label(window_edit_address, text='State', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    state_label.place(x=75, y=200)

    global state_entry_var
    state_entry_var = tk.StringVar()
    state_entry = tk.Entry(window_edit_address, textvariable=state_entry_var,
                              font=('arial', 12), bg='#C0C0C0', width=20)
    state_entry.place(x=130, y=200)
    state_entry_var.set(state)
    data_state = state_entry_var.get()

    copy_state = tk.Button(window_edit_address, image=copy_image, relief='groove',command = lambda: copy_data(data_state))
    copy_state.place(x=320, y=200)

    pin_label = tk.Label(window_edit_address, text='Pin Code', font=(
        'arial', 12, 'bold'), bg='black', fg='white')
    pin_label.place(x=45, y=225)

    global pin_code_entry_var
    pin_code_entry_var = tk.StringVar()
    pin_code_entry = tk.Entry(window_edit_address, textvariable=pin_code_entry_var,
                           font=('arial', 12), bg='#C0C0C0', width=20)
    pin_code_entry.place(x=130, y=225)
    pin_code_entry_var.set(pin)
    data_pin = pin_code_entry_var.get()

    copy_pin = tk.Button(window_edit_address, image=copy_image, relief='groove',command = lambda: copy_data(data_pin))
    copy_pin.place(x=320, y=225)

    save_button = tk.Button(window_edit_address, text='Save', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command = lambda: get_data(username,button_name))
    save_button.place(x=30, y=300)
    save_button.bind('<Enter>', entered_storage_save_button)
    save_button.bind('<Leave>', leave_storage_save_button)

    clear_button = tk.Button(window_edit_address, text='Clear', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=clear)
    clear_button.place(x=180, y=300)
    clear_button.bind('<Enter>', entered_storage_clear_button)
    clear_button.bind('<Leave>', leave_storage_clear_button)

    exit_button = tk.Button(window_edit_address, text='Exit', font=(
        'consolas', 13, 'bold'), relief='groove', width=8, bg='#f1f5e0', command=exit_window)
    exit_button.place(x=330, y=300)
    exit_button.bind('<Enter>', entered_storage_exit_button)
    exit_button.bind('<Leave>', leave_storage_exit_button)

    window_edit_address.focus_force()
    window_edit_address.mainloop()
