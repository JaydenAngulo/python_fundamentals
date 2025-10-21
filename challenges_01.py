# Challenge 1: Palindrome Checker

is_palindrome = input("Enter a word:")
backwards_is_palindrome = is_palindrome[::-1]
print(is_palindrome == backwards_is_palindrome)

# Challenge 2: Domain from Email

email = input("Enter your email: ")
domain_symbol = email.index("@") + 1
domain = email[domain_symbol::]
print(domain)

# Challenge 3: First and Last Match

given_list = ["apple", "orange", "banana"]
last_fruit = given_list[-1]
chosen_fruit = input("Choose a fruit: ")
print(chosen_fruit == last_fruit)

# Challenge 4: Conditional Suffix Adder

base_word = input("Enter a word: ")
base_word_length = len(base_word)
if base_word_length < 3:
    print(base_word)
elif base_word[-3:-1] != "ing":
    print(f"{base_word}ing")
else:
    print(f"{base_word}ly")