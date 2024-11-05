import tkinter as t
from tkinter import messagebox

class GWradioButtonsGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = t.Tk()
        self.main_window.title("Radiobutton GUI")

        #make two frames, one for the Radiobuttons and another for the regular Button widgets
        self.top_frame = t.Frame(self.main_window, pady=10)
        self.bottom_frame = t.Frame(self.main_window, pady=10)

        #make an IntVar object to use with the Radiobuttons and set it to 1:
        self.radio_var = t.IntVar()
        self.radio_var.set(1)

        #create the Radiobutton widgets in the top_frame with new colors:
        self.rb1 = t.Radiobutton(
            self.top_frame,
            text='Option 1',
            variable=self.radio_var,
            value=1,
            font=("Helvetica", 12, "bold"), #set font and style
            bg="#ffc0cb",  #light pink background
            fg="#c2185b"   #dark pink text color
        )

        #same for the other two:
        self.rb2 = t.Radiobutton(
            self.top_frame,
            text='Option 2',
            variable=self.radio_var,
            value=2,
            font=("Helvetica", 12, "bold"),
            bg="#b2dfdb",  #light teal background
            fg="#00796b"   #dark teal text color
        )

        self.rb3 = t.Radiobutton(
            self.top_frame,
            text='Option 3',
            variable=self.radio_var,
            value=3,
            font=("Helvetica", 12, "bold"),
            bg="#e6e6fa",  #lavendar background
            fg="#4a148c"   #dark purpe text color
        )

        # then pack all of the radiobuttoons:
        self.rb1.pack(anchor='w', pady=2)
        self.rb2.pack(anchor='w', pady=2)
        self.rb3.pack(anchor='w', pady=2)

        #Then create an OK button and a Quit button with new colors:
        self.ok_button = t.Button(
            self.bottom_frame,
            text='OK',
            command=self.show_choice,
            font=("Verdana", 12, "bold"),
            bg="#ffc0cb",  #light pink background
            fg="#c2185b"   #dark pink text color
        )

        self.quit_button = t.Button(
            self.bottom_frame,
            text='Quit',
            command=self.main_window.destroy,
            font=("Verdana", 12, "bold"),
            bg="#e6e6fa",  #lavndar background
            fg="#4a148c"   #dark purple text color
        )

        #now pack the quit and ok buttons seperate from the radiobuttons:
        self.ok_button.pack(side='left', padx=5)
        self.quit_button.pack(side='left', padx=5)

        #pack the entire frame:
        self.top_frame.pack()
        self.bottom_frame.pack()

        #here is to start the main event loop:
        t.mainloop()

    # The show_choice method displays the selected option.
    def show_choice(self):
        """ This will show the choice methods to display the user's selected button choice """
        choice = self.radio_var.get()
        messagebox.showinfo("Button Selection", f"You selected Option {choice}.") #this will return the button the user chose

#run the GUI.
if __name__ == '__main__':
    GWradioButtonsGUI()
