"""
Author: Senna Chan Carusone
Date Modified: February 26th, 2025
Description: A program to calculate the discriminant, which is b^2 – 4ac (from the quadratic formula)
"""
#Explaining to user via inital print statements
print("I will help you calculate discriminant. The discriminant is used in finding roots (aka zeros) of a quadratic.")
print("If it produces a negative number, there are no roots. If it produces zero, there is one root. And if it produces a positive number, there are two roots.")
print("To calculate the discriminant, we need a quadratic in standard form, which is ax^2 + bx + c")
print("You can now input values for a, b, and c, and I'll give you the answer by subbing your values into the discriminant.")

#Getting user input
a = float(input("Please input the value for a:\n"))
b = float(input("Please input the value for b:\n"))
c = float(input("Please input the value for c:\n"))
print("Thank you!")

#Calculating
discriminant = b**2 - 4*a*c

#Printing solution
print("Discriminant =",discriminant)

#Checking the number of roots
if discriminant > 0:
    print("Your quadratic has 2 solution.")
elif discriminant == 0:
    print("Your quadratic has 1 root.")
elif discriminant < 0:
    print("Your quadratic has no roots.")