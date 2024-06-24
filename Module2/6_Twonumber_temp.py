#write python program that swap two number with temp variable and without tenp variable.
Nu1=int(input("Enter Nu1:"))
Nu2=int(input("Enter Nu2:"))
temp=Nu1
Nu1=Nu2
Nu2=temp
print("The value of Nu1 After Swapping:",Nu1)
print("The value of Nu2 After Swapping:",Nu2)



#Without temp Variable:

S=int(input("Enter Number S:"))
N=int(input("Enter Number N:"))
S,N=N,S
print("THE VALUE OF S AFTER SWAPPING:",S)
print("THE VALUE OF N AFTER SWAPPING:",N)
