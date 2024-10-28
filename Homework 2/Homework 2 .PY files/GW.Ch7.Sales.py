def daily_sales():
    """
    purpose: for user to enter the sales for each day of the week in order to calculate the total weekly sales
    inputs: the sales each day of the week
    output: the total sales for the week
    """
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] # list of days
    week_sales = 0 # innitialize the weekly sales to 0 to start
    # for each day, user enter the sale for that day to be added to week sales
    for day in week_days:
        day_sales = float(input(f"enter the sales for {day}: ")) #use f string to prompt user to enter the sale for day in list
        week_sales += day_sales #add it to week_sales
    print(f"The total sales for this week is: $ {week_sales:.2f}") #print total week sales using f string and round to 100th place for cents

def main():
    """
    purpose: main script, runs the daily_sales if user wants to
    inputs: the inputs from the daily_sales function + if user wants to run again
    output: will output the total weekly sales to two float decimal places and in $
    """
    while True:
        daily_sales()
        sales_again = input("Would you like to run again? ('y/n'): ")
        if sales_again.lower() != 'y':
            break
        
#this is to run the main function to execute code
if __name__ == "__main__":
    main()
