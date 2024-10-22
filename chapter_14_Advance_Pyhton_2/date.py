import datetime
# Get the current date and time

current_datetime = datetime.datetime.now()
print(current_datetime)
print(current_datetime.strftime("%A %D %A %Y %H:%M:%S"))
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)

formatted_date = current_datetime.strftime("%d-%m-%Y")
print(formatted_date)  # Output: 11-10-2024
