# Integer and Float Variables Practice test

gross_salary = 10000
health_insurance = 430.99
rent = 1200
food = 400.5
salary_tax = 0.2

partial_salary1 = gross_salary * salary_tax
partial_salary2 = health_insurance + rent + food
partial_salary3 = gross_salary - partial_salary1

net_salary = partial_salary3 - partial_salary2

print("Net Salary is: " + str(net_salary))

donation_amt = net_salary * 0.10

print("The amount of Donation to be given to the poor is: " + str(donation_amt.__round__(2)))