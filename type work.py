"""
Author: Senna Chan Carusone
Date Modified: February 24th, 2025
Description: Describing different variable types.
"""

#Defining variables
integer = int(1) #An integer is a whole number
float1 = float(2/3) #A float is a number with a decimal
string = str("cupcake") #A string is any character(s)
double = float(2/3) #A double is a number with a decimal
character = 'a' #A char is a single character
boolean = True #A boolean is a true or false

type = input("What type of variable would you like to learn about today?") #Getting user input
type = type.lower() #Making it so input is not case sensitive

#Printing explanation based on the user's choice
if type == "int" or type == "integer":
    print("An integer is any whole number, positive or negative. \nNOTE: If you convert a float to an integer, it does not round.\nIt just takes the number before the decimal place (even if it's .999)!\nAn example is: ",integer)
elif type == "float":
    print("A float is a number with a decimal.\nAn example is: ",float1)
elif type == "str" or type == "string":
    print("A string is one or a bunch of characters.\nTo write a string put quotes and write whatever you want inside.\nYour code can't interpret a string, even if it's a number.\nAn example is: ",string)
elif type == "double":
    print("A double is a number with a decimal.\nIn python it's the same as a float, but in other coding languages it's more accurate.\nAn example is: ",double)
elif type == "character" or type == "char":
    print("A char is a single character.\nAn example is: ",character)
elif type == "boolean":
    print("A boolean is a true or false.\nAn example is: ",boolean)
else:
    print("Invalid selection.") #In case the user types something random