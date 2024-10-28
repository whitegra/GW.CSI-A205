# https://docs.python.org/3/library/turtle.html - used this source as well
# first import the turtle library:
import turtle as t

def draw_base(t, x, y, r, base_color):
    """
    purpose: will draw the snowman base
    inputs: turtle, x, y, radius, fill color
    output: will draw the base of snowman
    """
    t.penup() # lift pen to begin drawing
    bottom_y_base = y - r #bottom in y coordinate
    t.goto(x, bottom_y_base) #go to the bottom to begin drawing
    t.pendown() #put pen down to draw
    t.fillcolor(base_color)# fill shape with base color, YOU HAVE TO DO THIS BEFORE DRAWING CIRCLE
    t.begin_fill() # start coloring the circle
    t.circle(r)
    t.end_fill() # end fill will fill the circle and end this function

def draw_mid_section(t, x, y, r, mid_color):
    """
    purpose: will draw and fill the mid section of snowman
    inputs: turtle, x, y, radius(r), and the color
    output: will draw and fill the mid section
    """
    mid_r = r * 0.80# the radius of mid section is 80% size radius of bottom to be smaller
    t.penup() #lift
    t.goto(x, y + mid_r) # this will start at the bottom of the midsection above the base(+) to y
    t.pendown() #pen
    t.fillcolor(mid_color)
    t.begin_fill() # start the fill BEFORE SHAPE
    t.circle(mid_r) # the circle will be 80% of base radius to be smaller
    t.end_fill() # end the fill to draw circle and color it

def draw_arms(t, x, y, r, arm_color):
    """
    purpose: to draw the arms
    inputs: same except arm color
    output: arms on mid section
    """
    #define the measurments for the arm radius(s)
    arm_r_start_x = r * 0.69 # start a little before or else the snowman has floating arms
    arm_r_start_y = r *1.3 #can start at midsection r for y
    arm_r_draw_x = r * 1.4 # extend to 1.4 * the radius of base for arm x axis
    arm_r_draw_y = r * 1.5 # extent to 1.5 * the radius of base for y (a little smaller than the length)
    t.penup() #penup
    t.pencolor(arm_color)
    # LEFT ARM
    t.goto(x - arm_r_start_x, y + arm_r_start_y) # go to the start coordinates
    t.pendown() # pen down to begin
    t.goto(x - arm_r_draw_x, y + arm_r_draw_y) # FOR LEFT ARM, - X TO START ON LEFT SIDE
    # RIGHT ARM
    t.penup() #LIFT PEN to begin drawing the right arm on the other side, so start at origin
    t.goto(x + arm_r_start_x, y + arm_r_start_y) # start at the origin again, but + to x
    t.pendown() # start drawing the other arm now
    t.goto(x + arm_r_draw_x, y + arm_r_draw_y) # now, draw the right arm

def draw_head(t, x, y, r, head_color, eye_color):
    """
    purpose: to draw the head, face, and eyes 
    inputs: same + head color and eye color
    output: the head with the face and eyes 
    """
    head_r = r * 0.6 # the head is 60% the size of the base to be smaller
    t.penup() # lift pen
    t.goto(x, y + r * 2.2) # go to (start drawing) at the bottom of the head, mid is 0.8, *2 = 1.6 * r + y coordinate
    t.pendown()
    t.fillcolor(head_color) # fill w/ headcolor
    t.begin_fill() # innitialize the fill before drawing the circle
    t.circle(head_r) # draw circle with the head radius
    t.end_fill() # end this shape after filling
    # MOUTH
    t.penup()
    t.goto(x - r * 0.15, y + r * 2.6) # go to 1.8 - 1.65 for y coordinate = 0.15 x because mid = 0.8%
    t.pendown()
    t.setheading(-90) # SETHEADING WILL SET THE START, -90 to ensure the face is the right direction NOT 90
    t.circle(r * 0.15, 180) # start at the x, then 180 for a half circle shape mouth, not going to fill it
    # EYES
    eye_r = r * 0.06 #this will be the radius of eye circles
    #RIGHT EYE
    t.penup()
    t.goto(x + r * 0.2, y + r * 2.9) # eye x = 1/3 head r, eye y = 0.22 high
    t.pendown() # put pen down to begin drawinf
    t.fillcolor(eye_color)
    t.begin_fill() # innitialize
    t.circle(eye_r) # draw circle with eye radius
    t.end_fill() # end the right eye fill and draw
    # LEFT EYE
    t.penup()
    t.goto(x - r * 0.2, y + r * 2.9) # eye x = 1/3 head r, eye y = 0.22 high, but - x to start at left side 
    t.pendown() # put pen down to begin drawinf
    t.fillcolor(eye_color)
    t.begin_fill() # innitialize
    t.circle(eye_r) # draw circle with eye radius
    t.end_fill() # end the right eye fill and draw

def draw_hat(t, x, y, r, hat_color):
    """
    purpose: to draw the hat as two seperate shapes
    inputs: same + hat color
    output: will draw and fill the hat
    """
    # FOR THE BRIM RECTANGLE
    t.penup()
    t.setheading(0) # ensure the hat is drawn horizontally
    t.goto(x - r * 0.4, y + r * 3.2) # go to (start at) x bottom corner and start y a little above the center 1.6
    t.pendown() # pen down to begin
    t.fillcolor(hat_color)
    t.begin_fill() # innitialize the fill before the circle
    # there are two sides, so there needs to be a loop to draw both sides of the rectange shape for brim:
    for _ in range(2): # USE _ INSTEAD OF i HERE since its a shape
        t.forward(r *0.8) # move forward for the entire length of brim on head
        t.left(90) # after that, move 90 degrees left to rotate to draw the height/ thickness of hat brim
        t.forward(r * 0.12) #80 - length = h = 0.1
        t.left(90) # move left again to meet the other side to make the rectange solid shape
    t.end_fill() # end the fill OUTSIDE LOOP now that all sides are drawn
    # FOR THE TOP RECTANGE PART IN HAT:
    t.penup()
    t.goto(x - r *0.3, y + r *3.3) #start left, start at bottom corner and make the hat tall
    t.pendown()
    t.begin_fill()
    # same thing with the loop for both sides of hat to connect:
    for _ in range(2):
        t.forward(r * 0.6) # move forward for length (a little smaller than the brim)
        t.left(90) # move left to draw the other side (height)
        t.forward(r * 0.6) # the body of hat height
        t.left(90) # turn back aronund to connect the lines in a rectangle for top of hat shape
    t.end_fill() # end the fill OUTSIDE loop

def main():
    #you have to create a screen in turtle
    screen = t.Screen() # this will create the turtle screen to draw the object (snowman)
    screen.bgcolor("pink") # this is for the screen's background color
    # USER INPUT: (MUST USE screen.textinput instead of input for turtle
    r = int(screen.textinput("RADIUS", "Enter the radius for the base of the snowman: "))
    # FOR COLORS, YOU HAVE TO USE A PROMPT
    base_color = screen.textinput("BASE:", "Enter the base color: ")
    mid_color = screen.textinput("MID-SECTION", "Enter the mid-section color: ")
    arm_color = screen.textinput("ARMS", "Enter the arms color: ")
    head_color = screen.textinput("HEAD", "Enter the head color: ")
    eye_color = screen.textinput("EYES", "Enter the eye color: ")
    hat_color = screen.textinput("HAT", "Enter the hat color: ")
    # now, to create the turtle object by assigning it to variable t
    snowman = t.Turtle()
    t.speed(5) # this is to set the speed of turtle so it dosen't take 10 years
    # now set the coordinates to start the turtle object, start at x coordinate, 0 height(y), and -r for center
    x, y = 0, -r
    # TO ACTUALLY DRAW
    draw_base(snowman, x, y, r, base_color)
    draw_mid_section(snowman, x, y, r, mid_color)
    draw_arms(snowman, x, y, r, arm_color)
    draw_head(snowman, x, y, r, head_color, eye_color)
    draw_hat(snowman, x, y, r, hat_color)
    #now, turtle.done() will show the finished drawing
    t.done()

main()
    
    
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
