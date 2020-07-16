"""This module is not used in the software but is a separate file"""

def encrypt_string(string,specific_value):
    """This function takes a string and specific_value(integer) and encrypts the data
according to the specific_value in the unicode format"""

    new_str = ""
    val = ord(chr(specific_value))

    for i in string:
        variable = chr(ord(i) + val)
        small = f"{variable}"
        new_str = new_str + small

    return specific_value, new_str


def decrypt_string(key, string):
    """This function decrypts the string the by taking the key which was used to encrypt the string"""
    d_string = f""
    val = ord(chr(key))

    for i in string:
        variable = chr(ord(i) - val)
        small = f"{variable}"
        d_string = d_string + small

    return d_string
