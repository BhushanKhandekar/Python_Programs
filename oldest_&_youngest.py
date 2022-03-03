# TASK 06 : Take the input of age of 3 people by user and determine oldest and youngest among them.

p1 = int(input())
p2 = int(input())
p3 = int(input())

if p1 >= p2 and p1 >= p3 or p3 <= p1 and p3 <= p2:
    print("Oldest is", p1,"Youngest is", p3)
elif p2 >= p1 and p2 >= p3 or p1 <= p2 and p1 <= p3:
    print("Oldest is", p2,"Youngest is", p1)
elif p3 >= p1 and p3 >= p2 or p2 <= p1 and p2 <= p3:
    print("Oldest is", p3,"Youngest is", p2)
elif p3 >= p1 and p3 >= p1 or p1 <= p2 and p1 <= p3:
    print("Oldest is", p3,"Youngest is", p1)
elif p1 >= p2 and p1 >= p3 or p2 <= p1 and p2 <= p3:
    print("Oldest is", p1,"Youngest is", p2) 
elif p2 >= p1 and p2 >= p3 or p3 >= p1 and p3 >= p2:
    print("Oldest is", p2,"Youngest is", p3)
else:
    print("All are equal")