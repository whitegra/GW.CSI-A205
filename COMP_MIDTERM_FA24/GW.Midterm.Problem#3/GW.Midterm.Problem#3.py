def convert_to_short():
    """
    will convert from long format to /// format
    """
    user_date = input("Enter the date you want to convert: ")
        
    user_month, day, year = user_date.split(' ') #split by space since there should only be spaces
    day = day.replace(',', '') # YOU HAVE TO REPLACE THE COMMA WITH NOTHING
    months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_number_index = months.index(user_month) + 1 #index the month from the list and add one to be the correct month number

    print("______________________________________________")
    print(f"{month_number_index}/{day}/{year}")
    print("______________________________________________")

def convert_to_long():
    """
    will conert from /// format to the long format.
    """
    user_date = input("Enter the date you want to convert: ")
        
    month, day, year = user_date.split('/') #split to get the individual elements to convert
    months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print("______________________________________________")
    print(f"{months[int(month) - 1]}, {int(day)}, {year}") #this is the new format.
    print("______________________________________________")

def main():
    while True:
        convert_choice = input("Chose which conversion: mm/dd/yy (1), or Month day , year (2)?: ")
        
        if convert_choice == '1':
            convert_to_long()
        elif convert_choice == '2':
            convert_to_short()
        else:
            print("invalid option")
            
        run_again = input("Make another conversion? (y/n): ")
        if run_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
