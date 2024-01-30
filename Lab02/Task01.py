# (I)Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes 
# inputs like height, width and depth from user and then calculate volume of the cube:
# volume = height ∗ width ∗ depth
# After calculating volume of cube, compare it with following ranges and print the relevant label:
# Volume Range Label
# 1 cm3 
# – 10 cm3     Extra Small
# 11 cm3 
# – 25 cm3      Small
# 26 cm3 
# – 75 cm3       Medium
# 76 cm3 
# – 100 cm3      Large
# 101 cm3 
# – 250 
# cm3
# Extra          Large
# 251 cm3 and 
# above
#              Extra-Extra 
#                      Large
h=float(input("Enter the height:"))
w=float(input("Enter width:"))
d=float(input("Enter depth:"))
volume=h*w*d
print("The volume is: ",volume)
if volume>=1 or volume<=1:
    print("Extra small")
elif    volume>=11 or volume<=25:
    print("small")
elif    volume>=26 or volume<=75:
    print("Medium")
elif    volume>=76 or volume<=100:
    print("Large")
elif    volume>=101 or volume<=250:
    print("Extra large")
else:
    print("Extra-Extra large")


    


