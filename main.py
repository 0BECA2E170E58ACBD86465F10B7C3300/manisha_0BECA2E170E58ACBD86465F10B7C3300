# python program to find the factor of a number provided by the user.

#change the value for a different result
num =7

#To take input from the user
#num = int(input("Enter a number:"))

factorial = 1

#check if the number is negative
if num < 0:
    print("sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num +1):
        factorial = factorial*i
    print("The factoriaal of",num,"is",factorial)