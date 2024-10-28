class Car: #CLASSES MUST BE CAPITALIZED FOR INSTANCES.
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0 # speed is innitialized to zero

    # def for the acceleration
    def acceleration(self):
        self.__speed += 5 #add 5 to speed for each acceleration

    # def for breaking (subtract speed until it gets to zero):
    def breaking(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0 #cant have negative speed.

    # function to GET the speed and return it:
    def get_speed(self):
        return self.__speed
