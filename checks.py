
from ui import print_message

START_HOUR = 0
END_HOUR = 1
TITLE = 2

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
    return int(hour)            

def search_in_between(hour, schedule):
        for i in range(len(schedule)):
            if hour >  schedule[i][START_HOUR] and hour < schedule[i][END_HOUR]:
                return True
        return False         

def search_for_me(element, datatype, schedule):
    
    for i in range(len(schedule)):
        if schedule[i][datatype] == element:
            return True
    return False        

def check_hour_combined(hour,datatype, schedule):

    hour_modif = check_valid_hour(hour)

    if hour_modif == False:
        print_message('Unparsable input!\n')
        return hour_modif

    else:
        if search_for_me(hour_modif,datatype, schedule) == False:
            if search_in_between(hour_modif,schedule) == True:
                if datatype == START_HOUR:
                    print_message('Meeting start time overlaping with another meeting, try again.\n')
                return False
            else:
                return hour_modif    

        else:
            if datatype == START_HOUR:
                print_message('There is already a meeting starting at that time, try again.\n')
                return False        