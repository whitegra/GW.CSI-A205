import tkinter as t  
from random import randint

width = 300
height = 150
radius = 4

# Convert an integer to a single hex digit as a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # hexValue is between 10 and 15
        return chr(hexValue - 10 + ord('A'))

class GWrandomBallsGUI:
    def __init__(self):
        window = t.Tk()  # Create a window
        window.title("Random Balls")  # Set title

        self.canvas = t.Canvas(window, width=width, height=height)
        self.canvas.pack()

        t.Button(window, text="Display", command=self.display).pack()

        window.mainloop()  # Create an event loop

    def display(self):
        self.canvas.delete("ball")  # Clear previous balls

        for i in range(10):
            x = randint(0, width - 1)
            y = randint(0, height - 1)
            color = "#"
            for j in range(6):
                color += toHexChar(randint(0, 15))  # Create random hex color
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, tags="ball")

# Run the GUI()
GWrandomBallsGUI()
