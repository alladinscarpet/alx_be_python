from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    return current_date


print(f"Current date and time: {display_current_datetime()}")


def calculate_future_date():
    number = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future = current_date + timedelta(days=number)
    future_date = future.strftime("%Y-%m-%d")

    return future_date


print(f"Future date: {calculate_future_date()}")

