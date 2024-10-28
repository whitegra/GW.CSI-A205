def feet_to_inches(feet):
    """
    purpose: to convert feet to in
    input parameters: feet as a float num
    output: feet converted to inches.
    """
    return feet * 12
def inches_to_feet(inches):
    """
    purpose: to convert inches to feet
    input parameters: inches as a float num
    output: inches converted to feet.
    """
    return inches / 12
def main():
    """
    Purpose: to convert to feet or inches based on user's input and conversion choice.
    input parameters: user inputs "f" for feet conversion, or "i" to convert to inches, then, user will input a float value to convert.
                      user may also chose to rerun the program if they want to make another conversion. 
    output: user's value converted to feet or inches.
    """
    while True:
        # first the user choses the conversion they want to make, also, automatically convert response to lowercase to avoid issues:
        user_convert = input("To begin, enter 'f' for inches to feet, or 'i' for feet to inches: ").lower() # this is to make repsonse default lowercase
        # if user is converting from feet to inches:
        if user_convert == 'i':
            feet = float(input("Enter the number of feet to be converted to inches: ")) # user enter feet as float num
            inches = feet_to_inches(feet) # convert to inches
            print(f"{feet} feet = {inches} inches") # print as a string literal for clarity
        # if user is converting from inches to feet:
        elif user_convert == 'f':
            inches = float(input("Enter the number of inches to be converted to feet: ")) # user enters inches as float
            feet = inches_to_feet(inches) # convert to feet
            print(f"{inches} inches = {feet} feet") # print as string literal
        # in case user enters invalid choise:
        else:
            print("Invalid input. 'f' for in to feet, or 'i' for feet to inches.")
            continue # this is to reloop for user to try again.
        # this is for the user to re-run the program if they want to make an additonal conversion:
        convert_again = input("Run program again? Enter 'y' for yes, or 'n' to exit: ").lower() # make response lowercase to avoid issues.
        if convert_again != 'y': # if the response is not yes, then exit. 
            break
if __name__ == "__main__":
    main()
    
