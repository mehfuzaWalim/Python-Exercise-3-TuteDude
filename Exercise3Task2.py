#Program to take number from user and display its square root, log and sine value using math module
import math

num=int(input("Enter a number: "))
sqr_root = math.sqrt(num)
log = math.log(num)
sin = math.sin(num) 

print("\n")
print("Square root: ", sqr_root)
print("Logarithm: ", log)
print("Sine: ", sin)

