import tkinter as t
import math

class GWstillAndRunningFanGUI:
    def __init__(self):
        #create the main window
        self.window = t.Tk()
        #add title
        self.window.title("Move the Fan")
        #set the background to lavender
        self.window.config(bg="#E6E6FA")

        #first, initialize  the fan properties (angle, speed, running (y/n), and the color:
        self.angle = 0  #initial angle is zero (still)
        self.speed = 0  #innitial speed is zero (still)
        self.running = False  #not running at first
        self.fan_color = "#73737d"  #make the blade color

        #create GUI qidgets and start the main loop:
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        """Purpose: Creates the input fields, buttons, and frames for the GUI program using canvas."""
        #create the canvas to display the fan
        self.canvas = t.Canvas(self.window, width=600, height=600, bg="#E6E6FA")
        self.canvas.pack(pady=20)

        #Draw the initial fan (still)
        self.draw_fan()

        #Create the frame to hold the buttons and set the bg color
        button_frame = t.Frame(self.window, pady=15, bg="#CDCDFA")  #match lavender background
        button_frame.pack() #pack button

        #START BUTTON
        start_button = t.Button(button_frame, text="Start the Fan", command=self.start_fan)
        start_button.pack(side='left', padx=10) #make all the buttons left side

        #INCREASE SPEED BUTTON
        increase_button = t.Button(button_frame, text="Increase Fan Speed", command=self.increase_speed)
        increase_button.pack(side='left', padx=10)

        #DECREASE SPEED BUTTON
        decrease_button = t.Button(button_frame, text="Decrease Fan Speed", command=self.decrease_speed)
        decrease_button.pack(side='left', padx=10)

        #STOP BUTTON
        stop_button = t.Button(button_frame, text="Stop the Fan", command=self.stop_fan)
        stop_button.pack(side='left', padx=10)


    def draw_fan(self):
        """Purpose: Draws the fan blades based on the current angle, speed, and if the fan is on or off."""
        self.canvas.delete("all")  #First, clear the previous canvas

        #calculate the center and radius for the fan blades
        center_x, center_y = 300, 300  #center coordinates of the canvas
        radius = 200 #radius of the canvas (how far the blades extend from the center)

        #Now to draw the 4 fan blades using polygons (triangular sectors) and using the math library for the movement angles.
        for i in range(4):
            angle = math.radians(self.angle + i * 90)  #There are 4 blades, and each are 90 degrees apart to make the full circle

            #Now to calculate the points for the triangular blades
            x1 = center_x + radius * math.cos(angle) #x1 and y1 are the first vertex for each blade (in range 4) starting from the radius and extending out
            y1 = center_y + radius * math.sin(angle) 

            x2 = center_x + radius * math.cos(angle + math.radians(30)) #x2 and y2 is the second vertex, 30 degrees forward from the origional ones to make a triangle blade.
            y2 = center_y + radius * math.sin(angle + math.radians(30))

            #now to create the polygons (blades):
            self.canvas.create_polygon(
                center_x, center_y, x1, y1, x2, y2,
                fill=self.fan_color  #fill with the predefined fan color
            )

    def start_fan(self):
        """Purpose: Starts the fan moving."""
        if not self.running:  # If the fan is not already running
            self.running = True #then start running it (set self.running = True)
            self.update_fan() #update the fan condition

    def stop_fan(self):
        """Purpose: Stops the fan."""
        self.running = False  # Set running to False

    def increase_speed(self):
        """Purpose: Increases the speed of the fan by 5 units."""
        self.speed += 5  #Increase speed by 5 units if increase speed is clicked by the user

    def decrease_speed(self):
        """Purpose: Decreases the speed of the fan by 5 units."""
        if self.speed > 0:
            self.speed -= 5  # Decrease speed by 5 units

    def update_fan(self):
        """Purpose: Updates the fan's rotation and redraws it at the new angle as it is in movement based on the selected speed."""
        if self.running:
            self.angle = (self.angle + self.speed) % 360  # Update the angle and ensure that it stays within 360 rotation using modulo
            self.draw_fan()  #then redraw the fan with the new angle to simulate movement
            #This is to schedule the next update of movement based on the speed of the fan
            self.window.after(50, self.update_fan) #this will update the fan speed and angle after 50 miliseconds

# Run the program
if __name__ == "__main__":
    GWstillAndRunningFanGUI()


