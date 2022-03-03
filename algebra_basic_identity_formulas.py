# Program to Solve the Expression (a+b)^2 & (a-b)^2
a = int(input("enter a value : "))          # a=2
b = int(input("enter b value : "))          # b=3
exp1 = a**2 + 2*a*b + b**2             # exp1 = 2^2 + 2*2*3 + 3^2 = 25
exp2 = a**2 - 2*a*b + b**2             # exp2 = 2^2 - 2*2*3 + 3*3 = 1
print("-------after solving-------\n (a+b)^2 =",exp1,"& (a-b)^2 =",exp2)