from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()

    return current_date.strftime("%Y-%m-%d %H:%M:%S")


print(f"Current date and time: {display_current_datetime()}")


def calculate_future_date():
    number = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number)

    return future_date.strftime("%Y-%m-%d")


print(f"Future date: {calculate_future_date()}")

