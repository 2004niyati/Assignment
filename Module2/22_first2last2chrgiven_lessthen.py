# Take user input for the string
input_string = input("Enter a string: ")

# Check if the length of the string is less than 2
if len(input_string) < 2:
    result_string = ""
else:
    # Get the first 2 and last 2 characters from the string
    result_string = input_string[:2] + input_string[-2:]

print("Result:", result_string)
