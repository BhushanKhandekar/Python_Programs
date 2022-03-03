# TASK 01 : A company deccided to give bonus of 5% to employee if his / her year of service is more than 5 years. 
# Ask user for thair salary and year of service and print net amount bonus

salary = float(input("Enter the salary :"))
n = float(input("Enter the number of year of service : "))
if n > 5:
    bonus = salary // 20
else:
    bonus = 0
net_amt = salary + bonus
print("net bonus amount = ",net_amt)