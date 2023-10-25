from datetime import datetime, timedelta


def MostFreeTime(*args):
    """Takes arbitrary number of strings (*args) in format: 'hh:mm AM/PM-hh:mm AM/PM', where first part is start_time of some event, and second part 
    is end_time. Calculate most free time between given events.
    For example: MostFreeTime("5:45AM-6:50AM, "9:15PM-11:45PM", "5:15PM-8:35PM", "11:25AM-2:05PM") will return 04:35 --> since 6:50AM till 11:25AM

    Returns:
        [datetime]: Return most free time between given events in format: hh:mm
    """
    times = []
    most_free_time, current_free_time = timedelta(), timedelta()
    format = '%I:%M%p'  # 11:56PM // 12:35AM

    for arg in args:
        time_str = arg.split('-')[0], arg.split('-')[1]  # "8:30AM-10:30AM"
        times.append(time_str)

    times = [(datetime.strptime(time_str[0], format).time(), datetime.strptime(time_str[1], format).time())
             for time_str in times]  # transfor time_str to datetime object: [(start_time, end_time), (...)]
    times.sort(key=lambda x: x[0])  # sort by start_time

    for i in range(1, len(times)):
        current_free_time = timedelta(hours=times[i][0].hour, minutes=times[i][0].minute) - timedelta(
            hours=times[i-1][1].hour, minutes=times[i-1][1].minute)  # cast to timedelta object, datetime doesn't support subtraction or addition
        if current_free_time > most_free_time:
            most_free_time = current_free_time

    # format: 23:54:21, show only 23:54
    return datetime.strptime(str(most_free_time), '%H:%M:%S').strftime('%H:%M')


print(MostFreeTime("08:30AM-10:30AM", "05:25AM-06:30AM", "11:45AM-12:30PM"))
