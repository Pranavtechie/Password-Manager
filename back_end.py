
import sqlite3 as sq

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