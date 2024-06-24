# 20  Write a Python function that takes a list of words and returns the length of the longest one.

list1 = ['gfg', 'is', 'best', 'for', 'geeks','geeksworld','kjjkjkjkjkjhgfghj']
 
# printing original list 
print("The original list : ",str(list1))
 
# Longest String in list
# using max() + key
list2 = max(list1, key = len)
 
# printing result
print("Maximum length string is : ",list2)
