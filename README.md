# Task 1
## Version 1 specs - with concatenation
### define a variable name, and assign a string
`name = ""`
### re assign the original variable with your name
`name = input("What is your name? ")
name_capitalize = name.capitalize()`
### use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
print(name_capitalize + " Welcome to this task!")
# Task 2
## Version 2 - with interpolation
### define another variable full_name to a random string
`full_name = ""`
### re assign the variable full_name to a name
`full_name = input('What is your full name? ')
first_name = (full_name.split()[0])
first_name_capitalize = first_name.capitalize()
last_name = (full_name.split()[1])
last_name_capitalize = last_name.capitalize()
full_name_capitalize = first_name_capitalize + " " + last_name_capitalize`
### use interpolation to print the message
print(full_name_capitalize + " Welcome to this task!")