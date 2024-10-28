from GWcarClass import Car
# main function
def main():
    while True:
        print("________________________________________")
        year_model = int(input("Enter the model (in year) of your car: "))
        make = input("Enter the make of your car: ")

        #create an instance of the class with the user's information:
        user_car = Car(year_model, make)

        # first, accelerating:
        print("\nACCELERATING")
        for _ in range(5):
            user_car.acceleration() # accelerate the user's car 5 times
            # print each speed for range(5):
            print(f"Current speed of {year_model} {make} = {user_car.get_speed()}")
            print("_______________________________________________________________________")

        #then deaccelerate / breaking:
        print("\nBREAKING")
        for _ in range(5):
            user_car.breaking() #break 5 times
            #print each speed with each break:
            print(f"Current breaking speed of {year_model} {make} = {user_car.get_speed()}")
            print("_______________________________________________________________________")

        run_again = input("\nWould you like to run again? (y/n): ")
        if run_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
    
            
            
            

        
