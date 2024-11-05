from tkinter import *  # Import tkinter
import math

#canvas and pendulum dimensions
width = 200
height = 200
pendulumRadius = 150
ballRadius = 10
leftAngle = 120
rightAngle = 60

class GWpendulumGUI:
    def __init__(self):
        """Initialize the main window and set up the pendulum animation."""
        window = Tk()  #Create a window
        window.title("Pendulum")  # Set title
        
        # Create and pack the canvas
        self.canvas = Canvas(window, bg="pink", width=width, height=height)
        self.canvas.pack()

        # Initialize pendulum angle and swing direction
        self.angle = leftAngle  # Start at the left angle
        self.angleDelta = 1  # Initial swing interval

        # Animation loop
        self.animate()

        window.mainloop()  # Create an event loop

    def animate(self):
        """Animate the pendulum by updating its position at set intervals."""
        while True:
            # Clear previous pendulum drawing
            self.canvas.delete("pendulum")
            # Draw the current state of the pendulum
            self.displayPendulum()
            # Delay for 100 milliseconds
            self.canvas.after(100)
            # Update the canvas
            self.canvas.update()

    def displayPendulum(self):
        """Calculate the pendulum's position and display it on the canvas."""
        # Define pivot point coordinates
        x1 = width / 2
        y1 = 20

        # Update angle direction if it reaches limits
        if self.angle < rightAngle:
            self.angleDelta = 1  # Swing back to the left
        elif self.angle > leftAngle:
            self.angleDelta = -1  # Swing back to the right

        # Update the pendulum's angle
        self.angle += self.angleDelta

        # Calculate the pendulum bob's position
        x = x1 + pendulumRadius * math.cos(math.radians(self.angle))
        y = y1 + pendulumRadius * math.sin(math.radians(self.angle))

        # Draw the pendulum arm
        self.canvas.create_line(x1, y1, x, y, tags="pendulum")
        
        # Draw the pivot point
        self.canvas.create_oval(x1 - 2, y1 - 2, x1 + 2, y1 + 2, fill="black", tags="pendulum")
        
        # Draw the pendulum bob
        self.canvas.create_oval(x - ballRadius, y - ballRadius, x + ballRadius, y + ballRadius,
                                fill="black", tags="pendulum")

# Run the pendulum simulation
GWpendulumGUI()
