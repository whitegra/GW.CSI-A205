from GWpetClass import Pet

#main function for user to enter information and to call from pet class
def main():
    while True:
        print("__________________________________")
        pet_name = input("Enter the name of your pet: ")
        pet_type = input("Enter the type of animal your pet is: ")
        pet_age = int(input("Enter the age of your pet (in years): "))

        # call the pet class and fill with users provided info: (creating an instance)
        pet = Pet(pet_name, pet_type, pet_age)

        # now display the user's information using the get functions within the pet class:
        print("__________________________________")
        print("\nYour pet's information: ")
        print("__________________________________")
        print(f"Pet name: {pet.get_pet_name()}")
        print(f"Pet type: {pet.get_pet_type()}")
        print(f"Pet age: {pet.get_pet_age()}")

        run_again = input("Would you like to enter information for another pet? (y/n): ")
        if run_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()

