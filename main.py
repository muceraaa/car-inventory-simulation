import random
import turtle
import car
import suv
import truck
import flowers

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