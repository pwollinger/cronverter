import calendar

#Function to treat time to cron time, it can be every x minute, every x hour or the time defined. 
def treat_time(minute, hour):
    
    if minute == '*' and hour == '*':
        return "At every minute"
    
    if minute == '*':
        return f"At every minute past hour {hour}"
    
    if hour == '*':
        return f"At minute {minute}"

    return f"At {hour}:{minute}"   

#Treat the list of possible days of month
def treat_day_of_month(day_of_month, old_char):
    #checks the position of the last comma in the string.
    pos = day_of_month.rfind(old_char)

    #if the string doesn't contains a comma, then the rfind function returns -1. Because of that, we only returns the day_of_month
    if pos == -1:
        return day_of_month

    #First only gets the string until the last comma, then replace the comma with comma and space. Then, we add the " and " connector with the last day of the string.
    return f"{day_of_month[:pos].replace(old_char, f'{old_char} ')} and {day_of_month[(pos+1):]}"

#Treat the list of possible days of the week
def treat_day_of_week(day_of_week, old_char):
    #Replace the number of the day_of_week with the name of the day. calendar.day_name starts on 0 with monday. In the end, we join every day with an comma.
    days = old_char.join([calendar.day_name[int(day_int)-1] for day_int in day_of_week.split(old_char)])

    #checks the position of the last comma in the string.
    pos = days.rfind(old_char)
    
    #if the string doesn't contains a comma, then the rfind function returns -1. Because of that, we only returns days, that will contain only one day.
    if pos == -1:
        return days

    #First only gets the string until the last comma, then replace the comma with comma and space. Then, we add the " and " connector with the last day of the string.
    return f"{days[:pos].replace(old_char, f'{old_char} ')} and {days[(pos+1):]}"

#Treat the list of possible months
def treat_month_name(months, old_char):
    
    #Replace the number of the month with the name of the month. In the end, we join every day with an comma.
    months_names = old_char.join([calendar.month_name[int(month)] for month in months.split(old_char)])
    
    #checks the position of the last comma in the string.
    pos = months_names.rfind(old_char)
    
    #if the string doesn't contains a comma, then the rfind function returns -1. Because of that, we only returns month_names, that will contain only one month.
    if pos == -1:
        return months_names

    #First only gets the string until the last comma, then replace the comma with comma and space. Then, we add the " and " connector with the last month of the string.
    return f"{months_names[:pos].replace(old_char, f'{old_char} ')} and {months_names[(pos+1):]}" 

#Function that converts cron time to english.
def cronverter(cron_exp):
    
    #Split the string by the comma that separates the fields.    
    exp = cron_exp.split()
    minute, hour, day_month, month, day_week = exp[0], exp[1], exp[2], exp[3], exp[4]

    #Convert each field
    time = treat_time(minute, hour)
    day_of_month = '' if day_month == '*' else f'on day-of-month {treat_day_of_month(day_month, ",")}'
    day_of_week = '' if day_week == '*' else f' and on {treat_day_of_week(day_week, ",")}'
    month_name = '' if month == '*' else f'in {treat_month_name(month, ",")}'

    #Checks if only the time is defined. If so, then returns the time with the everyday sentence.
    if (day_month == '*' and day_week == '*' and month == '*'):
        return f"{time} everyday"    
    
    #Returns the english sentence.
    return f"{time} {day_of_month}{day_of_week} {month_name}"

#MAIN EXECUTION
if __name__ == "__main__":
    import sys
    
    #Read the first argument, it needs to be a string with all cron time values.
    print(cronverter(sys.argv[1]))