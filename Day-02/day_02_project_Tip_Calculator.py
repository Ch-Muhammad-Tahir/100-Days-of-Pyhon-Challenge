#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator.")
bill = float(input("What is was the total bill? $"))
tip = int(input("What percentage tip would you like to give ? 10 , 12 or 15: "))
peoples = int(input("How many people to split The Bill: "))
tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill =bill+total_tip
pre_person_bill =total_bill/peoples
finla_ammoumt = "{:.2f}".format(pre_person_bill)
print(f"Each Person Should pay ${finla_ammoumt}")