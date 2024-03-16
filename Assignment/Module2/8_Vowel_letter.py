#Write a python program to test whether a passed letter is a vowel or not.
Character=input("Enter Character:")
Vowel=['a','e','i','o','u','A','E','I','O','U']
if Character in Vowel:
    print("The Character Is Vowel")
else:
    print("The Character Is Consonant")
