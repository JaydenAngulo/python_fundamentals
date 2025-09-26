#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 7 + 2
print("Sum: ", add)

subtract = 7 - 2
print("Difference: ", subtract)

multiply = 7 * 2
print("Product: ", multiply)

float_divide = 7 / 2
print("Float Division: ", float_divide)

integer_divide = 7 // 2
print("Integer Division: ", integer_divide)

modulus = 7 % 2
print("Modulus: ", modulus)

exponent = 7 ** 2
print("Exponent: ", exponent)

print(2 + 2 == 10 -6)

result1 = (2 + 3) * 4
print("Result 1: ", result1)

result2 = 2 ** 3 * 4
print("Result 2: ", result2)

result3 = 20 / 5 * 2
print("Result 3: ", result3)

result4 = 10 - 2 + 3
print("Result 4: ", result4)

result5 = 5 + 2 ** 3 * (4 - 1)
print("Result 5: ", result5)

#CHALLENGES

# Challenge 1: Rectangle Area
# Calculate the area of a rectangle with a width of 8 and a height of 5.

rectangle_area = 8 * 5
print("Area of Rectangle = ", rectangle_area)

# Challenge 2: Circle Area
# Use the formula pi r2 to calculate the area of a circle with radius 7.
# (Use 3.14 for pi.)

circle_area = 3.14 * 7 ** 2
print("Area of Circle = ", circle_area)

# Challenge 3: Shopping Total
# A book costs $12.99 and a notebook costs $3.50.
# Calculate the total cost for 3 books and 4 notebooks.

shopping_total = (3 * 12.99) + (4 * 3.5)
print("Shopping Total = ", shopping_total)

# Challenge 4: Even or Odd
# Create a variable that holds any integer.
# Use the modulus operator to check if the number is even or odd.
# Explain your reasoning.

variable = 7
even_or_odd = variable % 2
if even_or_odd == 0:
    print("even")
if even_or_odd == 1:
    print("odd")