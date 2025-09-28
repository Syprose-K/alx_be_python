from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Save current date and time
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print(formatted)  # Print the formatted result
display_current_datetime()


def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print(future_date.strftime("%Y-%m-%d"))
number_of_days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(number_of_days)
