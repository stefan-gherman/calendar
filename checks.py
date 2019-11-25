
from ui import print_message

START_HOUR = 0
END_HOUR = 1
TITLE = 2

def check_menu_option(input_option):
    list_of_options = ['s', 'c', 'v','m','cm','t','q']
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

def search_in_between(hour, schedule, datatype):
        for i in range(len(schedule)):
            if datatype == START_HOUR:
                if hour >  schedule[i][START_HOUR] and hour < schedule[i][END_HOUR]:
                    return True
            else:
                if hour >  schedule[i][START_HOUR] and hour <= schedule[i][END_HOUR]:
                    return True        
        return False         

def search_for_me(element, datatype, schedule):
    
    for i in range(len(schedule)):
        if schedule[i][datatype] == element:
            return True,i
    return False        
def check_hour_in_working_time(hour,datatype):
    if datatype == START_HOUR:
        if hour < 8 or hour >= 18:
            return False
    else:
         if hour < 8 or hour > 18:
            return False        
    return True    


def check_hour_combined(hour,datatype, schedule):

    hour_modif = check_valid_hour(hour)

    if hour_modif == None:
        print_message('Unparsable input!\n')
        return hour_modif

    else:
        if search_for_me(hour_modif,datatype, schedule) == False:
            if search_in_between(hour_modif,schedule,START_HOUR) == True:
                if datatype == START_HOUR:
                    print_message('Meeting start time overlaping with another meeting, try again.\n')
                return None
            else:
                if check_hour_in_working_time(hour_modif,datatype) == False:
                    print_message('Starting time is outside working hours, try again.\n')
                    return None
                else:
                    return hour_modif    

        else:
            if datatype == START_HOUR:
                print_message('There is already a meeting starting at that time, try again.\n')
                return None

def check_end_hour_combined(hour, datatype, schedule):
    if check_hour_in_working_time(hour,datatype) == False:
        print_message('Meeting extends beyond working time. Try adjusting the duration.\n')
        return None
    if search_in_between(hour,schedule,END_HOUR) == True:
        if datatype == END_HOUR:
            print_message('Ending hour overlaps with another meeting, try changing the duration.\n')
            return None
    else:
        return hour        


def check_cancel_hour(hour,datatype,schedule):

    if check_valid_hour(hour) == None:
        print_message('Unparsable Data.\n')
        return None
    else:
        hour = check_valid_hour(hour)
        if search_for_me(hour, datatype, schedule) == False:
            print_message('No meeting starting at this hour, try again.\n')
            return None
        else:
            i = search_for_me(hour,datatype,schedule)
        
            return i[1]   