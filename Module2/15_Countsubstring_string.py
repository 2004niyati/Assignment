# 15.Write a Python program to count occurrences of a substring in a string.

str1 = "alphabbeticalbb,bbanna"
str2 = 'bb'
 
count = 0
n = len(str1)
m = len(str2)
 
for i in range(n - m + 1):
    if str1[i:i+m] == str2:
        count += 1
 
print("Number of substrings:", count)
