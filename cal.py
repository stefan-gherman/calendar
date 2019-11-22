from storage import *
from ui import *
from checks import *
from backend import *

def main():
    show_menu()
    option = get_input()

    while check_menu_option(option) is False:
        print_message('Option is not available!')
        option = get_input()


if __name__ == "__main__":
    main()
    dummy_schedule = [[8,10,'Meeting_1'], [10,12,'Sales Pitch']]
    show_schedule(dummy_schedule)