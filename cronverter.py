import calendar

def treat_day_of_month(day_of_month, old_char):
    pos = day_of_month.rfind(old_char)

    if pos == -1:
        return day_of_month

    return f"{day_of_month[:pos].replace(old_char, f'{old_char} ')} and {day_of_month[(pos+1):]}"

def treat_day_of_week(day_of_week, old_char):
    days = old_char.join([calendar.day_name[int(day_int)-1] for day_int in day_of_week.split(old_char)])
    pos = days.rfind(old_char)
    
    if pos == -1:
        return days

    return f"{days[:pos].replace(old_char, f'{old_char} ')} and {days[(pos+1):]}"

def treat_month_name(months, old_char):
    months_names = old_char.join([calendar.month_name[int(month)] for month in months.split(old_char)])
    pos = months_names.rfind(old_char)
    
    if pos == -1:
        return months_names

    return f"{months_names[:pos].replace(old_char, f'{old_char} ')} and {months_names[(pos+1):]}" 

def cronverter(cron_exp):    
    exp = cron_exp.split()
    minute, hour, day_month, month, day_week = exp[0], exp[1], exp[2], exp[3], exp[4]

    time = f"{hour}:{minute}"
    day_of_month = '' if day_month == '*' else f'on day-of-month {treat_day_of_month(day_month, ",")}'
    day_of_week = '' if day_week == '*' else f'and on {treat_day_of_week(day_week, ",")}'
    month_name = '' if month == '*' else f'in {treat_month_name(month, ",")}'

    if (day_month == '*' and day_week == '*' and month == '*'):
        return f"At {time} everyday."    
    
    return f"At {time} {day_of_month} {day_of_week} {month_name}"

if __name__ == "__main__":
    import sys
    
    print(cronverter(sys.argv[1]))