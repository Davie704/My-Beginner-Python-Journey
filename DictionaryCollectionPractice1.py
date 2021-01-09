
# 1. Create a dictionary about Alex
alex = {"Age": 32, "Married": "Yes", "Kids": 3}
print("About Alex: " + str(alex))

# Extract all values of the dictionary, and assign them into simple variables
age = alex["Age"]
status = alex["Married"]
kids = alex["Kids"]

print("\nAge value: " + str(age))
print("Status value: " + status)
print("Number of Kids: " + str(kids))

# 3. ( <Challenge> )
alex.update({"Married": "Python update value of dictionary"})

# 4. Alex is now 33, update the value that belongs to the key = ‘Age’
alex.update({"Age": 33})
print("\nAlex's updated age: " + str(alex))

# 5. A little girl joined his family, update the ‘Kids’ key value into ‘4’
alex.update({"Kids": 4})
print("No. of Alex's Kids: " + str(alex))

# 6. Print out the values of the dictionary
print("\n'Value' of the Dictionary: " + str(alex.values()))

# 7. Print out the keys of the dictionary
print("'Keys' of the Dictionary: " + str(alex.keys()))