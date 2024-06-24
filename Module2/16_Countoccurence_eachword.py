# 16.Write a Python program to count the occurrences of each word in a given sentence.

count = 0

# Opens a file in read mode 
str1 = "Apple,Banana"
  
# Gets each line till end 
for line in str1: 
    # Splits into words 
    word = line.split(" ") 
    # Counts each words 
    count += len(word) 
  
print("Total Number of Words:" +str(count))  
