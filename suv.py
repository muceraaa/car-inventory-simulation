import random
import turtle

#Create turtle objects for drawing
suv = turtle.Turtle()

# Set drawing speed and color
suv.speed(0)
turtle.tracer(1,0) # Skip animation of drawing

turtle.color("black")   # Set default drawing color
turtle.penup() #For precise positioning of the turtle before starting to draw lines initially 

# Generate random lengths for vehicles
a = 25
b = 90
u = random.random()
suv_length =a + u * (b -a)

#Function for drawing the suv
def draw_suv():
    # Lift the pen to avoid drawing while positioning the turtle
    suv.penup()
    # Move the turtle to the starting position to draw the SUV
    suv.goto(-350, 0)
    
    # Generate random color components for the SUV
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()
    
    # Lower the pen to start drawing
    suv.pendown()
    # Set the fill color of the SUV to a random RGB color
    suv.fillcolor(red_amount, green_amount, blue_amount)
    # Begin the fill operation for the SUV shape
    suv.begin_fill()
    
    # Draw the main body of the SUV
    suv_length =a + u * (b -a)
    suv.forward(suv_length * 2)
    suv.left(90)
    suv.forward(suv_length / 1.25)
    suv.left(90)
    suv.forward(suv_length * 2)
    suv.left(90)
    suv.forward(suv_length / 1.25)
    
    suv.end_fill() # End the fill operation
    
    # Draw the first wheel of the SUV
    suv.left(90)
    suv.forward(suv_length / 4)
    suv.right(90)
    suv.forward(suv_length / 8)
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle(suv_length / 5)  # Radius of the first wheel
    suv.end_fill()
    suv.back(suv_length / 8)
    
    # Move to position for drawing the second wheel
    suv.left(90)
    suv.forward(suv_length * 1.25)
    suv.right(90)
    suv.forward(suv_length / 8)
    
    # Draw the second wheel of the SUV
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle(suv_length / 5)  # Radius of the second wheel
    suv.end_fill()
    suv.back(suv_length / 8)
    
    # Position for drawing the roof of the suv
    suv.left(90)
    suv.forward(suv_length * 0.5)
    suv.left(90)
    suv.forward(suv_length / 1.25)
    suv.left(90)
    suv.forward(suv_length / 2)
    suv.right(90)
    suv.forward(suv_length * 0.75)
    suv.left(90)
    suv.forward(suv_length * 0.75)
    suv.left(90)
    suv.forward(suv_length * 0.75)
    suv.right(90)
    suv.forward(suv_length * 0.75)
    suv.right(90)
    suv.forward(suv_length * 0.75)
    suv.right(90)
    suv.forward(suv_length * 0.75)
    
    # Lift the pen after drawing the SUV
    suv.penup()
    # Hide the turtle (SUV) after drawing
    suv.ht()

draw_suv()
