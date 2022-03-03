# TASK 02 : Take the values of length and breath of a rectangle from the user and check if it is square or not.
# Rectangle : A rectangle is a quadrilateral with all four angles are right angles.
# NOTE : Every square is rectangle, but every rectangle is not a square.

l = int(input("Enter the length : "))
b = int(input("Enter the breath : "))

if l==b:
    print("It is a square.")
else:
    print("It is not a suqare.")