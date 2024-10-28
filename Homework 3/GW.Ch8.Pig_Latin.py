def convert_word(word):
    """
    purpose: to convert the words to big latin by moving characters and adding 'ay'
    """
    # first get rid of period at the end because its not the proper last character:
    if word.endswith('.'):
        word = word[:-1]  #remove the period if a word ends with one
        
    # if the word is longer than 1 character then convert
    if len(word) > 0:
        word_to_pig_latin = word[1:] + word[0]
        converted_word = word_to_pig_latin + "ay"
        return converted_word

def convert_sentence(sentence):
    """
    purpose: to split into individual words, then convert each word using the convert_word function
    """
    # split the sentence into individual words
    english_words= sentence.split()
    converted_pig_latin_words = [convert_word(word) for word in english_words] #this will call the convert word function for each word in sentence
    return ' '.join(converted_pig_latin_words) # join the converted words back together to make a sentence again

def main():
    """
    purpose: calls from functions above, takes user's input and converts to pig latin
    """
    #while running, take user input then return the converted sentence:
    while True:
        user_english_sentence = input("Enter the sentence you would like to convert to pig latin: ")
        sentence_convert = convert_sentence(user_english_sentence)
        sentence_converted = sentence_convert + "."
    
        print(f"{user_english_sentence} Converted to pig latin is: ")
        print(f"{sentence_converted}")

        # option to run program again
        run_again = print(input("Would you like to run the program again? (y/n): "))
        if run_again != 'y' or run_again != 'Y':
            break
        
# to execute the main block 
if __name__ == "__main__":
    main()




        
        
        
