a = (int)(input("Enter first number : " ))
b = (int)(input("Enter second number : "))
c = (int)(input("Enter third number : " ))
d = (int)(input("Enter fourth number : " ))

if(a > b and a > c and a > d):
    print("a is greatest number")
elif(b > c and b > d and b > a):
    print("b is greatest number")
elif(c > d and c > a and c > b):
    print("c is greatest number")
else:
    print("d is greatest number")


