import tkinter as t

class GWmoveTheBallGUI:
    def __init__(self):
        #create the main:
        self.main_window = t.Tk()
        self.main_window.title("Move the Ball GUI")

        #now to set the panel(canvas) with the dimensions and ball size:
        self.ball_r = 30 # this is the radius of the ball to not exceed the panel siz
        self.canvas_w = 500
        self.canvas_h = 400

        #now to create the widget for the canvas so the ball can be displayed:
        self.canvas = t.Canvas(
            self.main_window,
            width=self.canvas_w,
            height=self.canvas_h,
            bg="purple" #set the background color to be purple
        )
        self.canvas.pack() #now pack the widget to add it to the main window

        #CREATING THE BALL: (MUST BE CALLED ON THE CANVAS OBJECT)
        self.ball = self.canvas.create_oval(
            # ensure that the circle does not exceed the widgit size:
            self.canvas_w // 2 - self.ball_r, #this is for the left (x1)
            self.canvas_w // 2 + self.ball_r, #this is for the right (x2)
            self.canvas_h // 2 - self.ball_r, #this is for the top (y1)
            self.canvas_h // 2 + self.ball_r, #this is for the bototm (y2)
            fill="lavender" # fill it with the color
        )

        #now create the frame to hold the buttons to control the movement:
        button_move_frame = t.Frame(self.main_window)
        button_move_frame.pack() #add it to the main window

        #now define the style for the movement buttons (color, font, etc):
        button_move_style = {
            "font": ("Arial", 14, "bold"),  
            "bg": "lightblue",  
            "fg": "darkblue"  
        }

        #now to create the actual buttons:
        t.Button(button_move_frame, text="Left", command=self.move_left, **button_move_style).grid(row=0, column=0) #start at position in grid (0,0) for left
        t.Button(button_move_frame, text="Right", command=self.move_right, **button_move_style).grid(row=0, column=1) #move to (0,1) for right
        t.Button(button_move_frame, text="Down", command=self.move_down, **button_move_style).grid(row=1, column=1)#move to (1,1) for down
        t.Button(button_move_frame, text="Up", command=self.move_up, **button_move_style).grid(row=1, column=0) #move to (1,0) for up

        #start the main
        self.main_window.mainloop()

    # FUNCTIONS FOR MOVING THE BALL:

    #move the ball LEFT by 12 pixels method:
    def move_left(self):
        #first get the current coordinates of the ball
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        #then make sure the ball is within the left boundary (x1 > 0) so it dosent exceed the widgit size:
        if x1 > 0:
            self.canvas.move(self.ball, -12, 0)  #if its in the boundary, then move it by 12 pixels. 

    #move the ball RIGHT by 12 pixels method:
    def move_right(self):
        #same but for the right
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        #if the ball is within the right boundary (x2 < canvas width)
        if x2 < self.canvas_w:
            self.canvas.move(self.ball, 12, 0)  #then move the ball right by 12 pixels

    #move the ball UP by 12 pixels method:
    def move_up(self):
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        #if the ball is within the top boundary (y1 > 0)
        if y1 > 0:
            self.canvas.move(self.ball, 0, -10) #Move the ball up by 12pixels

    #move the ball DOWN by 12 pixels method:
    def move_down(self):
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        #if the ball is within the bottom boundary (y2 < canvas height)
        if y2 < self.canvas_h:
            self.canvas.move(self.ball, 0, 10)#then move ball down by 10 pixels

#create an instance of the GWmoveTheBallGUI class and run the program:
if __name__ == "__main__":
    GWmoveTheBallGUI() 


 
