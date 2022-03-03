# TASK 08 : A student will not be allowed to sit in the exam if his / her attendance is less than 75 %.
# Take following input from the user.
# 1. Number of classes held.  2.Number of classes attended. 
# print : 1. percentage of class attended   2. Is student allowed to sit in the exam or not.

# if NCH = 200 --- NCA = 120 --- PCA = ( 120 / 200 ) * 100 = 60 % --- Not Allowed

n = int(input("Enter Number of Classes Held : "))
a = int(input("Enter Number of Classes Attended : "))
p = ( a / n ) * 100
print("Percentage of Class Attended = ",p)

if p > 75:
    print("Allowed to Sit in the Exam")
else:
    print("Not Allowed to Sit in the Exam")
