#Program to take number from user and calculate its factorial using a recursive function and print the factorial.
num=int(input("Enter a number: "))
def factorial(number):
	if(number==0):
		return 1
	else:
		return number*factorial(number-1)	#recursive function call
		
		
fact = factorial(num)
print("Factorial of ", num, " is: ",fact)

