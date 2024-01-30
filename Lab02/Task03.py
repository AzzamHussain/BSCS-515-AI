# (iii)The program must prompt the user for a username and password. The program should compare 
# the password given by the user to a known password. If the password matches, the program should 
# display “Welcome!” If it doesn’t match, the program should display “I don’t know you.
# Note: the password should not be case sensitive and it’s value is abc$123 or ABC$123
username=(str(input("Input user name:")))
password=(str(input("Enter password")))
if username=='AzzamHussain' and password=='abc$123':
    print("Welcome")
else:
    print("I dont know you")