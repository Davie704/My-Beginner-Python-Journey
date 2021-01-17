# Collections Set

drinks = {"Cola", "Sprite", "Beer", "Water", "Soda"}
print("\nMy Set: " + str(drinks))

#drinks.add("Pepsi")
#print(drinks)
drinks.add("Soda")
print("\nMy Set with additional item: " + str(drinks))

drinks.remove("Soda")
print("\nSoda was removed: " + str(drinks))

drinks_2 = drinks.copy()
print("\nDrinks 1 copy: " + str(drinks_2))

print("Length of Set: " + str(len(drinks)))
