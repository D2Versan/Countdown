import time
import datetime

def countdown(target_datetime):
    while True:
        current_datetime = datetime.datetime.now()
        time_left = target_datetime - current_datetime

        if time_left.total_seconds() <= 0:
            print("This is the end of this fucking shit show")
            break

        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Time left: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="\r")
        time.sleep(1)

if __name__ == "__main__":
    import datetime

    year = 2023
    month = 12
    day = 31
    hour = 23
    minute = 59
    second = 59
    
    target_datetime = datetime.datetime(year, month, day, hour, minute, second)
    countdown(target_datetime)

    
    
