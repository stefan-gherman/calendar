from ui import print_message, show_schedule
from checks import check_hour_combined

def dummy_return_list():
    return [[9,10,'Meeting_A'],[11,13,'Presentation'],[14,16,'Ending']]
dummy_schedule = dummy_return_list()    
def kill():
    print_message('Exiting...')
    quit()

def schedule_meeting(schedule):
    START_HOUR = 0
    END_HOUR = 1
    print_message('Schedule a new meeting')
    title = get_input('Meeting Title: ')
    start_hour = get_input('Start Hour: ')

    while check_hour_combined(start_hour,START_HOUR, dummy_schedule) == False:
       start_hour = get_input('Start Hour: ')
       
    start_hour = int(start_hour) 
       
def cancel_meeting(schedule):
    pass

def view_meeting(schedule):
    show_schedule(schedule)
    

def get_input(prompt):
    option = input(prompt)

    return option

def handle_option(option):

    option_handler = {'s' : schedule_meeting, 'c' : cancel_meeting, 'v' : view_meeting, 'q' : kill}

    if option == 'q':
        return option_handler[option]()
    return option_handler[option](dummy_schedule)