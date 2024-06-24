# Take user input for the main string
str1 = input("Enter the main string: ")

# Take user input for the string to be inserted
str2 = input("Enter the string to be inserted: ")

# Calculate the middle index of the main string
mid2 = len(str1) // 2

# Insert the string in the middle
str3 = str1[:mid2] + str2 + str1[mid2:]

print("Result:", str3)
