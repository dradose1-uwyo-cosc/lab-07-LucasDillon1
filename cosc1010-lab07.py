# Lucas Dillon
# UWYO COSC 1010
# Submission Date: 10/28/24
# Lab 7
# Lab Section: 16
# Sources, people worked with, help given to: NA
# 

# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered


factorial = 1

while True:
    upper_bound = input("Please enter a number for an upper bound:\n")
    if upper_bound.isdigit():
        upper_bound = int(upper_bound)
        for i in range(1, upper_bound + 1):
            factorial = factorial * i
        print(f"\nThe result of the factorial based on the given bound is {factorial}\n")
        break
    else:
        print("\nThe upper bound given is not an integer, and will not work.\n")


print("*"*75)

# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

num_sum = 0 

while True:
    add_to = input("\nEnter an integer to add to the value of the sum. type exit to finish.\n")
    if add_to.isdigit():
        num_sum += int(add_to)
# This section is a little iffy, because typing 10- would also end up subtracting (for strip()). I fixed with lstrip (I think).
    elif "-" in add_to:
        add_to = add_to.lstrip("-")
        if add_to.isdigit():
            num_sum -= int(add_to)

    elif add_to.lower() == "exit":
        break
    else:
    
        print(f"\n{add_to} is not a valid input\n")


print(f"\nYour final sum is {num_sum}\n")

print("*"*75)

# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

while True:
    op = input("Please input two numbers and one operator in the form: 'operand operator operand'. Type exit to finish.\n")

# Easy exit method
    if op.lower() == 'exit':
        break

# Gets rid of whitespace (yay for easy method).
    op = op.strip()

# A list of possible operators.
    operators = ["+", "-", "*", "/", "%"]

# A method of getting only the numbers, each bundled nice and separate.
    for character in op:
        if character in operators:
            op = op.split(character)
            operator = character

# Makes op hold integers
    op[0] = int(op[0])
    op[1] = int(op[1])

# I gave up on a for loop for now. Super inefficient below.
    if operator == "+":
        new_num = op[0] + op[1]

    elif operator == "-":
        new_num = op[0] - op[1]

    elif operator == "*":
        new_num = op[0] * op[1]
    
    elif operator == "/":
        new_num = op[0] / op[1]

    elif operator == "%":
        new_num = op[0] % op[1]

    print(new_num)