from ui import print_message, show_schedule
from checks import check_hour_combined, check_duration, check_end_hour_combined

START_HOUR = 0
END_HOUR = 1
def dummy_return_list():
    return [[9,10,'Meeting_A'],[11,13,'Presentation'],[14,16,'Ending']]
dummy_schedule = dummy_return_list()    
def kill():
    print_message('Exiting...')
    quit()

def schedule_meeting(schedule):
    print_message('Schedule a new meeting.')
    title = get_input('Meeting Title: ')
    start_hour = handle_hour()
       
    start_hour = int(start_hour)
    duration = handle_duration()
    end_hour = start_hour + duration
    while check_end_hour_combined(end_hour, END_HOUR, dummy_schedule) == None:
        duration = handle_duration()
        end_hour = start_hour + duration
    print_message('\nNew Meeting Created: {startHour} - {endHour} {Title}\n'.format(startHour = start_hour, 
                                                                                    endHour = end_hour, 
                                                                                    Title = title))    
    dummy_schedule.append([start_hour, end_hour, title])

def cancel_meeting(schedule):
    print_message('Cancel a meeting.')

def view_meeting(schedule):
    schedule = sort_schedule(schedule)
    show_schedule(schedule)
    
def sort_schedule(schedule):
    schedule = sorted(schedule, key = lambda x: x[START_HOUR])
    return schedule

def get_input(prompt):
    option = input(prompt)

    return option

def handle_option(option):

    option_handler = {'s' : schedule_meeting, 'c' : cancel_meeting, 'v' : view_meeting, 'q' : kill}

    if option == 'q':
        return option_handler[option]()
    return option_handler[option](dummy_schedule)

def handle_duration():
    duration = get_input('Meeting Duration: ')
    while check_duration(duration)  == None:
        duration = get_input('Meeting Duration: ')
    print_message('\n')
    duration = int(duration) 
    return duration   

def handle_hour():
    start_hour = get_input('Start Hour: ')

    while check_hour_combined(start_hour,START_HOUR, dummy_schedule) == None:
       start_hour = get_input('Start Hour: ')  
    print_message('\n')
    return int(start_hour)  