
def print_message(message):
    print(message)


def show_menu():
    line_spacing = 2
    print('Menu:')
    print('\n' + '(s) Schedule a new meeting' + '\n' * line_spacing
          + '(c) Cancel an existing meeting' + '\n' * line_spacing
          + '(v) View your schedule' + '\n' * line_spacing
          + '(q) Quit' + '\n' * line_spacing)


def process_choice(choice):
    pass


def show_schedule(schedule):
    START_HOUR = 0
    END_HOUR = 1
    TITLE = 2
    print_message('Your Schedule for the day:')
    for meetings in range(len(schedule)):
        print_message('{StartHour} - {EndHour} {Title}'
                      .format(StartHour=schedule[meetings][START_HOUR],
                              EndHour=schedule[meetings][END_HOUR],
                              Title=schedule[meetings][TITLE]))
