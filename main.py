import random
import turtle

#Create turtle objects for drawing
car = turtle.Turtle()
suv = turtle.Turtle()
truck = turtle.Turtle()
flr = turtle.Turtle()

# Set drawing speed and color
car.speed(20)
suv.speed(20)
truck.speed(20)
turtle.color("black")   # Set default drawing color
turtle.penup() #For precise positioning of the turtle before starting to draw lines initially 

# Generate random lengths for vehicles
car_length = 10 + 80 * random.random()
suv_length = 25 + 90 * random.random()
truck_length = 50 + 95 *random.random()


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
    car_length = 10 + 80 * random.random()  # Length of the car
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
    
    # Position for drawing the lower part of the car's body
    car.left(90)
    car.forward(car_length * 1 / 2)
    car.left(90)
    car.forward(car_length / 1.25)
    car.left(90)
    car.forward(car_length / 2)
    car.right(75)
    car.forward(car_length)
    car.left(75)
    car.forward(car_length / 2)
    car.left(75)
    car.forward(car_length)
    
    # Lift the pen after drawing the car
    car.penup()
    # Hide the turtle (car) after drawing
    car.ht()


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
    suv_length = 25 + 90 * random.random()  # Length of the SUV
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
    
    # Position for drawing the lower part of the SUV's body
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
    truck_length = 50 + 95 * random.random()  # Length of the truck
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


#Function for drawing the flowers
def draw_flr():
    # Lift the pen to avoid drawing while positioning the turtle
    flr.penup()
    # Loop to draw multiple flowers
    for i in range(8):
        flr.pendown()
        # Generate random color components for the flower
        red_amount = random.random()
        blue_amount = random.random()
        green_amount = random.random()
        # Set the fill color of the flower to a random RGB color
        flr.fillcolor(red_amount, green_amount, blue_amount)
        # Set drawing speed
        flr.speed(20)
        # Determine the length of the flower petals
        flower_length = 25 + 45 * random.random()
        # Begin the fill operation for the flower shape
        flr.begin_fill()
        # Draw the petals of the flower
        for i in range(9):
            flr.forward(flower_length)
            flr.left(160)
        # Complete the fill operation for the flower shape
        flr.end_fill()
        
        # Move to the next flower position
        flr.penup()
        flr.forward(flower_length * 1.5)  # Move to the next flower
        flr.forward(80)  # Move to the next flower position

#Function to position the turtle and draw flowers
def draw_flr1():
     flr.penup()
     flr.goto(-600, -250)
     draw_flr()

draw_car()

draw_suv()

draw_truck()

draw_flr1()

# Display inventory details
car_details = """The following car is in inventory:
Make: BMW
Model: 2001
Mileage: 70000
Price: $15000.0
Number of doors: 4"""
turtle.penup()
turtle.goto(-600, 200)  
turtle.write(car_details, align="left", font=("Arial", 10, "normal"))

suv_details = """The following SUV is in inventory:
Make: Volvo
Model: 2000
Mileage: 30000
Price: $18500.0
Passenger Capacity: 5"""
turtle.goto(0, 200)  
turtle.write(suv_details, align="center", font=("Arial", 10, "normal"))

truck_details = """The following truck is in inventory:
Make: Toyota
Model: 2002
Mileage: 40000
Price: $12000.0
Drive type: 4WD"""
turtle.goto(600, 200) 
turtle.write(truck_details, align="right", font=("Arial", 10, "normal"))

# Finish drawing
turtle.done()