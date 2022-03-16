height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))
calculated_bmi = round(weight / height**2)
if calculated_bmi < 18.5:
    print(f"Your BMI is {calculated_bmi}, you are under weight.")
elif calculated_bmi < 25:
    print(f"Your BMI is {calculated_bmi}, you have a normal weight.")
elif calculated_bmi < 30:
     print(f"Your BMI is {calculated_bmi}, you are slightly overweight.")
elif calculated_bmi < 35 :
    print(f"Your BMI is {calculated_bmi}, you are obese.")
else:
    print(f"Your BMI is {calculated_bmi}, you are clinically obese.")