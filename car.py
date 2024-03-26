import random
import turtle

#Create turtle objects for drawing
car = turtle.Turtle()

# Set drawing speed and color
car.speed(0)
turtle.tracer(1,0) # Skip animation of drawing

turtle.color("black")   # Set default drawing color
turtle.penup() #For precise positioning of the turtle before starting to draw lines initially 

# Generate random lengths for vehicles
a = 20
b = 80
u = random.random()
car_length =a + u * (b -a)


#Function for drawing the car
def draw_car():
    # Lift the pen to avoid drawing while positioning the turtle
    car.penup()
    # Move the turtle to the starting position to draw the car
    car.goto(-600, 0)
    
    # Generate random color components for the car
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()
    
    # Lower the pen to start drawing
    car.pendown()
    # Set the fill color of the car to a random RGB color
    car.fillcolor(red_amount, green_amount, blue_amount)
    # Begin the fill operation for the car shape
    car.begin_fill()
    
    # Draw the main body of the car
    car_length =a + u * (b -a)
    car.forward(car_length * 2)
    car.left(90)
    car.forward(car_length / 1.25)
    car.left(90)
    car.forward(car_length * 2)
    car.left(90)
    car.forward(car_length / 1.25)
    
    car.end_fill() # End the fill operation

    # Draw the first wheel of the car
    car.left(90)
    car.forward(car_length / 4)
    car.right(90)
    car.forward(car_length / 8)
    car.fillcolor('black')
    car.begin_fill()
    car.circle(car_length / 5)  # Radius of the first wheel
    car.end_fill()
    car.back(car_length / 8)
    
    # Move to position for drawing the second wheel
    car.left(90)
    car.forward(car_length * 1.25)
    car.right(90)
    car.forward(car_length / 8)
    
    # Draw the second wheel of the car
    car.fillcolor('black')
    car.begin_fill()
    car.circle(car_length / 5)  # Radius of the second wheel
    car.end_fill()
    car.back(car_length / 8)
    
    # Position for drawing the roof of the car
    car.left(90)
    car.forward(car_length * 1 / 2)
    car.left(90)
    car.forward(car_length / 1.25)
    car.left(90)
    car.forward(car_length / 2)
    car.right(75)
    car.forward(car_length / 1.75)
    car.left(75)
    car.forward(car_length /2)
    car.left(90)
    car.forward(car_length / 1.75)
    car.left(180)
    car.forward(car_length /1.75)
    car.left(90)
    car.forward(car_length /2)
    car.left(75)
    car.forward(car_length / 1.75)

    # Lift the pen after drawing the car
    car.penup()
    # Hide the turtle (car) after drawing
    car.ht()

draw_car()