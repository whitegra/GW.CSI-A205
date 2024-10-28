def determine_grade(score): #only individual score
    """
    purpose: to calculate individual grades based on individual score
    input parameters: individual score
    output: will return the letter grade for each score
    """
    # if score is between 90 to 100 (including 90 and 100), then grade = A:
    if 90 <= score <= 100:
        return 'A!'
    # if score is between 80 - 89 (EXclusive of 90), then grade = B:
    elif 80 <= score < 90: # not including 90
        return 'B'
    # if score is between 70 - 79 (EXcluding 80), then grade = C:
    elif 70 <= score < 80:
        return 'C'
    # if score is between 60 - 69 (EXcluding 70), then grade = D:
    elif 60 <= score < 70:
        return 'D'
    # if score is lower than 60, then grade = F:
    elif score < 60:
        return 'F'
    # this is in case the score entered by user is not valid:
    else:
        return 'invalid'
def calculate_average(scores):
    """
    Purpose: to calculate the average from the user's input of scores
    input parameters: scores
    outputs: Will return the average scores in a float num
    """
    # average = sum of all 5 scores / length(number of score values)
    return sum(scores) / len(scores)
        
def main():
    """
    Purpose: Main loop to compute letter grades and average scores
    input parameters: List of 5 scores, then user may chose to run program again
    outputs: will return the average scores and individual grades per score
    """
    while True:
        # innitialize the list of scores to be used later
        scores = []
        # for i in range 5 for 5 test scores to be entered:
        for i in range(5): # To loop 5 times to collect 5 test scores:
            score = float(input("Enter score: ")) # use string literal for score 1.. 2.. etc etc for clarity and storing
            scores.append(score) # this is to append all the individual score to the scores library
        # for score in scores len(5), determine score for score[i] in the list, and then print:
        for i in range(5):
            score = scores[i] #this is to index the 'scores' list to each individual score in list
            letter_grade = determine_grade(score) # calling determine grade to calculate score for each score in list
            print("__________________________")
            print("student letter grades:")
            print("Score", score, " = Grade", letter_grade) # this is to print the score(s) and the letter grades.
            print("__________________________")

        # to calulate average score:
        average_score = calculate_average(scores)
        # to calculate average grade:
        average_letter_grade = determine_grade(average_score)

        # now to print the average score and average letter grade:
        print("______________________________")
        print("Average Score:", average_score)
        print("Average Letter Grade:", average_letter_grade)
        print("______________________________")

        # if user wants to run program again:
        run_again = input("Run again? Enter 'y' for yes, or 'n' to exit.").lower() # default to lowercase to avoid issues
        if run_again.lower() != 'y':
            break # if user dosen't enter 'y', then exit.

# built in variable to execute the program:
if __name__ == "__main__":
    main() # run main
        
            
 
