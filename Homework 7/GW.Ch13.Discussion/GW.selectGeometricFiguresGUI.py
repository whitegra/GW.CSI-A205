from tkinter import *  # Import tkinter

# Set canvas dimensions
width = 300
height = 50

class GWselectGeometricFiguresGUI:
    def displayFigure(self):
        """Display either a rectangle or an oval, filled or unfilled based on user selection."""
        self.canvas.delete("shape")
        if self.filled.get() == 1:  # Check if filled option is selected
            if self.v.get() == 1:  # Rectangle selected
                self.canvas.create_rectangle(
                    width / 2 - width * 0.4, height / 2 - height * 0.4,
                    width / 2 + width * 0.4, height / 2 + height * 0.4,
                    fill="purple", tags="shape"
                )
            else:  # Oval selected
                self.canvas.create_oval(
                    width / 2 - width * 0.4, height / 2 - height * 0.4,
                    width / 2 + width * 0.4, height / 2 + height * 0.4,
                    fill="blue", tags="shape"
                )
        else:
            if self.v.get() == 1:  # Rectangle unfilled
                self.canvas.create_rectangle(
                    width / 2 - width * 0.4, height / 2 - height * 0.4,
                    width / 2 + width * 0.4, height / 2 + height * 0.4,
                    tags="shape"
                )
            else:  # Oval unfilled
                self.canvas.create_oval(
                    width / 2 - width * 0.4, height / 2 - height * 0.4,
                    width / 2 + width * 0.4, height / 2 + height * 0.4,
                    tags="shape"
                )

    def left(self):
        """Move shape text to the left."""
        self.canvas.move("text", -5, 0)

    def right(self):
        """Move shape text to the right."""
        self.canvas.move("text", 5, 0)

    def __init__(self):
        """Initialize the main window and widgets."""
        window = Tk()  # Create a window
        window.title("Radiobuttons and Checkbuttons")  # Set title
        
        # Create and pack the canvas
        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.create_rectangle(
            width / 2 - width * 0.4, height / 2 - height * 0.4,
            width / 2 + width * 0.4, height / 2 + height * 0.4,
            tags="shape"
        )
        self.canvas.pack()

        # Create a frame to hold radio buttons and check button
        frame1 = Frame(window)
        frame1.pack()

        # Radio buttons for selecting shape
        self.v = IntVar()
        Radiobutton(frame1, text="Rectangle", variable=self.v, value=1, command=self.displayFigure).pack(side=LEFT)
        Radiobutton(frame1, text="Oval", variable=self.v, value=2, command=self.displayFigure).pack(side=LEFT)

        # Checkbutton for filled option
        self.filled = IntVar()
        Checkbutton(frame1, text="Filled", variable=self.filled, command=self.displayFigure).pack(side=LEFT)

        window.mainloop()  # Create an event loop

# Run the GUI application
GWselectGeometricFiguresGUI()
