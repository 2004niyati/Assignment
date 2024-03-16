#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

integer1 = int(input("Enter the first integer1: "))
integer2 = int(input("Enter the second integer2: "))

if integer1 == integer2 or integer1 - integer2 == 5 or integer1 + integer2 == 5:
    print("True")
else:
    print("False")

