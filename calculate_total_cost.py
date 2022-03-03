
# TASK 04 : A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity. Suppose one unit will cost 100. Judge and print total cost for user.
#   Q = 6 --- Cost = 600 --- discount = 0 % = 0 Rs.--- total cost = 600
#   Q = 15 --- Cost = 1500 --- discount = 10 % = 150 Rs. --- total cost = 1350

q = int(input("Enter the Quantity : "))
unit = int(input("Enter the cost per unit : "))
cost = q * unit

if  cost > 1000:
    d = cost * 0.1
else:
    d = 0

total_cost = cost - d
print("TOTAL COST = ",total_cost)