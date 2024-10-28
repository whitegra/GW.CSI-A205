def read_test_key(filename):
    """
    will read the test ket .txt file into a list
    """
    with open(filename, 'r') as file: #open for reading as a file
        test_key = file.read().splitlines()# this will read file and splitlines and convert to lowercase to avoid issues later
        return test_key
def read_student_test(filename):
    """
    will read student's snwers as a .txt file
    """
    with open(filename, 'r') as file:
        student_answers = file.read().splitlines()#same as the test key file
        return student_answers

def grade_test(test_key, student_answers):
    """
    purpose: grade student test, return a score, track correct answers, track incorrect answers
    inputs: the test key and the student's answers
    output: will return the score, correct, incorrect answers
    """
    # first innitialize the correct answer vs. incorrect answer lists:
    correct_list = []
    incorrect_list = []
    # innitialize the correct vs. incorrect answer count:
    count_correct = 0
    count_incorrect = 0
    # a for loop to compare answers, count answers, and apppend answers:
    for i in range(len(test_key)):
        if student_answers[i] == test_key[i]:
            count_correct += 1 # add 1 to correct COUNT
            correct_list.append((i + 1, student_answers[i])) #append the correct answer to the correct list, (i + 1) to iter through
        else:
            count_incorrect += 1
            incorrect_list.append((i + 1, student_answers[i])) # else, then its incorrect, so add to incorrect list and count for i + 1 ...
    return count_correct, count_incorrect, correct_list, incorrect_list

def main():
    """
    purpose: main program
    """
    while True:
        test_key = read_test_key("test_key.txt")
        student_answers = read_student_test("student_answers.txt")
        count_correct, count_incorrect, correct_list, incorrect_list = grade_test(test_key, student_answers)
        if count_correct < 15:
            print("You did not pass the test.")
        else:
            print("Congrats, you passed!")
        print("_______________________")
        print(f"Number of correct answers: {count_correct}")
        print(f"Questions answered correctly: {correct_list}")
        print(f"Number of incorrect answers: {count_incorrect}")
        print(f"Questions answered incorrect: {incorrect_list}")
        print("_______________________")

        run_again = input("Would you like to re-grade?: 'y/n': ")
        if run_again.lower() != 'y':
            break

# to execute the main block 
if __name__ == "__main__":
    main()
