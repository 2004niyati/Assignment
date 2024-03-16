# 18 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add
#'ly' instead if the string length of the given string is less than 3, leave it unchanged.

string1 = input("Enter a Str:")
if len(string1) < 3:
  print(string1)
elif string1[-3:] == 'ing':
  print(string1 + 'ly')
else:
  print(string1 + 'ing')
