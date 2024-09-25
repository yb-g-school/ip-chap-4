#bmi calculator
w = float(input("Enter your weight (in kg): "))
h = float(input("Enter your height (in m): "))
bmi = w /(h*h)

if bmi < 18.5:
    print("Your BMI is",bmi)
    print("You are underweight!")
if bmi>=18.5 and bmi<25:
    print("Your BMI is",bmi)
    print("Your BMI is normal!")
if bmi >= 25 and bmi < 30:
    print("Your BMI is",bmi)
    print("You are overweight!")
if bmi >= 30:
    print("Your BMI is",bmi)
    print("You are obese!")
