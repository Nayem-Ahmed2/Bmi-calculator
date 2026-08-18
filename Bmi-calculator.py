weight = float(input("Enter your weight in kg = "))
height = float(input("Enter your height in meters="))

bmi = weight / (height * height)

print("Your BMI is=", bmi)

if bmi < 18.5:
    print(" You are underweight")
elif bmi < 24.9:
    print("Your weight is normal")
elif bmi < 29.9:
    print("You are overweight")
else:
    print("High Obesity")
