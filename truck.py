import random
import turtle

#Create turtle objects for drawing
truck = turtle.Turtle()

# Set drawing speed and color
truck.speed(0)
turtle.tracer(1,0) # Skip animation of drawing

turtle.color("black")   # Set default drawing color
turtle.penup() #For precise positioning of the turtle before starting to draw lines initially 

# Generate random lengths for vehicles
a = 30
b = 95
u = random.random()
truck_length =a + u * (b -a)

#Function to draw the truck
def draw_truck():
    # Lift the pen to avoid drawing while positioning the turtle
    truck.penup()
    # Move the turtle to the starting position to draw the truck
    truck.goto(200, 0)
    
    # Generate random color components for the truck
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()
    
    # Lower the pen to start drawing
    truck.pendown()
    # Set the fill color of the truck to a random RGB color
    truck.fillcolor(red_amount, green_amount, blue_amount)
    # Begin the fill operation for the truck shape
    truck.begin_fill()
    
    # Draw the main body of the truck
    truck_length =a + u * (b -a)
    truck.forward(truck_length * 2)
    truck.left(90)
    truck.forward(truck_length)
    truck.left(90)
    truck.forward(truck_length * 2)
    truck.left(90)
    truck.forward(truck_length)
    truck.left(90)
    truck.forward(3 * truck_length)
    truck.left(90)
    truck.forward(truck_length * 0.5)
    truck.left(90)
    truck.forward(truck_length)

    #truck.end_fill() # End the fill operation
    
    # Draw the first wheel of the truck
    truck.back(0.5 * truck_length)
    truck.right(90)
    truck.forward(0.3 * truck_length)
    truck.right(90)
    truck.forward(0.5 * truck_length)
    truck.right(90)
    truck.forward(0.8 * truck_length)
    truck.right(90)
    truck.end_fill()
    truck.forward(0.5 * truck_length)
    
    # Draw the second wheel of the truck
    truck.left(90)
    truck.forward(truck_length / 8)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 5)  # Radius of the second wheel
    truck.end_fill()
    truck.back(truck_length / 8)
    
    # Draw the third wheel of the truck
    truck.right(90)
    truck.forward(1.5 * truck_length)
    truck.left(90)
    truck.forward(truck_length / 8)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 5)  # Radius of the third wheel
    truck.end_fill()
    truck.back(truck_length / 8)
    
    # Draw the fourth wheel of the truck
    truck.right(90)
    truck.forward(0.5 * truck_length)
    truck.left(90)
    truck.forward(truck_length / 8)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 5)  # Radius of the fourth wheel
    truck.end_fill()
    truck.back(truck_length / 8)
    
    # Hide the turtle (truck) after drawing
    truck.hideturtle()
    # Lift the pen after drawing the truck
    truck.penup()

draw_truck()
