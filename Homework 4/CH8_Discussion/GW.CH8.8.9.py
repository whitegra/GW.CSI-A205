def main():
    """
    purpose: user enters a date, then plit by month day and year
    """
    date_string = input("Enter a date: ")
    date_list = date_string.split('/')

    print(f"Month: {date_list[0]}")
    print(f"Day: {date_list[1]}")
    print(f"Year: {date_list[2]}")
        

# to execute the main block 
if __name__ == "__main__":
    main()
