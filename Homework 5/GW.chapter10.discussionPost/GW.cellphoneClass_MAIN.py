
class CellPhone:
    def __init__(self, manufact, model, retail_price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = retail_price

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

#For simplicity I am putting it all in one program.

def main():
    # Get a list of Phone objects.
    phone_inventory = create_phone_list()

    print("\nThe following data was entered:")
    show_phone_list(phone_inventory)

# The create_phone_list function gets data from the user
# for five phones. The function returns a list of the entered data
def create_phone_list():
    # Innitialize phone to an empty list
    phones = []

    # Add five Phone objects to the list.
    print("Enter details for five phones:")
    for i in range(1, 6):
        print(f"\nPhone {i}:")

        # Get the phone details.
        manufacturer = input("Enter the brand: ")
        model = input("Enter the model: ")
        price = float(input("Enter the price: "))

        # Create a new Phone object in memory and
        # assign it to the phone variable.
        phone = CellPhone(manufacturer, model, price)

        # Add the object to the list.
        phones.append(phone)

    
    return phones


# display data stored in each object.
def show_phone_list(phone_inventory):
    for phone in phone_inventory:
        print("Brand:", phone.get_manufact())
        print("Model:", phone.get_model())
        print(f"Price: ${phone.get_retail_price():,.2f}")

if __name__ == '__main__':
    main()
