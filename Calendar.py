__author__ = 'student'

import os

'''

IMPORTANT NOTE: Do NOT change any of the function names or their signatures (the parameters they take).
Your functions must behave exactly as described. Please check for correctness by running DocTests
included in function headers.

Manage a calendar database.

A calendar is a dictionary keyed by date ("YYYY-MM-DD") with value being a list of
strings, the events on the specified date.

Example:
calendar["2015-10-12"] # is a list of events on "2015-10-12"

calendar["2015-10-12"]==["Eye doctor", "lunch with sid", "dinner with jane"]
'''

# ---------------------------------------------------------------------------------------------------------------------
# Implementation of calendar commands
# ---------------------------------------------------------------------------------------------------------------------

def command_help():
    '''
    Print out help for the system. That is...
    :return: a string indicating any errors, "" for no errors
    '''

    help = """
    Help for Calendar. The calendar commands are

    add DATE DETAILS               add the event DETAILS at the specified DATE
    show                           show all events in the claendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user input follows command:

    command: add 2015-10-12 dinner with jane
    added

    command: show
        2015-10-12:
            0: Eye doctor
            1: lunch with sid
            2: dinner with jane
        2015-10-29:
            0: Change oil in blue car
            1: Fix tree near front walkway
            2: Get salad stuff, leuttice, red peppers, green peppers
        2015-11-06:
            0: Sid's birthday

    command: delete 2015-10-29 2
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2015-12-21
    2016-01-02

    Event DETAILS consist of alphabetic characters, not tabs or newlines allowed.
    """
    print(help)
    return ""




def command_add(date, event_details, calendar):
    '''
    Add event_details to the list at calendar[date]
    Create date if it was not there

    :param date: A string date formatted as "YYYY-MM-DD"
    :param event_details: A string describing the event
    :param calendars: The calendars database
    :return: a string indicating any errors, "" for no errors

    >>> calendar = {}
    >>> command_add("2015-10-20", "Python class", calendar)
    ''
    >>> calendar == {'2015-10-20': ['Python class']}
    True
    >>> command_add("2015-11-01", "CSC108 test 2", calendar)
    ''
    >>> calendar == {'2015-11-01': ['CSC108 test 2'], '2015-10-20': ['Python class']}
    True
    >>> command_add("2015-11-01", "go out with friends after test", calendar)
    ''
    >>> calendar == {'2015-11-01': ['CSC108 test 2', 'go out with friends after test'], '2015-10-20': ['Python class']}
    True
    >>>

    '''

    #Validate input

    if not len(date)==10:
        return "Date is not valid"

    splitDate = date.split("-")

    if not len(splitDate) == 3:
        return "Date is not valid"

    if len(splitDate[0])!=4 or not splitDate[0].isdigit():
        #fail
        return "The Year you inputed is not valid"

    if len(splitDate[1])!=2 or not int(splitDate[1]) > 0 or not int(splitDate[1])<13:
        #fail
        return "The month you inputed is not valid"

    if len(splitDate[2])!=2  or not int(splitDate[2]) > 0 or not int(splitDate[2])<32:
        #fail
        return "The day you inputed is not valid"

    else:
        if date in calendar:
            calendar[date].append(event_details)
        else:mvhmhmvhmgh
            calendar[date] = [event_details]
        return ""

#dictionary = dict();
#date = "1920-12-20"
#wrong_date = "19999-29"
#super_wrong_date = "abcd-de-de"
#print(command_add(date,"Right event",dictionary))
#print(command_add(date,"Right event 2",dictionary))
#print(command_add(wrong_date,"Wrong event",dictionary))
#print(command_add(super_wrong_date,"super wrong event", dictionary))
#print(dictionary)
#print (dictionary == {'1920-12-20': ['Right event', 'Right event 2']} )






def command_show(calendar):
    '''
    Print the list of events for calendar sorted in increasing date order
    :param calendar: the database of events
    :return: a string indicating any errors, "" for no errors

    Example:
    >>> calendar = {}
    >>> command_add("2015-10-12", "Eye doctor", calendar)
    ''
    >>> command_add("2015-10-12", "lunch with sid", calendar)
    ''
    >>> command_add("2015-10-29", "Change oil in blue car", calendar)
    ''
    >>> command_add("2015-10-12", "dinner with Jane", calendar)
    ''
    >>> command_add("2015-10-29", "Fix tree near front walkway", calendar)
    ''
    >>> command_add("2015-10-29", "Get salad stuff", calendar)
    ''
    >>> command_add("2015-11-06", "Sid's birthday", calendar)
    ''
    >>> command_show(calendar)
        2015-10-12:
            0: Eye doctor
            1: lunch with sid
            2: dinner with Jane
        2015-10-29:
            0: Change oil in blue car
            1: Fix tree near front walkway
            2: Get salad stuff
        2015-11-06:
            0: Sid's birthday
    ''
    '''
    # Hint: Don't use \t (the tab character) to indent, or DocTest will fail in the above testcase.
    # Put 4 spaces before the date, 8 spaces before each item.

    listOfDates = list(calendar.keys())

    listOfDates.sort()

    #for each key in key array
    #for each item that will be named date that are inside the list that is named listOfDates
    # for date in listOfDates:

    i=0



    if len(listOfDates) > 0:
        while i<len(listOfDates):

            print("    "+listOfDates[i])

            j=0
            while j<len(calendar[listOfDates[i]]):
                #print out the events one by one
                print("        " + str(j) +": "+calendar[listOfDates[i]][j])
                j=j+1
            i=i+1

    else:
        print (calendar)


    '''
              date(key)->listOfDates(array)
              calendar(key of string, value of array)-> Every key(string) corresponds to a particular value(array)
              listOfDates[i] ->gets the date(key)
              calendar[listOfDates[i]] == calendar[key](conceptually)==value == an array!
              calendar[key][j]
    '''



#Sort this list- You will proobably have to parse the date in to proper numbers, and
#then sort by year, month, day

# go through this list from bottom to top, and print the contents of the dictionary as you go through the dates, using the date as the key to retrieve the events






def command_delete(date, entry_number, calendar):
    '''
    Delete the entry at calendar[date][entry_number]
    If calendar[date] is empty, remove this date from the calendar

    :param date: A string date formatted as "YYYY-MM-DD"
    :param entry_number: An integer indicating the entry in calendar[date] to delete
    :param calendar: The calendars database
    :return: a string indicating any errors, "" for no errors

    Example:

    >>> calendar = {}
    >>> command_add("2015-10-20", "Python class", calendar)
    ''
    >>> calendar == {'2015-10-20': ['Python class']}
    True
    >>> command_add("2015-11-01", "CSC108 test 2", calendar)
    ''
    >>> calendar == {'2015-11-01': ['CSC108 test 2'], '2015-10-20': ['Python class']}
    True
    >>> command_add("2015-11-01", "go out with friends after test", calendar)
    ''
    >>> calendar == {'2015-11-01': ['CSC108 test 2', 'go out with friends after test'], '2015-10-20': ['Python class']}
    True
    >>> command_show(calendar)
        2015-10-20:
            0: Python class
        2015-11-01:
            0: CSC108 test 2
            1: go out with friends after test
    ''

    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2015-10-20", 3, calendar)
    'there is no entry 3 on date 2015-10-20 in the calendar'
    >>> command_delete("2015-10-20", 0, calendar)
    ''
    >>> calendar == {'2015-11-01': ['CSC108 test 2', 'go out with friends after test']}
    True
    >>> command_delete("2015-11-01", 0, calendar)
    ''
    >>> calendar == {'2015-11-01': ['go out with friends after test']}
    True
    >>> command_delete("2015-11-01", 0, calendar)
    ''
    >>> calendar == {}
    True

    '''


    if not date in calendar:
        return date + " is not a date in the calendar"

    eventsOfDay = calendar[date]

    if not int(entry_number) >= 0 and not int(entry_number) <= (len(eventsOfDay)-1):
        return "there is no " + entry_number + " on date " + date + " in the calendar"


    eventsOfDay.pop(int(entry_number))

    listOfDates = list(calendar.keys())


    if eventsOfDay == []:
        calendar.pop(date)

    print("deleted")

    return ""


# ---------------------------------------------------------------------------------------------------------------------
# Functions dealing with calendar persistence
# ---------------------------------------------------------------------------------------------------------------------



'''
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

'''



def save_calendar(calendar):
    '''
    Save calendar to 'calendar.txt', overwriting it if it already exists.

    The format of calendar.txt is the following:

    date_1:description_1\tdescription_2\t...\tdescription_n\n
    date_2:description_1\tdescription_2\t...\tdescription_n\n
    date_3:description_1\tdescription_2\t...\tdescription_n\n
    date_4:description_1\tdescription_2\t...\tdescription_n\n
    date_5:description_1\tdescription_2\t...\tdescription_n\n

    Example: The following calendar...

        2015-10-20:
            0: Python class
        2015-11-01:
            0: CSC108 test 2
            1: go out with friends after test

    appears in calendar.txt as ...

    2015-10-20:Python class
    2015-11-01:CSC108 test 2    go out with friends after test

                            ^^^^ This is a \t, (tab) character.


    :param calendar:
    :return: True/False, depending on whether the calendar was saved.
    '''
    # YOUR CODE GOES HERE

    # Retrieve date
        #For each description, format in to a line
        #save to file

#     date_1:description_1\tdescription_2\t...\tdescription_n\n

    #a loop that goes through all the dates
    #print out the contents

    #calendar[date]== ['entry 1', 'entry 2']
    #calendar[i]=='entry 1'
    #2010-12-31['entry 1', 'entry 2']


    # date_1:description_1\tdescription_2\t...\tdescription_n\n
    # I notice sumtingz
    # 1. I notice that the date only happens once, at the beginning.
    # 2. I notice that the descriptions repeat n times,
    # 3. I notice the description follows the template description_n\t
    # 4. I notice that the string ends with \n
    # 5. I should only print when this string is fully assembled.


    #for every date in calendar
    for date in calendar:
        # 1. I notice that the date only happens once, at the beginning.
        dateLine = date + ":"
        # 2. I notice that the descriptions repeat n times, and it repeats for all members of the date
        for event in calendar[date]:
        # 3. I notice the description follows the template description_n\t
            dateLine = dateLine + event + "\t"
        # 4. I notice that the string ends with \n
        dateLine = dateLine + "\n"
        # 5. Add this string section to the whole string.

        if dateLine == "\t":
            del dateLine

        file = open ("calendar.txt","a")

        file.write (dateLine)



    #date_1:description_1\tdescription_2\t...\tdescription_n\n
    #expected print : 2010-12-31:entry 1\tentry 2\t\n

#   for event in calendar[date]:

#calendar = {}
#date = "2010-10-10"
#date2 = "2011-11-11"
#event1 = "event 1"
#event2 = "event 2"

#command_add(date,event1,calendar)
#command_add(date,event2,calendar)
#command_add(date2,event1,calendar)
#command_add(date2,event2,calendar)

#save_calendar(calendar)




def load_calendar():
    '''
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above.

    :return: calendar, or False, if calendar could not be loaded from disk.

    '''
    calendar = {}
    if os.path.isfile('calendar.txt'):

        input_file = open("calendar.txt")

        for line in input_file:

            splitLine = line.split(":")

            if len(splitLine) == 0:
                del splitLine

            if len(splitLine)<=2:

                command_add(splitLine[0], splitLine[1], calendar)

            if len(splitLine)>2:
                splitline = splitLine[1].split("\t")

                i=0
                while i <= len(splitline)-2:

                    command_add(splitLine[0], splitline[i], calendar)

                    i=i+1

        return calendar
    else:
        return calendar





# ---------------------------------------------------------------------------------------------------------------------
# Functions dealing with parsing commands
# ---------------------------------------------------------------------------------------------------------------------




def is_command(command):
    '''
    Return whether command is indeed a command, that is, one of
    "add", "delete", "quit", "help", "show"
    :param command: string
    :return: True if command is one of ["add", "delete", "quit", "help", "show"], false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''

    if command == "add" or command == "delete" or command == "quit" or command == "help" or command == "show":
        return True
    else:
        return False







def is_calendar_date(date):
    '''
    Return whether date looks like a calendar date
    :param date: a string
    :return: True, if date has the form "YYYY-MM-DD" and False otherwise

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only basic string
    # manipulation, comparisons, and type conversion. Please do not use any powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789

    if not len(date)==10:
        return False

    splitDate = date.split("-")

    if not len(splitDate) == 3:
        return False

    if len(splitDate[0])!=4 or not splitDate[0].isdigit():
        #fail
        return False

    if len(splitDate[1])!=2 or not int(splitDate[1]) > 0 or not int(splitDate[1])<13:
        #fail
        return False

    if len(splitDate[2])!=2  or not int(splitDate[2]) > 0 or not int(splitDate[2])<32:
        #fail
        return False
    else:
        return True






def is_natural_number(str):
    '''
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    :param str: string
    :return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''

    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]

    return str.isdigit()





def parse_command(line):
    '''
    Parse command and arguments from the line. Return a list [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid. Return ["help"] otherwise.
    The valid commands are

    1) add DATE DETAILS
    2) show
    3) delete DATE NUMBER
    4) quit
    5) help

    :param line: a string command
    :return: A list consiting of [command, arg1, arg2, ...]. Return ["error", ERROR_DETAILS], if
    line can not be parsed.

    Example:
    >>> parse_command("add 2015-10-21 budget meeting")
    ['add', '2015-10-21', 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE DETAILS']
    >>> parse_command("add 2015-10-22 Tims with Sally.")
    ['add', '2015-10-22', 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE NUMBER']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE NUMBER']
    >>> parse_command("delete 15-10-22 1")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event index']
    >>> parse_command("delete 2015-10-22 314")
    ['delete', '2015-10-22', '314']
    >>> parse_command("quit")
    ['quit']

    '''
    # HINT: You can first split, then join back the parts of the final argument.


    # YOUR CODE GOES HERE

    splitLine = line.split( " " , 2)

    #checking the validity of the command
    if not (splitLine[0] == "add" or splitLine[0] == "delete" or splitLine[0] == "quit" or splitLine[0] == "show") or  splitLine[0] == "help":
        return ['help']
    if splitLine[0] == "quit":
        return ['quit']



    chars = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM')
    if splitLine[0] == "delete" and len(splitLine) == 1:
        return ['error', 'delete DATE NUMBER']
    if splitLine[0] == "add" and len(splitLine)== 1:
        return ['error', 'add DATE DETAILS']
    if splitLine[0] == "show" and len(splitLine)== 1:
        return ['show']
    if splitLine[0] == "show" and any((c in chars) for c in splitLine[1]):
        return ['error', 'show']
    if splitLine[0] == "add" and any((c in chars) for c in splitLine[1]):
        return ['error', 'add DATE DETAILS']
    if splitLine[0] == "delete" and any((c in chars) for c in splitLine[1]):
        return ['error', 'delete DATE NUMBER']



    #checking the validity of the date
    date = splitLine[1]

    is_calendar_date(date)

    if is_calendar_date(date)is False:
        return (['error', 'not a valid calendar date'])



    #checking the validity of the event description
    if is_calendar_date(date) is True and splitLine[0] == "add" and len(splitLine)== 2:
        return ['error', 'add DATE DETAILS']


    chars2 = set('!@#$%^&*()_+=-`~[]{}\|:;<>/?')
    if len(splitLine)==3:
        if any((c in chars2) for c in splitLine[2]):
            return ['error', 'not a valid event index']

    return (splitLine)


# ---------------------------------------------------------------------------------------------------------------------
# Functions dealing with the user. This is the calendar application.
# ---------------------------------------------------------------------------------------------------------------------

def user_interface():
    '''
    Load calendar.txt and then interact with the user. The user interface
    operates as follows, the text after command: is the command entered by the user.

    calendar loaded
    command: add 2015-10-21 budget meeting
    added
    command: add 2015-10-22 go to the gym
    added
    command: add 2015-10-23 go to the gym
    added
    command: add 2015-11-01 Make sure to submit csc108 assignment 2
    added
    command: add 2015-12-02 Make sure to submit csc108 assignment 3
    added
    command: add 2015-11-06 Term test 2
    added
    command: add 2015-10-29 Get salad stuff, leuttice, red peppers, green peppers
    added
    command: add 2015-11-06 Sid's birthday
    added
    command: show
        2015-10-21:
            0: budget meeting
        2015-10-22:
            0: go to the gym
        2015-10-23:
            0: go to the gym
        2015-10-29:
            0: Get salad stuff, leuttice, red peppers, green peppers
        2015-11-01:
            0: Make sure to submit csc108 assignment 2
        2015-11-06:
            0: Term test 2
            1: Sid's birthday
        2015-12-02:
            0: Make sure to submit csc108 assignment 3
    command: delete 2015-10-29 0
    deleted
    command: delete 2015-12-03 0
    2015-12-03 is not a date in the calendar
    command: delete 2015-12-02 0
    deleted
    command: show
        2015-10-21:
            0: budget meeting
        2015-10-22:
            0: go to the gym
        2015-10-23:
            0: go to the gym
        2015-11-01:
            0: Make sure to submit csc108 assignment 2
        2015-11-06:
            0: Term test 2
            1: Sid's birthday
    command: quit
    calendar saved

    :return: None
    '''

    calendar = load_calendar()

    print("calendar loaded")

    while True:
        command = input("command: ")
        args = parse_command(command)


        if args[0] == "add":
            result = command_add (args[1], args[2], calendar)
            print ("added")
            if result != "":
                print(command_add (args[1], args[2], calendar))


        if args[0] == "show":
            command_show (calendar)


        if args[0] == "help":
            command_help()

        if len(args)==3:
            if args[0] == "delete":
                result = command_delete (args[1], args[2], calendar)
                if result != "":
                    print(result)
            print(result)

        if args[0] == "quit":
            break

    save_calendar(calendar)
    print ("calendar saved")


if __name__ == "__main__":
    user_interface()