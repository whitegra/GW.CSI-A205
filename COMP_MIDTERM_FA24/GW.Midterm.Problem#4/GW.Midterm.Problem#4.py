def count_consonants(sentence):
    consonants = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return sum(1 for char in sentence if char in consonants) # sum of all consonants (1 per each)

def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in sentence if char in vowels) #same here

def count_upper(sentence):
    return sum(1 for char in sentence if char.isupper())

def count_lower(sentence):
    return sum(1 for char in sentence if char.islower())

def count_words(sentence):
    return len(sentence.split()) #if u split sentence each element should be a word

def main():
    while True:
        sentence = input("Enter your sentence: ")

        count_consonants(sentence)
        print("___________________________________")
        print(f"Consonants, {count_consonants(sentence)}")
        print("___________________________________")

        count_vowels(sentence)
        print(f"Vowels, {count_vowels(sentence)}")
        print("___________________________________")

        count_upper(sentence)
        print(f"Uppercase letters: {count_upper(sentence)}")
        print("___________________________________")

        count_lower(sentence)
        print(f"Lowercase letters, {count_lower(sentence)}")
        print("___________________________________")

        count_words(sentence)
        print(f"Words, {count_words(sentence)}")
        print("___________________________________")

        run_again = input("Run again? (y/n): ")
        if run_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
