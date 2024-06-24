# Write a python program to sum of the first n positive integers.

n=int(input("Enter Positive n:"))
sum=0
if n<=0:
    print("Please Enter a Positive integer:")
else:
    for i in range(1,n+1):
        sum+=i
        print("The sum of a Positive integer:",sum)
