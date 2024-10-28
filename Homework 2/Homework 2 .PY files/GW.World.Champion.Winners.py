def read_champions(filename):
    """
    this will read the .txt into a list
    """
    with open(filename, 'r') as file:
        champions_list = file.read().splitlines()
        return champions_list
def main():
    """
    purpose: the main program
    inputs: the user's team
    outputs: will display the number of times the user's team has won
    """
    while True:
        champions_list = read_champions('WorldSeriesWinners.txt')
        # innitialize the win count to zero
        win_count = 0
        user_team = input("Enter a world series team: ")
        for i in range(len(champions_list)):
            if user_team == champions_list[i]:
                win_count += 1
            else:
                win_count += 0
        print(f"The team {user_team} won the championship a total of {win_count} times")
        run_again = input("Would you like to enter a new team? ('y/n'): ")
        if run_again.lower() != 'y':
            break

# to execute the main block 
if __name__ == "__main__":
    main()
        
                    
                    
                           
                       

