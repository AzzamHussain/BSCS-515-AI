#I. a Python program to square and cube every number in a given list of integers using Lambda. 
list =[3,8,9,6,4]
square=lambda a:a**2
cube=lambda b:b**3
s = [square(num) for num in list] #to apply lambdas to each element of the list
c = [cube(num) for num in list]
print("The square of given numbers are:",s)
print("The cube of a given numbers are:",c)