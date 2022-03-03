
# TASK 09 : Write a program to calculate the electricity bill ( accept number of unit from the user )
# According to the foloowing Unit Price 
# First 100 units --- No Charge  ----------- 0 - 100 
# Next 100 units --- Rs. 5 per unit  ----- 101 - 200 
# Ater 200 units --- Rs. 10 per unit  ------ 201 - 400
# Above that Rs. 15 per unit  -------------- 401 -

u = float(input("Enter Number of Unit : "))

if u <= 100:
    print("No Charge")
elif 200 >= u > 100:
    total = u * 5
elif 400 >= u > 200:
    total = u * 10
else:
    total = u * 15

print("Total = ",total)

