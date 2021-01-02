# My Learning Python Journey

# A simple string example
short_string_example = "Have a great week, Ninjas!"
print(short_string_example)

# Print the first letter of a string variable, index 9
first_letter_variable = "New York City"[9]
print(first_letter_variable)

# Mixed upper and lowercase variable
mixed_letter_variable = "ThiS iS a MIxED vaRiAble"
print(mixed_letter_variable.lower())

# Length of the variable
print(len(mixed_letter_variable))

# Use '+' sign inside a print command
first_name = "David"
print("First Name is: " + first_name)

# Adding String and Integer
age = 25
print("Age: " + str(age))

# Replace a part of a string
first_serial_num = "ABC123"
print("Change serial number: " + first_serial_num.replace('123', '456'))

# Replace a part of a string TWICE
second_serial_num = "ABC123ABC123ABC"
print("Changed serial number 2: " + second_serial_num.replace('ABC', 'ZZZ', 2))

# Take a part of a variable according to specific index range
range_of_indexes = second_serial_num[2:7]
print(range_of_indexes)

# Adding spaces between multiple variables in print
first_word = "Thank"
second_word = "You"
third_word = "Python"
print(first_word + " " + second_word + " " + third_word)
