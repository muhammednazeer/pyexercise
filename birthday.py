def days_difference (day1, day2):
    return day2 - day1

def get_weekday (current_weekday, days_ahead):
    return (current_weekday + days_ahead - 1) % 7 + 1

def get_birthday_weekday(current_weekday, current_day, birthday_day):
    days_differce = days_difference(current_day, birthday_day)
    return get_weekday(current_weekday, days_differce)

current_weekday = int(input("Enter current day of the week (1-7): "))
current_day = int(input("Enter the day of the year (1-365): "))
birthday_day = int(input("Enter your birthday day (1-365): "))

birthday = get_birthday_weekday(current_weekday, current_day, birthday_day)

if birthday == 1:
    print ("Your next Birthday is on Sunday") 
elif birthday == 2:
    print ("Your next Birthday is on Monday")
elif birthday == 3:
    print ("Your next Birthday is on Tuesday")
elif birthday == 4:
    print ("Your next Birthday is on Wednesday")
elif birthday == 5:
    print ("Your next Birthday is on Thursday")
elif birthday == 5:
    print ("Your next Birthday is on Friday")
elif birthday == 7:
    print ("Your next Birthday is on Saturday")
else:
    print("Your input was wrong!")