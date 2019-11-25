from ui import print_message, show_schedule
from checks import check_hour_combined, check_duration, check_end_hour_combined, check_cancel_hour, search_for_me
from storage import write_to_file, read_from_file

START_HOUR = 0
END_HOUR = 1
TITLE = 2
filename = 'meetings.txt'
schedule = read_from_file(filename)  
def kill():
    print_message('Exiting...')
    quit()

def scheduler(schedule,pop_index = None):
    if pop_index != None:
        schedule.pop(pop_index)
    title = get_input('Meeting Title: ')
    start_hour = handle_hour()
    start_hour = int(start_hour)
    duration = handle_duration()
    end_hour = start_hour + duration
    while check_end_hour_combined(end_hour, END_HOUR, schedule) == None:
        duration = handle_duration()
        end_hour = start_hour + duration
    print_message('\nNew Meeting Created: {startHour} - {endHour} {Title}\n'.format(startHour = start_hour, 
                                                                                        endHour = end_hour, 
                                                                                        Title = title))    
    
    schedule.append([start_hour, end_hour, title])
    schedule = sort_schedule(schedule)
    write_to_file(schedule, filename)

def schedule_meeting(schedule):
    print_message('Schedule a new meeting.')
    scheduler(schedule)

def cancel_meeting(schedule):
    print_message('Cancel a meeting.')
    cancel_hour = get_input('Select Starting Hour: ')

    while check_cancel_hour(cancel_hour, START_HOUR, schedule) == None:
        cancel_hour = get_input('Select Starting Hour: ')

    cancel_hour = int(cancel_hour)
    pop_index = search_for_me(cancel_hour, START_HOUR, schedule)[1]
    schedule.pop(pop_index)
    write_to_file(schedule, filename)
    print_message('Meeting Canceled.\n')

def view_meeting(schedule):
    schedule = sort_schedule(schedule)
    write_to_file(schedule, filename)
    show_schedule(schedule)
    
def sort_schedule(schedule):
    schedule = sorted(schedule, key = lambda x: x[START_HOUR])
    return schedule

def get_input(prompt):
    option = input(prompt)

    return option

def handle_option(option):

    option_handler = {'s' : schedule_meeting, 'c' : cancel_meeting, 'v' : view_meeting, 
    'm': modify_meeting, 't': calculate_total_hrs, 'cm': compact_meeting , 'q' : kill}

    if option == 'q':
        return option_handler[option]()
    return option_handler[option](schedule)

def handle_duration():
    duration = get_input('Meeting Duration: ')
    while check_duration(duration)  == None:
        duration = get_input('Meeting Duration: ')
    print_message('\n')
    duration = int(duration) 
    return duration   

def handle_hour():
    start_hour = get_input('Start Hour: ')

    while check_hour_combined(start_hour,START_HOUR, schedule) == None:
       start_hour = get_input('Start Hour: ')  
    print_message('\n')
    return int(start_hour)  


def calculate_total_hrs(schedule):
    total_hrs = 0
    for i in range(len(schedule)):
        total_hrs += schedule[i][END_HOUR] - schedule[i][START_HOUR]
    print_message('Total Hours of Meeting: {}\n'.format(total_hrs))   

def modify_meeting(schedule):
    print_message('Modify a meeting.')
    modif_hour = get_input('Select Starting Hour: ')     

    while check_cancel_hour(modif_hour, START_HOUR, schedule) == None:
        modif_hour = get_input('Select Starting Hour: ')

    modif_hour = int(modif_hour)
    pop_index = search_for_me(modif_hour, START_HOUR, schedule)[1]
    scheduler(schedule, pop_index)

def compact_meeting(schedule):
    min_start_hour = 8

    for i in range(len(schedule)):
        timespan = schedule[i][END_HOUR] - schedule[i][START_HOUR]
        if schedule[i][START_HOUR] > min_start_hour:
            schedule[i][START_HOUR] = min_start_hour
            schedule[i][END_HOUR] = schedule[i][START_HOUR] + timespan
            min_start_hour = schedule[i][END_HOUR]

    show_schedule(schedule)        

