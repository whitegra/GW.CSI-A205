import tkinter as t
from tkinter import messagebox

class GWtempConverterGUI:
    def __init__(self):
        #create the main window in t:
        self.main_window = t.Tk()
        self.main_window.title("Temperature Converter")  #set the title of the window to the name of the program
        
        #two frames to group widgets, top and bottom:
        self.top_frame = t.Frame(self.main_window, pady=10) #create the top and pad by 10
        self.bottom_frame = t.Frame(self.main_window, pady=10) #create the bottom and pad by 10

        #Now create the entry point widget and lables for user to enter the temp:
        t.Label(
            self.top_frame, 
            text='Enter a temperature to convert:', #prompt for entry (txt)
            font=("Verdana", 14) #set the font and size
        ).pack(side='left') #pack it to the left

        #create the entry frame and set the font, size, and pack:
        self.temp_entry = t.Entry(self.top_frame, width=10, font=("Verdana", 12))
        self.temp_entry.pack(side='left')

        #now define the option buttons and set the button colors:
        option_buttons = [
            ("Fahrenheit -> Celsius", self.f_to_c, 'blue'),
            ("Celsius -> Fahrenheit", self.c_to_f, 'purple'),
            ("Exit Program", self.main_window.destroy, 'red') #exit if quit is chosen
        ]

        #now create a for loop to create the buttons and to pack them all together:
        for text, command, bg in option_buttons: #for the text, commands, and backgorund (button color) in the buttons:
            t.Button(
                self.bottom_frame, 
                text=text, 
                command=command, 
                bg=bg, 
                fg='black' if bg == 'red' else 'white', #make the text on quit button black, make the rest of the text white
                font=("Verdana", 12, "bold") #set the font, size, and make it bolded
            ).pack(side='left', padx=5)#pack it to the left and pad the x by 5

        #noe pack all the frames, top and bottom:
        self.top_frame.pack()
        self.bottom_frame.pack()

        #now execute the main loop:
        t.mainloop()

    #CONERSION FUNCTIONS:
    def f_to_c(self):
        # start with a try in case an invalid entry is entered so the program dosent break:
        try:
            f = float(self.temp_entry.get()) #get the temp as float
            c = (f - 32) * 5/9 #convert
            self.show_conversion(f, 'F', c, 'C')
        except ValueError: # if there is an error than pass it to the helper function to display the error:
            self.show_error()

    #same for the other conversion function:
    def c_to_f(self):
        try:
            c = float(self.temp_entry.get())
            f = (c * 9/5) + 32
            self.show_conversion(c, 'C', f, 'F')
        except ValueError:
            self.show_error()

    #This is the show conversion function to return the conversion and origional entry in the proper format for degrees:
    def show_conversion(self, from_value, from_unit, to_value, to_unit):
        messagebox.showinfo( #use the messagebox helper
            "Results", 
            f"{from_value}°{from_unit} = {to_value:.2f}°{to_unit}"
        )

    #here is teh function to display the error if there is one using the same messagebox method as the other helper function:
    def show_error(self):
        messagebox.showerror("Invalid.", "Re-enter a valid temperature.")

#Run the application.
if __name__ == '__main__':
    GWtempConverterGUI()
