# Collections Lists Practice Test Advance

# 1 Create list of employees
employees = ["Adam", "John", "Greg", "Danna", "Ashly"]
print(employees)
# 2 print list length
print("Length of list: " + str(len(employees)))
# 3 John quited and came Jay
employees[1] = "Jay"
print("John was replaced by Jay: " + str(employees))
# 4 Another guy joined the team, James
employees.insert(3, "James")
print("James was hired: " + str(employees))
# 5 Remove James from the list and add him to be last
employees.remove("James")
print("James was removed from 3rd place: " + str(employees))
employees.append("James")
print("James was added to last place: " + str(employees))
# 6 James got fired - remove him using pop()
employees.pop(5)
print("James was fired: " + str(employees))
# 7 Sort the list ASC
employees.sort()
print("Sorted the employees ASC: " + str(employees))
# 8 Sort the list DES
employees.sort(reverse = True)
print("Sorted the employees DES: " + str(employees))