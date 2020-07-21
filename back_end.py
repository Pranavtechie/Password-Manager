"""This function handles the back-end for the button function"""
import main_window

class Back_End(main_window.Main_Window):

    def __init__(self, got_username):
        super(Back_End, self).__init__()
        self.got_username = got_username

    def address_buttons(self):
        self.change_the_address_box_name(self.got_username)


