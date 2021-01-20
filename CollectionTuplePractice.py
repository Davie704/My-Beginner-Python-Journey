# Collections Tuple Practice Test

# 1
tech_terms = ("PYTHON", "PYCHARM IDE", "TUPLE", "COLLECTIONS", "STRING")
print(tech_terms)

# 2
print("We are Ninja Developers. We write " + str(tech_terms[0]) + " code in " + str(tech_terms[-4]) +
      " and now practicing " + str(tech_terms[2]) + " collections topic that contains " + str(tech_terms[-1]) + " variable")

# 3
var_list = ["Thanks.", 99.0]

add_tech = list(tech_terms)
add_tech.extend(var_list)
print(add_tech)

# 4
single_cell_tuple = (1,)
print(type(single_cell_tuple))

int(single_cell_tuple[0])
print(type(single_cell_tuple[0]))
print("Singe Tuple Type: " + str(single_cell_tuple))