from GWPersonalinfoClass import Personal_info

def main():
    # innitialize a list for the people
    people = []
    
    # for people in range (start at 1, inclusive 4 = 3):
    for i in range(1, 4):
        name = input(f"Enter the name of person {i}: ")
        age = int(input(f"Enter the age of person {i}: "))
        address = input(f"Enter the address of person {i}: ")
        phone_num = input(f"Enter the phone number for person {i}: ")

        #create an instance for that person:
        person = Personal_info(name, age, address, phone_num)

        #append the person to people list:
        people.append(person)

    # start at i = 1 because thats the index it starts with above:
    i = 1
    for person in people:
        print("________________________________________________")
        print(f"\n INFORMATION FOR PERSON #{i}: \n")
        print("________________________________________________")
        print(f"name : {person.get_name()}\n")
        print(f"age : {person.get_age()}\n")
        print(f"address : {person.get_address()}\n")
        print(f"phone number : {person.get_phone_num()}\n")
    # incriment i to print all the people's information:
    i += 1
        


if __name__ == "__main__":
    main()

        
        
        
        
        
