# Basic string creation and indexes:
greeting = "Hello"
name = "Ada"
print(greeting, name)

# 0 1 2 3 4
# H e l l o
second_letter = greeting[1]
print(second_letter)

# Concatenation:
message = greeting + " " + name + "!!!!"
print("Concatenated message:", message)

print()
# Splicing
word = "Super-cali-fragil-istic-expi-ali-docious"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Range of letters (non-inclusive):", word[:-1])
print(word[:5])
print("Last seven letters:", word[:-7])
print("Step through every second character:", word[::2])
print("Reversed, stepping every third letter:", word[::-3])

## Built in string functions

country = "Finland"
length_of_word = len(country)
print(length_of_word)

phrase = "spOngEBOB"
print("\nUppercase:", phrase.upper())
print("Lowercase:", phrase.lower())
print("Capitalized first letter:", phrase.capitalize())
print("Title format:", phrase.title())

print()

# Find and replace text
sentence = "I'm a goofy goober"
new_sentence = sentence.replace("I'm", "You're")
next_replacement = sentence.replace("goofy", "goober")
print(sentence)
print(new_sentence)
print(next_replacement)

# FORMATTED STRINGS IN PYTHON
# f-strings allow variables and expressions inside strings

print("\n--- Formatted Strings ---")

name = "Jayden"
age = 14
city = "Flemington"

print(f"Hello, my name is {name}. I am {age} years old and I live in {city}.")

# f-strings can do math and function calls inside {}

print(f"Next year, I'll be {age + 1}. My name in uppercase is {name.upper()}.")

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

favorite_quote = input("Enter your favorite quote: ")
length_of_quote = len(favorite_quote)
if len(favorite_quote) == 1:
    print(f"Your quote is {length_of_quote} letter long.")
else:
    print(f"Your quote is {length_of_quote} letters long.")

# Challenge 2: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Output formatted name: Lovelace, Ada

first_name = input("Enter your first name: ")
last_name = input("Now enter your last name: ")
print(f"{last_name.capitalize()}, {first_name.capitalize()}")

# Challenge 3: Word Mutation
# Ask for a word and print it backwards, in uppercase, and lowercase.
# Example output
# Enter a word: Python
# Uppercase: PYTHON
# Lowercase: python
# Backwards: nohtyP

premutated_word = input("Enter a word: ")
print("The word uppercase is: ", premutated_word.upper())
print("The word lowercase is: ", premutated_word.lower())
print("The word backwards is: ", premutated_word.capitalize()[::-1])