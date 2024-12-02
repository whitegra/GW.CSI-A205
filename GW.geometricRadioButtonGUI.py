from tkinter import *

#set the window canvas dimensions
width = 400
height = 200

class GWGeometricRadioButtonsGUI:
    def displayFigure(self): #PUT THIS TO START
        """
    this will display the shape, either a circle or triangle, filled or not filled.
    """
        self.canvas.delete("shape") #delete the previous shape
        if self.v.get() == 1:  #1 = circle
            radius = min(width, height) * 0.5 #calculate the radius 0.5 = LOOKS GOOD
            if self.filled.get() == 1:  #fill the circle
                self.canvas.create_oval(
                    width / 2 - radius, height / 2 - radius,
                    width / 2 + radius, height / 2 + radius,
                    fill="blue", tags="shape" #create the cicle geometry, and tag it as a shape and fill it with blue(if filled)
                )
            else:  #if the circle isnt filled>>>
                self.canvas.create_oval(
                    width / 2 - radius, height / 2 - radius,
                    width / 2 + radius, height / 2 + radius,
                    tags="shape" #create the oval circle with no fill colow
                )
        elif self.v.get() == 2:  #the riangle = 2
            triangle_points = [
                width / 2, height / 2 - height * 0.3,  #this is to calculate the ertex at the top - 0.3 LOOKS OK
                width / 2 - width * 0.3, height / 2 + height * 0.3,  #here is to calculate the bottom ertex of the shape
                width / 2 + width * 0.3, height / 2 + height * 0.3  #this is for the bottom vertex at the bottom right
            ]
            if self.filled.get() == 1:  #triangle filled
                self.canvas.create_polygon(
                    triangle_points, fill="purple", tags="shape" #fill it and tag it as a shape
                )
            else:  #Unfilled triangle - I DONT KNOW WHY ITS BLACK but for this purpose black = unfilled 
                self.canvas.create_polygon(
                    triangle_points, tags="shape" #its just a shape with no color
                )

    def __init__(self):
        """this is to initialize the main window and widgets to call from the functions aboe for the shapes."""
        window = Tk()  #create the program window
        window.title("Circle or Triangle Geometric Figures")  #title of window
        
        #create and pack the canas for the window program
        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        #these are the frames to hold the radio buttons
        frame1 = Frame(window)
        frame1.pack()

        #these are the specific radio buttons to select the shape, which calls from the create shapes ones above
        self.v = IntVar()
        Radiobutton(frame1, text="create circle", variable=self.v, value=1, command=self.displayFigure).pack(side=LEFT) #circle is 1
        Radiobutton(frame1, text="create triangle", variable=self.v, value=2, command=self.displayFigure).pack(side=LEFT) #triangle is 2

        #here is a button i think a check button instead of radio, but its to fill the shape:
        self.filled = IntVar()
        Checkbutton(frame1, text="fill the shape", variable=self.filled, command=self.displayFigure).pack(side=LEFT)

        window.mainloop() #call the main event loop in the window to run the program
        
#just call the GUI program to run it since innit is above:
GWGeometricRadioButtonsGUI()

