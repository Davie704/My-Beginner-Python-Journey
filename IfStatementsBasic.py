# If statement basics

# Ex 1
salary = 8000
if salary > 5000:
    print("My salary is too low!")
else:
    print("My salary is above average, its okay right now.")

# Ex 2
age = 55
if age > 50:
    print("You're a senior Developer, for sure!")
elif age > 40:
    print("You're more than 40 years old.")
elif age > 35:
    print("You're more than 35 years old.")
else:
    print("Doesn't matter what age you are. Let's start learning programming!")

# Ex 3 Logical Operators
a = 10
b = 5
c = 2

if a > b or a > c:
    print("\nOne of the conditions is true")
else:
    print("\nNone of them is true")

if b < a < c:
    print("\nOne of the conditions is true")
else:
    print("\nOne or None of them is true")

# Ex 4 Nested 'If Statement'
age = 30
name = "James"
married = True

if age > 20 and name =="James":
    if married == True:
        print("\nCongratulations! The statement is TRUE!")
    else:
        print("\nThe statement is FALSE :(.")
else:
    print("\nThis is from the parent 'else'.")