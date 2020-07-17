"""This module manages the complete backend for the Software - Password Manager"""
import sqlite3 as sq
from tkinter import messagebox as msgb
import login
import main_window
import hashlib as hl
from sqlite3 import Error
import sign_up
import delete_window
import address_edit
import payment_edit
import password_edit

def check_username_for_signup(username):
    """This function checks whether given username exists or not"""
    conn = sq.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(username) FROM users_data')
    count = cursor.fetchone()
    count = count[0]

    cursor.execute('SELECT username FROM users_data;')
    database_usernames = cursor.fetchall()


    username_list = []
    for i in range(count):
        var = database_usernames[i][0]
        if var not in username_list:
            username_list.append(var)

    conn.commit()
    conn.close()

    if username not in username_list:
        return True

    else:
        return False



def insert_data(f_name, l_name, username, password, q_1, a_1, q_2, a_2):
    """This functions Signs Up the user for the use of the program"""
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()

    if q_1[-1] != '?':
        q_1 = q_1 + '?'

    if q_2[-1] != '?':
        q_2 = q_2 + '?'
    try:
        conn = sq.connect('database.db')
        cursor = conn.cursor()

        my_string = hl.sha256(password.encode('utf-8'))
        hash_password = my_string.hexdigest()

        string_1 = hl.sha256(a_1.encode('utf-8'))
        answer_1 = string_1.hexdigest()

        string_2 = hl.sha256(a_2.encode('utf-8'))
        answer_2 = string_2.hexdigest()

        sql = ("""INSERT INTO users_data 
                    (username, password, first_name, last_name, question_1, answer_1, question_2, answer_2)
                    VALUES (?,?,?,?,?,?,?,?)""")
        data = (username, hash_password, f_name, l_name, q_1, answer_1, q_2, answer_2)
        cursor.execute(sql, data)

        sql_1 = f"CREATE TABLE {username}_password (val_no text, fe_name text, username text, password text, ref_1 text, ref_2 text)"
        cursor.execute(sql_1)

        sql_2 = f"CREATE TABLE {username}_payment (val_no text, fe_name text, card_number integer, name_on_card text, expiry_date text, username text , password text)"
        cursor.execute(sql_2)

        sql_3 = f"CREATE TABLE {username}_address (val_no text, fe_name text, line_1 text, line_2 text, city text, district text, state text ,pin_code integer)"
        cursor.execute(sql_3)

        copy_1 = f"INSERT INTO {username}_password SELECT * FROM copy_password"
        cursor.execute(copy_1)

        copy_2 = f"INSERT INTO {username}_payment SELECT * FROM copy_payment"
        cursor.execute(copy_2)

        copy_3 = f"INSERT INTO {username}_address SELECT * FROM copy_address"
        cursor.execute(copy_3)

        conn.commit()
        conn.close()
        msgb.showinfo('Success Sign Up', 'You have successfully Signed Up')
        sign_up.enter_login_page()

    except Error as e:
        print(e)

def delete_account(usr, pw1, pw2):
    """This function checks whether the given passwords in the delete window are Correct
and if evaluated True the account and its tables are deleted"""
    global cred
    conn = sq.connect('database.db')
    cursor = conn.cursor()
    try:
        sql = f"SELECT password FROM users_data WHERE username = '{usr}'"
        out = cursor.execute(sql)
        cred = out.fetchone()
        cred = cred[0]


    except Error as e:
        print(e)

    if pw1 == pw2:

        val = hl.sha256(pw1.encode('UTF-8'))
        password = val.hexdigest()


        if password == cred:
            try:
                sequel = f"DELETE FROM users_data where username = '{usr}'"
                cursor.execute(sequel)

                sequel_1 = f"DROP TABLE {usr}_password"
                cursor.execute(sequel_1)

                sequel_2 = f"DROP TABLE {usr}_address"
                cursor.execute(sequel_2)

                sequel_3 = f"DROP TABLE {usr}_payment"
                cursor.execute(sequel_3)

                msgb.showinfo('Success', 'You have successfully deleted you account we are sorry to see you go')

                delete_window.window_delete.destroy()
                login.open_window()
            except Error as e:
                print(e)

        else:
            msgb.showerror('Error while deleting Account', 'The password is incorrect. Try Again')

    else:
        msgb.showerror('Error while deleting Account','The passwords entered do not match please re-enter')

    conn.commit()
    conn.close()










def update_address_data(username, button_value,fe_name, add_1, add_2,town, district, state, pin):
    """This function updates the data in the address table in database"""
    conn = sq.connect('database.db')
    cursor = conn.cursor()

    update = f"""UPDATE {username}_address set fe_name = "{fe_name}",     
            line_1 = "{add_1}",
            line_2 = "{add_2}" ,
            city = "{town}",
            district = "{district}",
            state = "{state}",
            pin_code = "{pin}"
            WHERE val_no = "{button_value}" """
    cursor.execute(update)

    msgb.showinfo('Success', 'You have successfully update the data')


    conn.commit()
    conn.close()

    main_window.change_the_address_box_name(username)
    address_edit.window_edit_address.destroy()


def update_payment_data(username, button_value,fe_name, card_number, name_on_card, expiry_date, pay_username, pay_password):
    """This function updates the payment data to the database"""
    conn = sq.connect('database.db')
    cursor = conn.cursor()

    try:
        update_payment = f"""UPDATE {username}_payment set fe_name = "{fe_name}",     
                card_number = "{card_number}",
                name_on_card = "{name_on_card}" ,
                expiry_date = "{expiry_date}",
                username = "{pay_username}",
                password = "{pay_password}"
                WHERE val_no = "{button_value}" """

        cursor.execute(update_payment)

        msgb.showinfo('Success', 'You have successfully update the data')

    except Error as e:
        print(e)

    conn.commit()
    conn.close()

    main_window.change_the_payment_box_name(username)
    payment_edit.window_edit_payment.destroy()


def update_password_data(username, button_value,fe_name,pass_username,pass_password, ref_1, ref_2):
    """This function updates the data to the database"""
    conn = sq.connect('database.db')
    cursor = conn.cursor()

    update = f"""UPDATE {username}_password set fe_name = "{fe_name}",     
            username = "{pass_username}",
            password = "{pass_password}" ,
            ref_1 = "{ref_1}",
            ref_2 = "{ref_2}"
            WHERE val_no = "{button_value}" """
    cursor.execute(update)

    msgb.showinfo('Success', 'You have successfully update the data')


    conn.commit()
    conn.close()

    main_window.change_the_password_box_name(username)
    password_edit.window_edit_password.destroy()