# Write a Python program to calculate the length of a string.

#Without inbuilt function.
string = input("Enter a String: ")

# character variable to count the character in a string
character = 0
for i in string:
    character = character+1
print("Length of the string is:",character)


#With inbuilt function.

string = input("Enter a String: ")

print("Length of the string is:",len(string))
