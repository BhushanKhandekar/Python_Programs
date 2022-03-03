# TASK 05 : A school has following rules for grading system : 
# a. Below 25 - F  ---  marks < 25
# b. 25 to 45 - E  ---  25 < marks < 45 
# c. 45 to 50 - D  ---  45 < marks < 50
# d. 50 to 60 - C  ---  50 < marks < 60
# e. 60 to 80 - B  ---  60 < marks < 80
# f. Above 80 - A  ---  80 < marks
# Ask user to enter marks and print the corresponding grades. 

m = int(input("Enter the marks : "))

if m < 25:
    print(" F ")
elif 45 > m >= 25:
    print(" E ")
elif 50 > m >= 45:
    print(" D ")
elif 60 > m >= 50:
    print("  C ")
elif 80 > m >= 60:
    print(" B ")
else:
    print(" A ")
