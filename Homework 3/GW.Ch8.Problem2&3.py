def average_sentence_words(file):
    """
    purpose:calculate average words per sentence
    """
    # if it ends in period its a sentence
    file_sentences = file.split('.')
    # also a sentence if it ends with ? or !
    file_sentences += file.split('!')
    file_sentences += file.split('?')

    #count words per sentence
    sentence_words = 0
    for sentence in file_sentences:
        #words = sentences.split
        words = sentence.split()
        sentence_words += len(words)
    #calculate the average words:
    if len(file_sentences) > 0:
        return sentence_words / len(file_sentences)
    # else then there are no words so its zero
    else:
        return 0

def count_lowercase(file):
    """
    purpose:to count the number of lowercase letter in the file
    """
    lowercase_count = 0
    for char in file:
        if char.islower():
            lowercase_count += 1
    return lowercase_count

def count_uppercase(file):
    """
    purpose: count the number of uppercase letters in file
    """
    # for char in file if its uppercase add it and return it 
    uppercase_count = 0
    for char in file:
        if char.isupper():
            uppercase_count += 1
    return uppercase_count

def count_numbers(file):
    """
    purpose: to count the number of digits in the file
    """
    numbers_count = 0
    for char in file:
        if char.isdigit():
            numbers_count += 1
    return numbers_count

def main():
    """
    purpose: main function that will call from the ones above
    inputs: file, choice of oppertions, user run again option 
    output: the choice of opperations
    """
    while True:
        # first read the file:
        with open('text.txt', 'r') as text_file:
            file = text_file.read()
            
        #then user can chose which opperation they want to do:
        user_opperation = input("Choose which operation you would like to complete:\n"
                            "'W' for average words per sentence\n"
                            "'L' for lowercase count\n"
                            "'U' for uppercase count\n"
                            "'N' for number count\n"
                            "'A' for ALL OF THE ABOVE\n"
                            "Enter your choice: ")
        
        # call from above functions per the users choice of opperations: 
        if user_opperation.lower() == 'w':
            average_words = average_sentence_words(file)
            print("______________________________________")
            print(f"Average words per sentence: {average_words}")
            print("______________________________________")
        elif user_opperation.lower() == 'l':
            lowercase = count_lowercase(file)
            print("______________________________________")
            print(f"Lowercase count: {lowercase}")
            print("______________________________________")
        elif user_opperation.lower() == 'u':
            uppercase = count_uppercase(file)
            print("______________________________________")
            print(f"Uppercase count: {uppercase}")
            print("______________________________________")
        elif user_opperation.lower() == 'n':
            numbers = count_numbers(file)
            print("______________________________________")
            print(f"Number count: {numbers}")
            print("______________________________________")
        elif user_opperation.lower() == 'a':
            average_words = average_sentence_words(file)
            print("______________________________________")
            print(f"Average words per sentence: {average_words}")


            lowercase = count_lowercase(file)
            print("______________________________________")
            print(f"Lowercase count: {lowercase}")
     
            uppercase = count_uppercase(file)
            print("______________________________________")
            print(f"Uppercase count: {uppercase}")

            numbers = count_numbers(file)
            print("______________________________________")
            print(f"Number count: {numbers}")
            print("______________________________________")
        else:
            print("Invalid option.")

        # option to run again
        run_again = print(input("Would you like to run this program again?: 'y/n': "))
        if run_again != 'y' or run_again != 'Y':
            break
        
# to execute the main block 
if __name__ == "__main__":
    main()












                  
