# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

print()
print("--- Conditionals in Python ---")

print( 3 == 2 )
print("Hello" == "Hi there")
print( 7 != 4 )
print( 4 > 5 )

print()
print()
print()
print()

# if
num1 = 10
if num1 == 10:
    print("Your number is equal to 10")

num2 = 13
print(num2 <= 12)
if num2 <= 12:
    print("Your number is less than or equal to 12")
else:
    print("Your number is greater than 12")

#if elif else

temperature = 68
if temperature >= 80:
    print("It's hot!")
elif temperature >= 60:
    print("It's nice.")
else:
    print("It's cold!")

print()
print()

x = 2
y = 20

if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("error")

# Logical operator: and
# Both sides of the 'and' must be true, otherwise it's false.
print()
print()
print()

age = 17
has_permission = True

if age >= 17 and has_permission:
    print("You can drive")
else:
    print("Can't drive yet")

# Using 'or' and 'not'
print("--- Using 'or' ---")

day = "Saturday"

if day is "Saturday" or day is "Sunday":
    print("It's the weekend!")
elif day is "Monday" or day is "Tuesday" or day is "Wednesday":
    print("It's Monday or Tuesday or Wednesday")
else:
    print("It's Wed, Thur, or Fri")

if day is not "Monday":
    print("It's not Monday")

# Challenge 1: Even or Odd
# Ask the user for a number, and tell them if it’s even or odd.
# Example output:
# Enter a number: 7
# 7 is odd.
# Hint: use modulus operator

even_or_odd = int(input("Pick a number: ")) % 2
if even_or_odd == 0:
    print("The number is even")
if even_or_odd == 1:
    print("The number is odd")

# Challenge 2: Password Check
# Create a variable with a stored password
# Ask the user to enter a password. 
# If it matches the stored password, print "Access granted." Otherwise, "Access denied."
# Example output:
# Enter password: dolphin
# Access granted. Access denied.
# Enter password: swordfish
# Access granted.

real_password = "Shell$5"
password_input = input("Enter a password: ")
if password_input == real_password:
    print("Access granted")
else:
    print("Access denied")

# Challenge 3: Grading System
# Ask the user for a numeric grade (0-100) and print a letter grade (A,B,C,D,F).
# Example output:
# Enter your grade: 81
# You earned an B.

grade = int(input("Enter your numeric grade: "))
if grade <= 64:
    print("You earned an F")
if grade >= 65 and grade <= 73:
    print("You earned a D")
if grade >= 74 and grade <= 82:
    print("You earned a C")
if grade >= 83 and grade <= 91:
    print("You earned a B")
if grade >= 92:
    print("You earned an A")