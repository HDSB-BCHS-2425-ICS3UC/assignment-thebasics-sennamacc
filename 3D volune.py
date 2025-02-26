"""
Author: Senna Chan Carusone
Date Modified: February 26th, 2025
Description: Calculating the volume of 3D shapes based on user input.
"""
#SETUP
import math

#MAIN CODE
#first we need to ask the user what shape we're doing, so we know what formula to use
print("I'm here to help you calculate the volume of a 3D shape!")
shape = input("Before we start, what shape are we going to be working with today?\n")
shape = shape.lower()
if shape == "cube": #finding the volume for if it's a cube
    print("Okay, great, let's find the are of your cube :)")
    length = input("Please input the length:\n") #user input
    length = float(length)
    volume = length*length*length #calculate
    print("Thanks. The volume is ",volume) #print answer
elif shape == "sphere": #finding the volume for if it's a sphere
    print("Awesome, let's find the area of your sphere.")
    radius = input("Please input the radius:\n") #user input
    radius = float(radius)
    volume = (4/3)*(math.pi)*(radius**2) #calculate
    print("Okey dokey. The volume is ",volume) #print answer
elif shape == "cone": #finding the volume for if it's a cone
    print("Do you want some ice cream with your cone?\nI'm joking, I can't give you ice cream, I can only do math.")
    radius = input("What's the radius?\n")
    height = input("Thanks, and what's the height?\n") #user input
    radius = float(radius)
    height = float(height)
    volume = (1/3)*(math.pi)*(radius**2)*(height) #calculate
    print("The volume of your cone is ",volume) #print answer
    if volume > 20:
        print("You could fit a lot of ice cream in that cone!")
    else:
        print("Oh. You could not fit a lot of ice cream in that cone...")
elif shape == "cylinder":
    print("Alright, let's find the volume of your cylinder.")
    radius = input("Please input the radius of the base of the cylinder\n:")
    height = input("And please input the height:\n") #user input
    radius = float(radius)
    height = float(height)
    volume = (math.pi)*(radius**2)*(height) #calculate
    print("The volume of your cylinder is ",volume)
else:
    print("I'm sorry, I don't know that shape yet.")