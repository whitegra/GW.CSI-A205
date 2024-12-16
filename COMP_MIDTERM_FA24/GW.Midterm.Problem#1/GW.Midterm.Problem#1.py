def calc_bonus(sales, hours):
    """
    purpose: to calculate bonus given sales and hours worked
    """
    # if sales < 5000, 1 per 10000 sales
    if sales < 5000:
        hourly_bonus = (sales / 10000) * 1
    # else, bonus = the same but * 2
    elif sales > 5000:
        hourly_bonus = (sales / 10000) * 2
    # function return the hourly bonus * hours worked for total:
    return hourly_bonus * hours

def main():
    """
    purpose: the main script
    """
    # innitialize lists for data:
    sales_list = []
    hours_list = []
    bonus_list = []
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #user enter sales and hours worked for each day of the week:
    for day in days_of_week:
        sales = float(input(f"Enter the sales for weekday {day}: ")) 
        hours = float(input(f"Enter the hours worked for day {day}: ")) #same with hours

        sales_list.append(sales) # append sales to the list
        hours_list.append(hours) #same with hours

        bonus = calc_bonus(sales, hours)
        bonus_list.append(bonus)

        total_hours_worked = sum(hours_list) # to calc total hours
        total_bonus = sum(bonus_list) #same for total bonuses

        #print the other data:
        print(f"Total hours: {total_hours_worked}")
        print(f"Total bonuses: {total_bonus}")

if __name__ == "__main__":
    main()


