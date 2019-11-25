START_HOUR = 0
END_HOUR = 1
TITLE = 2
def check_create_file(filename):
    try:
         with open(filename) as filename:
             pass
    except:
        with open(filename, 'w') as filename:
            pass

def read_from_file(filename):
    check_create_file(filename)
    with open(filename,'r') as schedule_text:
        schedule = schedule_text.readlines()
    for elem in range(len(schedule)):
        schedule[elem] = schedule[elem].rstrip().split(',')
    for elem in range(len(schedule)):
        schedule[elem][START_HOUR] = int(schedule[elem][START_HOUR])    
        schedule[elem][END_HOUR] = int(schedule[elem][END_HOUR])    
    return schedule

def write_to_file(schedule,filename):
    with open(filename, 'w') as schedule_text:
        for elem in range(len(schedule)):
            schedule_text.writelines('{},{},{}\n'.format(schedule[elem][START_HOUR], schedule[elem][END_HOUR], schedule[elem][TITLE]))
