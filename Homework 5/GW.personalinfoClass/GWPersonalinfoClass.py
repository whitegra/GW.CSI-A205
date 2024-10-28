class Personal_info:
    def __init__(self, name, age, address, phone_num):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone_num = phone_num

    #def SET name
    def set_name(self, name):
        self.__name = name

    #def for GET name
    def get_name(self):
        return self.__name

    #def for SET age
    def set_age(self, age):
        self.__age = age

    # def for GET age
    def get_age(self):
        return self.__age

    #def for SET address
    def set_address(self, address):
        self.__address = address

    #def for GET address
    def get_address(self):
        return self.__address

    #def for SET phone_num
    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    #def for GET phone_num
    def get_phone_num(self):
        return self.__phone_num
    
    
