# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi =int(weight)/(float(height)**2)
print(int(bmi))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you are slightly Normal weight")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are slightly obese")
else:
    print(f"Your BMI is {bmi}, they are  clinically obese")