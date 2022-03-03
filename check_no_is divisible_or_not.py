# check a number whether the number is divisible by 5, 11, 15
# input : 55 --- output :  divisible  by 5 ,divisible by 11, not divisible by 15.
# n = 55
# d = { 5 : "divisible by 5" , 11 : "divisible by 11" , 15 : "not divisible by 15"}
# print(d.get(5),"\n",d.get(11),"\n",d.get(15))



n = int(input())
if n % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5")

if n % 11 == 0:
    print("divisible by 11")
else:
    print("Not divisible by 11")

if n % 15 == 0:
    print("divisible by 15")
else:
    print("Not divisible by 15")

