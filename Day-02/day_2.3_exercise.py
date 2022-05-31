# 🚨 Don't change the code below 👇
age = input("What is your current age?: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
assume_total_age = 90
remaining_age = assume_total_age - int(age)

remaining_month = remaining_age * 12
remaining_weeks = remaining_age * 52
remaining_days = remaining_age * 365
# print(remaining_month)
# print(remaining_weeks)
# print(remaining_days)
message = f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_month} month left."
print(message)