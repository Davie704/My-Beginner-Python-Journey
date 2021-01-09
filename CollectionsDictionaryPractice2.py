# Collection Dictionary Practice Test 2

# 1. Create a nested dictionary of building attendants, the building has 3 apartments on 2 floors:
building_attendants = {"floor1": {"first_apartment": "Rachel", "second_apartment": "Jean"}, "floor2": {"third_apartment": "Jay"}}

# 2. Print all nested cell items of the 1st floor
print(building_attendants["floor1"])

# 3. Print out the resident in the ‘second_apartment’
print(building_attendants["floor1"]["second_apartment"])

# 4. Additional apartment was built on the second floor, and a new resident moved to the new 4th apartment-her name is Carroll
building_attendants["floor2"]["fourth_apartment"]  = {"Carroll"}
print(building_attendants)

# 5. The building owner decided to let his daughter in the first apartment, so it would not be leased any more
# 1st way using 'del'
del building_attendants["floor1"]["first_apartment"]
print(building_attendants)

# 2nd way using '.pop()'
floor_3 = building_attendants["floor2"].pop("third_apartment")
# print("Floor 3: " + str(floor_3))
print(building_attendants)