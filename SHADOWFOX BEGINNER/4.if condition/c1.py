'''
1. Write a program to determine the BMI Category based on user input.
Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal"
'''
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)
print("BMI:", round(bmi, 2))


if bmi >= 30:
    print("Output: Obesity")
elif bmi >= 25:
    print("Output: Overweight")
elif bmi >= 18.5:
    print("Output: Normal")
else:
    print("Output: Underweight")