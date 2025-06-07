from datetime import datetime, timedelta

#create the function 
def display_current_datetime():
    current_date = datetime.now() #The current date and time
    formatted_datetime = current_date.strftikme("%Y-%m-%d %H:%M:%S") #Format current date and time
    print(f"Current date and time: {formatted_datetime}")
    return current_date

def calculate_future_date(days_to_add):
    days = int(input("Enter the number of days to add to the current dae: "))
    current_date = datetime.now()
    future_date = current_date = timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

display_current_datetime()
calculate_future_date()
    
    

