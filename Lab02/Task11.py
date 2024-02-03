# Write a program to compute quotient and remainder of a number without using division ('/') operator
# and modulo ('%') operator. Also mention procedure for calculating

# Take the dividend and divisor as input from the user.
# Initialize the quotient to 0 and the remainder to the dividend.
# While the remainder is greater than or equal to the divisor, subtract the divisor from the remainder and increment the quotient by 1.
# After the loop, print the quotient and remainder.

dividend=int(input("Enter dividend:"))
divisor=int(input("Enter divisor:"))
quotient=0
remainder=dividend
while remainder>=divisor:
    remainder-=divisor
    quotient+=1
print("Quotient",quotient)
print("Remainder",remainder)