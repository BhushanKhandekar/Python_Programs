a = int(input())
b = int(input())
c = int(input())

if a > b and a < c:
    print("median is", a)
elif b > a and b < c:
    print("median is", b)
else:
    print("median is", c)

