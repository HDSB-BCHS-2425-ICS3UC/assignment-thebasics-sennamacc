"""
Author: Senna Chan Carusone
Date Modified: February 25th, 2025
Description: A program to calculate the discriminant, which is b^2 – 4ac (from the quadratic formula)
"""
print("I will help you calculate discriminant. The discriminant is used in finding roots of a quadratic.")
print("If it produces a negative number, there are no roots. If it produces zero, there is one root. And if it produces a positive number, there are two roots.")
a = float(input("Please input the value for a:\n"))
b = float(input("Please input the value for b:\n"))
c = float(input("Please input the value for c:\n"))

print("Thank you!")
discriminant = b**2 - 4*a*c
print("Discriminant =",discriminant)