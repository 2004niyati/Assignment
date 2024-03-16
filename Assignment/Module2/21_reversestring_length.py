#user input
input_string = input("Enter string:")

# Check if the length of the string is a multiple of 4
if len(input_string) % 4 == 0:
    # Reverse the string
    reversed_string = input_string[::-1]
    print("Reversed string :",reversed_string)
else:
    # If the length is not a multiple of 4, print the original string
    print("Original string:",input_string)

