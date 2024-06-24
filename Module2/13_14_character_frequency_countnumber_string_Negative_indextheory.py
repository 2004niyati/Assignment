#13: Write a Python program to count the number of characters (character frequency) in a string.

str1="Hello,How are you?"
chr={}
for i in str1:
    if i in chr:
        chr[i] += 1
    else:
        chr[i] = 1
print("Count of all Character:",chr)


#14: What are negative indexes and why are they used?
ANS:  The index of the last element refers to -1 , the second element from the last refers to -2 , and so on.
      The index() method along with the len() function to get the index of the list element from the ending point.
