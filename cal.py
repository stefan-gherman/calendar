from storage import *
from ui import *
from checks import *
from backend import *

def main():
    show_menu()
    option = get_input('Your Choice: ')

    while check_menu_option(option) is False:
        print_message('Option is not available!')
        option = get_input('Your Choice: ')
    print_message('\n')
    handle_option(option)

if __name__ == "__main__":
    print('\033c')
    while True:
        main()
