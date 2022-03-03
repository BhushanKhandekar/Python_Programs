# Reverse of three digit number
a = 123
rem1 = a % 10       # rem1=3
a = a // 10         # a=12 (int quotient)
rem2 = a % 10       # rem2=2
a = a // 10         # a=1  (int quotient)
rev = rem1*100 + rem2*10 + a     # rev = 3*100 + 2*10 + 1 = 300 + 20 + 1 = 321 
print(rev)