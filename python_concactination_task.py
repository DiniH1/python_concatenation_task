
# Task 1
name = ""
name = input("What is your name? ")
name_capitalize = name.capitalize()
print(name_capitalize + " Welcome to this task!")
# Task 2
full_name = ""
full_name = input('What is your full name? ')
first_name = (full_name.split()[0])
first_name_capitalize = first_name.capitalize()
last_name = (full_name.split()[1])
last_name_capitalize = last_name.capitalize()
full_name_capitalize = first_name_capitalize + " " + last_name_capitalize
print(full_name_capitalize + " Welcome to this task!")

