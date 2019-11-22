

def check_menu_option(input_option):
    list_of_options = ['s', 'c', 'v', 'q']
    if input_option not in list_of_options:
        return False
    return True

def check_valid_hour(hour):
    digs = ['1' , '2' , '3', '4', '5', '6', '7', '8', '9', '0']
    if hour.startswith('0') == True and len(hour) > 1:
        return False
    else:    
        for char in hour:
            if char not in digs:
                return False
    return True            

def check_valid_range(hour_start, hour_end):
    pass
