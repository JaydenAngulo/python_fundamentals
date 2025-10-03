# USER INPUT IN PYTHON

print("\n--- User Input Demonstration ---\n")

name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
print(type(age))

age_number = int(age)
print("Next year, you will be: ", age_number + 1)
print(type(age_number))

# Example with float input
height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

favorite_color = input("Enter your favorite color: ")
print("Your favorite color is: ", favorite_color)

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))
print("The answer is: ", first_number + second_number)

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.

import math
diameter = int(input("Enter the diameter: "))
radius = diameter / 2
print("The area of the circle is: ", (math.pi * (radius ** 2)))

# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

import random
sides = int(input("What die do you want: "))
print("I landed on:", random.randint(1, sides))