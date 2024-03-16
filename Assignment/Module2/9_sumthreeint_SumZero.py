#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))

if a==b or b==c or c==a:
    print("sum will be zero")
else:
    total=a+b+c
    print("The total is equal:",total)
