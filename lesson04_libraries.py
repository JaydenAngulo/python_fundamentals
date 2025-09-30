# Python libraries are repositories of code that you can use in your own files

import math
print("\n--- Math Library ---\n")

print("Square root: ", math.sqrt(25))
print("Round up to an integer: ", math.ceil(4.2))
print("Round down to an integer: ",math.floor(4.8))
print("Power: ", math.pow(2, 5))
print("Pi: ", math.pi)

seed = 53248
second_number = math.floor(seed / 734)
third_number = math.floor(second_number * 5.7)
random_number = math.floor(third_number + 7342)
print("Random number: ", random_number)