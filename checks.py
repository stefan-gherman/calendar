
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
   
    if check_int(hour) == None:
        return None
    else:
        return int(hour)   

def check_int(string):
    if string.startswith('0') == True and len(string) > 1:
        return None
    digs = ['1' , '2' , '3', '4', '5', '6', '7', '8', '9', '0']
    for char in string:
        if char not in digs:
                return None
    return int(string) 

def check_duration(duration):
    if check_int(duration) == None:
        print_message('Unparsable input.\n')
        return None
    else:
        duration = check_int(duration)
        if duration > 2 or duration < 1:
            print_message('Duration is diferent from 1 or 2. Try again.\n')
            return None
        else:
            return duration            

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

    if hour_modif == None:
        print_message('Unparsable input!\n')
        return hour_modif

    else:
        if search_for_me(hour_modif,datatype, schedule) == False:
            if search_in_between(hour_modif,schedule) == True:
                if datatype == START_HOUR:
                    print_message('Meeting start time overlaping with another meeting, try again.\n')
                return None
            else:
                return hour_modif    

        else:
            if datatype == START_HOUR:
                print_message('There is already a meeting starting at that time, try again.\n')
                return None

def check_end_hour_combined(hour, datatype, schedule):
    if search_in_between(hour,schedule) == True:
        if datatype == END_HOUR:
            print_message('Ending hour overlaps with another meeting, try changing the duration.\n')
            return None
    else:
        return hour        