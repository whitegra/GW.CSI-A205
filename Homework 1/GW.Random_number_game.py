# import the random library to generate the number:
import random

def main():
    """
    purpose: main program will generate random number, allow user to try to guess the number, and will keep track of user's attempts.
    input parameters: user's guesses
    outputs: will retun the user's num of attemps and the random number, will also prompt the user to play again if they chose.
    """
    # while true (user is playing):
    while True:
        magic_num = random.randint(1, 100) #generate random number between 1 and 100
        # innitialize the correct guess attemps and the incorrect guesses to start at 0:
        correct_guess = 0
        incorrect_guess = 0
        # start while the correct guesses are 0 (the first attempt):
        while correct_guess == 0:
            user_guess = int(input("Guess a number between 1 and 100: "))
            # if user_guess is < magic_num, then it's incorrrect:
            if user_guess < magic_num:
                print("Incorrect. The magic number is greater than", user_guess)
                # add count to incorrect guess
                incorrect_guess += 1
            # else if user_guess is > magic_num, then it's also incorrect:
            elif user_guess > magic_num:
                print("Incorrect. The magic number is less than", user_guess)
                incorrect_guess += 1
            elif user_guess == magic_num:
                print("Correct! The magic number is:", user_guess)
                correct_guess += 1
            else:
                print("Invalid guess")
                incorrect_guess += 1
                
        # to find the total number of attemps:
        total_attempts = incorrect_guess + correct_guess

        # to print the total number of guesses at the end:
        print("Game Summary:")
        print("-----------------")
        print("The magic number was:", magic_num)
        print("Number of Incorrect Guesses:", incorrect_guess)
        print("Total number of Attempts:", total_attempts)
        print("------------------")

        # to prompt user to run the program again if they want:
        play_again = input("Would you like to play again? 'y' for yes, 'n' to exit: ").lower()
        # default to lowercase to avoid issues:
        if play_again.lower() != 'y':
            break
        
# built in variable to execute the program:
if __name__ == "__main__":
    main() # run main
        
            
        
