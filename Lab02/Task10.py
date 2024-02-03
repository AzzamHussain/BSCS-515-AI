# Write a program that calculates the user’s body mass index (BMI) and classify it as underweight,
# normal, overweight, or obese, based on the table from the United States Centers for Disease Control.


# The Body Mass Index (BMI) is calculated using the following formula:

# BMI = weight / (height * height)

# where:

# weight is measured in kilograms (kg)
# height is measured in meters (m)
# The BMI formula calculates an individual's body mass relative to their height. Once you have calculated the BMI, you can use the following classification from the United States Centers for Disease Control (CDC) to determine whether the individual is underweight, normal weight, overweight, or obese:

# BMI less than 18.5: Underweight
# BMI between 18.5 and 24.9: Normal Weight
# BMI between 25 and 29.9: Overweight
# BMI 30 or greater: Obese

w=float(input("Enter your weight in kg:"))
h=float(input("Enter your height in meters:"))
BMI=w/(h*h)
print("Your Body Mass Index (BMI) is:",BMI)
if BMI<18.5 :
    print("You are underweight")
elif BMI>18.5 or BMI<24.9:
    print("Normal Weight")
elif  BMI>25 or BMI<29.9:
    print("overweight")
elif  BMI>=30:
    print("Obese")


