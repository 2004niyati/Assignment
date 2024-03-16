# 17 Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.


string="Hello,How are you,"
x=list(string)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
print("".join(x))
